import pandas as pd
import mysql.connector
import streamlit as st
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Koneksi ke database dan ambil data
def get_data():
    # Koneksi ke database MySQL
    connection = mysql.connector.connect(
            host="localhost",        
            user="root",              
            password="",             
            database="db_prediksi_beasiswa" 
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
    threshold = 1890
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

def laporan_hasil_prediksi(df):
    # Daftar kelas yang dipilih
    selected_classes = ['X MP', 'X AK', 'X BC', 'X TKJ', 'X TKR', 'XI MP', 'XI AK', 'XI BC', 'XI TKJ', 'XI TKR']
    
    # Filter hanya siswa dari kelas yang dipilih
    df_filtered = df[df['kelas'].isin(selected_classes)]
    
    # Ambil 1 siswa terbaik dari setiap kelas
    top_per_class = []
    for kelas in selected_classes:
        kelas_df = df_filtered[df_filtered['kelas'] == kelas]
        if not kelas_df.empty:  # Cek apakah ada siswa di kelas ini
            top_per_class.append(kelas_df.nlargest(1, 'total_skor_akhir'))  # Ambil 1 terbaik per kelas
    
    # Gabungkan semua siswa terbaik dari tiap kelas
    df_top = pd.concat(top_per_class)

    # Urutkan lagi berdasarkan skor tertinggi, lalu ambil hanya 10 siswa terbaik
    df_top10 = df_top.sort_values(by='total_skor_akhir', ascending=False).head(10)

    # Tambahkan kolom ranking
    df_top10['ranking'] = range(1, len(df_top10) + 1)

    # Tampilkan hasil
    st.write(df_top10[['nis', 'nama', 'kelas', 'total_skor_akhir', 'layak_beasiswa_prediksi', 'ranking']])

# 3. Fungsi utama untuk menjalankan Streamlit
def app():
    # Tambahkan CSS untuk mempercantik font dan ikon
    st.markdown("""
        <style>
            .custom-title {
                font-size: 24px;
                font-weight: bold;
                display: flex;
                align-items: center;
                gap: 10px;
                color: #673AB7;
            }
            .custom-subtitle {
                font-size: 18px;
                font-weight: bold;
                display: flex;
                align-items: center;
                gap: 8px;
                color: #3F51B5;
            }
            .custom-icon {
                font-size: 20px;
                margin-right: 8px;
            }
            label {
                font-size: 14px !important; /* Perkecil font input */
            }
            input, select, textarea {
                font-size: 14px !important; /* Perkecil font di kolom input */
            }
            button {
                font-size: 14px !important; /* Perkecil font di tombol */
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="custom-title"><span class="custom-icon">🎓</span> Laporan Hasil Prediksi</div>', unsafe_allow_html=True)
    # Deskripsi atau informasi tambahan
    st.markdown("""
    <div class="custom-description">
        Selamat datang di halaman laporan hasil prediksi kelayakan beasiswa. Berdasarkan data akademik dan non-akademik siswa yang telah diolah menggunakan algoritma <b>Naive Bayes</b> dan <b>Support Vector Machine (SVM)</b>, berikut adalah daftar siswa yang terpilih untuk menerima rekomendasi beasiswa.
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    # Mengambil dan memproses data
    df = get_data()
    st.markdown('<div class="custom-subtitle"><span class="custom-icon">📊</span>10 Siswa Terpilih Penerima Beasiswa</div>', unsafe_allow_html=True)  
    # Menampilkan data siswa dan hasil seleksi menggunakan SVM
    df = display_results(df)  # Pastikan prediksi ditambahkan ke DataFrame
    
    # Menampilkan hasil prediksi
    laporan_hasil_prediksi(df)

if __name__ == "__main__":
    app()
