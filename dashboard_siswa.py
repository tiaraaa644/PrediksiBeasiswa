import pandas as pd
import pymysql
import streamlit as st
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Koneksi ke database dan ambil data
def get_data():
    # Koneksi ke database MySQL
    connection = pymysql.connect(
           host=st.secrets["DB_HOST"],
            database=st.secrets["DB_DATABASE"],
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"]
    )

    # Mengambil data siswa, akademik, dan non-akademik
    query_siswa = "SELECT nis, nama, kelas FROM data_siswa"
    query_akademik = "SELECT nis, total_nilai_uts, total_nilai_uas FROM data_akademik"
    query_non_akademik = "SELECT nis, total_score FROM data_non_akademik"

    df_siswa = pd.read_sql(query_siswa, connection)
    df_akademik = pd.read_sql(query_akademik, connection)
    df_non_akademik = pd.read_sql(query_non_akademik, connection)

    # Menggabungkan data berdasarkan NIS
    df = pd.merge(df_siswa, df_akademik, on='nis')
    df = pd.merge(df, df_non_akademik, on='nis')

    # Menghitung total skor
    df['total_uts_uas'] = df['total_nilai_uts'] + df['total_nilai_uas']
    df['total_skor_akhir'] = df['total_uts_uas'] + df['total_score']

    # Tentukan apakah siswa layak mendapatkan beasiswa (threshold lebih dari 200 untuk layak)
    threshold = 1900
    df['layak_beasiswa'] = df['total_skor_akhir'].apply(lambda x: 'layak' if x > threshold else 'tidak layak')

    return df

# 2. Menampilkan data dan hasil seleksi menggunakan SVM
def display_results(df):
    # 3. Memisahkan fitur dan label
    X = df[['total_nilai_uts', 'total_nilai_uas', 'total_score']]  # Fitur
    y = df['layak_beasiswa'].map({'layak': 1, 'tidak layak': 0})  # Label (0: tidak layak, 1: layak)

    # Menyandikan data dengan StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 4. Membagi data menjadi data latih dan data uji
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # 5. Latih model SVM
    clf = svm.SVC(kernel='linear')  # Gunakan kernel linear
    clf.fit(X_train, y_train)

    # 6. Prediksi dengan model SVM
    y_pred = clf.predict(X_test)

    # 7. Tambahkan hasil prediksi ke dalam DataFrame
    df['prediksi_layak'] = clf.predict(X_scaled)  # Prediksi untuk semua data
    
    # Menampilkan hasil prediksi
    df['layak_beasiswa_prediksi'] = df['prediksi_layak'].map({1: 'layak', 0: 'tidak layak'})

    return df

# 3. Fungsi halaman laporan_hasil_prediksi
def laporan_hasil_prediksi(df):
    st.markdown('<h3 style="font-size: 25px;">👤 Kelayakan Beasiswa</h3>', unsafe_allow_html=True)
    st.markdown("""
        <style>
            .custom-title {
                font-size: 24px;
                font-weight: bold;
                color: #673AB7;
            }
            .custom-subtitle {
                font-size: 18px;
                font-weight: bold;
                color: #3F51B5;
            }
        </style>
    """, unsafe_allow_html=True)

    st.write(df[['nis', 'nama', 'kelas', 'total_nilai_uts', 'total_nilai_uas', 'total_score', 'total_uts_uas', 'total_skor_akhir', 'layak_beasiswa']])

    # Menentukan fitur dan target
    X = df[['total_nilai_uts', 'total_nilai_uas', 'total_score']]
    y = df['layak_beasiswa'].map({'layak': 1, 'tidak layak': 0})

    # Jika data hanya ada satu kelas, tampilkan error
    if len(y.unique()) == 1:
        st.error("Semua data berada dalam satu kelas. Pastikan ada perbedaan antara 'layak' dan 'tidak layak'.")
        return

    # Menampilkan siswa terbaik dari setiap kelas yang diinginkan
    st.markdown('<h3 style="font-size: 25px;">🏆 Laporan Hasil Prediksi</h3>', unsafe_allow_html=True)

    kelas_terpilih = ["X AK", "X MP", "X BC", "X TKJ", "X TKR", "XI AK", "XI MP", "XI BC", "XI TKJ", "XI TKR"]
    selected_students = pd.DataFrame()

    for kelas in kelas_terpilih:
        kelas_df = df[df['kelas'] == kelas]
        if not kelas_df.empty:
            top_student = kelas_df.nlargest(1, 'total_skor_akhir')  # Ambil 1 siswa terbaik di kelas
            selected_students = pd.concat([selected_students, top_student])

    # Menambahkan kolom Ranking (1-10)
    selected_students = selected_students.sort_values(by='total_skor_akhir', ascending=False)
    selected_students.insert(0, 'Ranking', range(1, len(selected_students) + 1))

    # Menampilkan hasil ranking siswa terbaik
    st.write(selected_students[['Ranking', 'nis', 'nama', 'kelas', 'total_skor_akhir', 'layak_beasiswa']])


    st.write("")
    
    # Menambahkan CSS untuk mempercantik pesan semangat
    st.markdown("""
    <style>
        .custom-message {
            font-size: 24px;
            font-weight: bold;
            color: #FF5733;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Menambahkan pesan semangat dengan ikon
    st.markdown('<div class="custom-message"><i class="fas fa-thumbs-up"></i> Tetap Semangat dan Tingkatkan Belajar Lagi! <i class="fas fa-smile"></i></div>', unsafe_allow_html=True)



def dashboard(df):
    # Mengubah ukuran font judul menggunakan markdown
    st.markdown("<h2 style='font-size: 24px;'>📊 Dashboard Siswa</h2>", unsafe_allow_html=True)

    st.write("""
    Selamat datang di halaman dashboard siswa. Di sini Anda bisa melihat hasil prediksi beasiswa yang dihitung berdasarkan data akademik dan non-akademik siswa.
    """)

    # Menampilkan informasi persyaratan beasiswa
    # Mengubah ukuran font subheader menggunakan markdown
    st.markdown("<h3 style='font-size: 16px;'>➡️ Persyaratan Beasiswa</h3>", unsafe_allow_html=True)
    st.markdown("""
    <ul class="custom-list">
        <li><b>Nilai Akademik:</b> Dipilih berdasarkan total nilai UTS dan UAS yang paling tinggi.</li>
        <li><b>Presensi:</b> Siswa tidak boleh memiliki alfa (ketidakhadiran tanpa keterangan sah).</li>
        <li><b>Nilai Non-Akademik:</b> Siswa harus memiliki nilai non-akademik minimal A dan B.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Grafik distribusi nilai
    st.markdown('<h5 style="font-size: 16px;">➡️ Distribusi Nilai UTS dan UAS</h5>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['total_nilai_uts'], kde=True, color='blue', label='UTS', ax=ax)
    sns.histplot(df['total_nilai_uas'], kde=True, color='green', label='UAS', ax=ax)
    ax.legend()
    st.pyplot(fig)

    # Grafik distribusi skor akhir
    st.markdown('<h5 style="font-size: 16px;">➡️ Distribusi Skor Akhir</h5>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df['total_skor_akhir'], kde=True, color='purple', label='Total Skor Akhir', ax=ax)
    ax.legend()
    st.pyplot(fig)


# 3. Fungsi utama untuk menjalankan Streamlit
def app():
    # Tambahkan CSS untuk mempercantik sidebar
    st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f7f7f7;
            border-radius: 10px;
            padding: 15px;
        }
        .sidebar .sidebar-content h1 {
            color: #673AB7;
            font-size: 24px;
            font-weight: bold;
        }
        .sidebar .sidebar-content select {
            font-size: 16px;
            padding: 10px;
            background-color: #673AB7;
            color: white;
            border-radius: 5px;
            border: none;
            width: 100%;
        }
        .sidebar .sidebar-content select:hover {
            background-color: #512DA8;
        }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar untuk memilih halaman menggunakan selectbox
    page = st.sidebar.selectbox(
        "Pilih Halaman", 
        ["Dashboard", "Laporan Hasil Prediksi", "Logout"],
        format_func=lambda x: f"🔎 {x}"  # Menambahkan ikon ke dalam pilihan
    )

    # Mengambil dan memproses data
    df = get_data()
    df = display_results(df)  # Pastikan prediksi ditambahkan ke DataFrame
    
    # Menampilkan halaman berdasarkan pilihan
    if page == "Dashboard":
        dashboard(df)
    elif page == "Laporan Hasil Prediksi":
        laporan_hasil_prediksi(df)
    if page == "Logout":
        st.session_state.clear()
        st.session_state["page"] = "login"
        st.success("Anda telah keluar!")    


if __name__ == "__main__":
    app()
