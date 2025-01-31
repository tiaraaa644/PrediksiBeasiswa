import pandas as pd
import numpy as np
import mysql.connector
import streamlit as st
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
import time
import random

# 1. Koneksi ke database dan ambil data
@st.cache_data
def get_data():
    try:
        # Membuka koneksi ke database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_prediksi_beasiswa"
        )

        # Menggunakan SQL JOIN untuk efisiensi
        query = """
        SELECT 
            s.nis, s.nama, s.kelas, 
            a.total_nilai_uts, a.total_nilai_uas, 
            n.total_score
        FROM data_siswa s
        JOIN data_akademik a ON s.nis = a.nis
        JOIN data_non_akademik n ON s.nis = n.nis
        """

        # Membaca data langsung dari query
        df = pd.read_sql_query(query, connection)

        # Menghitung total nilai
        df['total_uts_uas'] = df['total_nilai_uts'] + df['total_nilai_uas']
        df['total_skor_akhir'] = df['total_uts_uas'] + df['total_score']

        # Menentukan kelayakan beasiswa
        threshold = 1900
        df['layak_beasiswa'] = df['total_skor_akhir'].apply(lambda x: 'layak' if x > threshold else 'tidak layak')

        return df

    except mysql.connector.Error as e:
        print(f"Error dalam koneksi database: {e}")
        conn = None

    finally:
        if 'connection' in locals():
            connection.close()



def update_student_data(nis, nama, kelas, total_nilai_uts, total_nilai_uas, total_score):
    try:
        # Membuka koneksi ke database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_prediksi_beasiswa"
        )

        # SQL untuk memperbarui data siswa
        update_query = """
        UPDATE data_siswa
        SET nama = %s, kelas = %s
        WHERE nis = %s
        """
        update_akademik_query = """
        UPDATE data_akademik
        SET total_nilai_uts = %s, total_nilai_uas = %s
        WHERE nis = %s
        """
        update_non_akademik_query = """
        UPDATE data_non_akademik
        SET total_score = %s
        WHERE nis = %s
        """
        
        # Eksekusi query update data siswa
        with connection.cursor() as cursor:
            cursor.execute(update_query, (nama, kelas, nis))
            cursor.execute(update_akademik_query, (total_nilai_uts, total_nilai_uas, nis))
            cursor.execute(update_non_akademik_query, (total_score, nis))
            connection.commit()

        st.success("Data siswa berhasil diperbarui!")
        
    except mysql.connector.Error as e:
        st.error(f"Error dalam memperbarui data: {e}")
    finally:
     if 'connection' in locals() and connection.is_connected():
        connection.close()

    # Clear cache dan refresh data
    st.cache_data.clear()  # Clear the cache
    st.rerun()  # Rerun the app to load updated data

# Fungsi untuk menampilkan form input dan memperbarui data siswa
def update_student_form():
    st.markdown('<div class="custom-title">✍ Update Data Siswa</div>', unsafe_allow_html=True)

    # Input NIS siswa untuk mencari data
    nis = st.text_input("Masukkan NIS Siswa", "")

    if nis:  # Hanya menampilkan form setelah NIS dimasukkan
        # Mencari data siswa berdasarkan NIS
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_prediksi_beasiswa"
        )

        query = """
        SELECT s.nama, s.kelas, a.total_nilai_uts, a.total_nilai_uas, n.total_score
        FROM data_siswa s
        JOIN data_akademik a ON s.nis = a.nis
        JOIN data_non_akademik n ON s.nis = n.nis
        WHERE s.nis = %s
        """
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, (nis,))
                result = cursor.fetchone()

            if result:
                nama, kelas, total_nilai_uts, total_nilai_uas, total_score = result

                # Form input untuk mengupdate data siswa
                nama = st.text_input("Nama Siswa", nama)
                kelas_options = ['X MP', 'X AK', 'X BC', 'X TKJ', 'X TKR', 'XI MP', 'XI AK', 'XI BC', 'XI TKJ', 'XI TKR']
                kelas = st.selectbox("Kelas", kelas_options, index=kelas_options.index(kelas))
                total_nilai_uts = st.number_input("Total Nilai UTS", min_value=0, max_value=1000, value=int(total_nilai_uts))
                total_nilai_uas = st.number_input("Total Nilai UAS", min_value=0, max_value=1000, value=int(total_nilai_uas))
                total_score = st.number_input("Total Nilai Non-Akademik", min_value=0, max_value=1000, value=int(total_score))

                if st.button("Perbarui Data Siswa"):
                    if nama:
                        update_student_data(nis, nama, kelas, total_nilai_uts, total_nilai_uas, total_score)
                    else:
                        st.error("Mohon lengkapi semua data!")
            else:
                st.error("Data siswa tidak ditemukan!")

        except mysql.connector.Error as e:
            st.error(f"Error dalam mengambil data: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

# 2. Menampilkan data dan hasil seleksi menggunakan SVM dan Naïve Bayes
def display_results(df):
    st.markdown("""
        <style>
            .custom-title {
                font-size: 21px;
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

    # Normalisasi fitur (hanya dilakukan sekali)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Membuat dan melatih model SVM (gunakan X_scaled, y)
    svm_model = SVC(probability=True, kernel='rbf', C=1, gamma=0.1, random_state=42)
    svm_model.fit(X_scaled, y)

    # Membuat dan melatih model Naïve Bayes
    nb_model = GaussianNB()
    nb_model.fit(X_scaled, y)

    # Prediksi awal (digunakan nanti setelah tombol diklik)
    nb_predictions = nb_model.predict(X_scaled)

    # Tombol Mulai Prediksi
    if st.button('Mulai Prediksi', key="mulai_prediksi_svm"):
        # Prediksi menggunakan SVM
        y_pred = svm_model.predict(X_scaled)

        # Menambahkan hasil prediksi ke dataframe
        df['prediksi_layak'] = y_pred
        df['layak_beasiswa_prediksi'] = df['prediksi_layak'].map({1: 'layak', 0: 'tidak layak'})

        # Menambahkan hasil prediksi Naïve Bayes ke dataframe
        df['prediksi_nb'] = nb_predictions
        df['layak_beasiswa_nb'] = df['prediksi_nb'].map({1: 'layak', 0: 'tidak layak'})

        # Menampilkan siswa yang layak berdasarkan prediksi SVM
        st.markdown('<div class="custom-title">🎓 Siswa Layak Berdasarkan Prediksi SVM</div>', unsafe_allow_html=True)
        students_svm = df[df['layak_beasiswa_prediksi'] == 'layak']
        st.write(students_svm[['nis', 'nama', 'kelas', 'total_skor_akhir', 'layak_beasiswa_prediksi']])

        # Menampilkan siswa yang layak berdasarkan prediksi Naïve Bayes
        st.markdown('<div class="custom-title">🎓 Siswa Layak Berdasarkan Prediksi Naïve Bayes</div>', unsafe_allow_html=True)
        students_nb = df[df['layak_beasiswa_nb'] == 'layak']
        st.write(students_nb[['nis', 'nama', 'kelas', 'total_skor_akhir', 'layak_beasiswa_nb']])

        # Menampilkan 10 siswa terpilih berdasarkan gabungan SVM dan Naïve Bayes per kelas
        st.markdown('<div class="custom-title">🎓 10 Siswa Terpilih Berdasarkan Gabungan SVM dan Naïve Bayes Per Kelas</div>', unsafe_allow_html=True)

        kelas_terpilih = ['X MP', 'X AK', 'X BC', 'X TKJ', 'X TKR', 
                          'XI MP', 'XI AK', 'XI BC', 'XI TKJ', 'XI TKR']

        siswa_terpilih_per_kelas = []

        # Loop untuk memilih siswa terbaik dari setiap kelas
        for kelas in kelas_terpilih:
            siswa_kelas = df[(df['kelas'] == kelas) & (df['prediksi_layak'] == 1) & (df['prediksi_nb'] == 1)]
            if not siswa_kelas.empty:
                siswa_terpilih_per_kelas.append(siswa_kelas.nlargest(1, 'total_skor_akhir'))

        # Gabungkan semua siswa terpilih
        if siswa_terpilih_per_kelas:
            siswa_terpilih_final = pd.concat(siswa_terpilih_per_kelas)

            # Urutkan siswa berdasarkan 'total_skor_akhir' dari yang tertinggi
            siswa_terpilih_final = siswa_terpilih_final.sort_values(by='total_skor_akhir', ascending=False)

            # Tambahkan kolom ranking
            siswa_terpilih_final['ranking'] = range(1, len(siswa_terpilih_final) + 1)

            # Tampilkan hasilnya
            st.write(siswa_terpilih_final[['nis', 'nama', 'kelas', 'total_skor_akhir', 'ranking']])
        else:
            st.write("Tidak ada siswa yang memenuhi kriteria dari kedua model.")

        # Evaluasi model
        display_evaluation(df, X_scaled, y, svm_model, nb_model)


# 2. Menambahkan evaluasi untuk SVM dan Naïve Bayes
def display_evaluation(df, X_test, y_test, svm_model, nb_model):
    # Prediksi menggunakan SVM
    y_pred_svm = svm_model.predict(X_test)
    
    # Prediksi menggunakan Naïve Bayes
    y_pred_nb = nb_model.predict(X_test)

    # Menghitung evaluasi untuk SVM
    accuracy_svm = accuracy_score(y_test, y_pred_svm)
    precision_svm = precision_score(y_test, y_pred_svm)
    recall_svm = recall_score(y_test, y_pred_svm)
    f1_svm = f1_score(y_test, y_pred_svm)
    cm_svm = confusion_matrix(y_test, y_pred_svm)

    # Menghitung evaluasi untuk Naïve Bayes
    accuracy_nb = accuracy_score(y_test, y_pred_nb)
    precision_nb = precision_score(y_test, y_pred_nb)
    recall_nb = recall_score(y_test, y_pred_nb)
    f1_nb = f1_score(y_test, y_pred_nb)
    cm_nb = confusion_matrix(y_test, y_pred_nb)

    # Menampilkan evaluasi model
    st.markdown('<div class="custom-title">🎓 Evaluasi Model SVM</div>', unsafe_allow_html=True)
    st.write(f"📈 Accuracy SVM: {accuracy_svm:.2f}")
    st.write(f"🎯 Precision SVM: {precision_svm:.2f}")
    st.write(f"🔍 Recall SVM: {recall_svm:.2f}")
    st.write(f"✨ F1 Score SVM: {f1_svm:.2f}")
    st.write("Confusion Matrix SVM:")
    fig_svm, ax_svm = plt.subplots(figsize=(6, 4))
    sns.heatmap(cm_svm, annot=True, fmt="d", cmap="Blues", ax=ax_svm)
    ax_svm.set_xlabel('Prediksi')
    ax_svm.set_ylabel('Aktual')
    st.pyplot(fig_svm)

    st.markdown('<div class="custom-title">🎓 Evaluasi Model Naïve Bayes</div>', unsafe_allow_html=True)
    st.write(f"📈 Accuracy Naïve Bayes: {accuracy_nb:.2f}")
    st.write(f"🎯 Precision Naïve Bayes: {precision_nb:.2f}")
    st.write(f"🔍 Recall Naïve Bayes: {recall_nb:.2f}")
    st.write(f"✨ F1 Score Naïve Bayes: {f1_nb:.2f}")
    st.write("Confusion Matrix Naïve Bayes:")
    fig_nb, ax_nb = plt.subplots(figsize=(6, 4))
    sns.heatmap(cm_nb, annot=True, fmt="d", cmap="Blues", ax=ax_nb)
    ax_nb.set_xlabel('Prediksi')
    ax_nb.set_ylabel('Aktual')
    st.pyplot(fig_nb)

# Gabungkan total nilai UTS dan UAS menjadi satu fitur
    df['total_uts_uas'] = df['total_nilai_uts'] + df['total_nilai_uas']

        # Pilih dua fitur utama: total_uts_uas dan total_score
    X = df[['total_uts_uas', 'total_score']]
    y = df['layak_beasiswa'].map({'layak': 1, 'tidak layak': 0})

    # Latih model SVM dengan dua fitur
    svc = SVC(kernel='linear')
    svc.fit(X, y)

    # Visualisasikan scatter plot dengan hyperplane
    st.markdown('<div class="custom-title">📊 Scatter Plot dengan Hyperplane SVM</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
    data=df, 
    x='total_uts_uas', 
    y='total_score', 
    hue='layak_beasiswa', 
    palette={'layak': 'green', 'tidak layak': 'red'},
    style='layak_beasiswa',
    ax=ax
    )
    plt.title('Scatter Plot Total UTS + UAS vs Total Score dengan Hyperplane SVM')
    plt.xlabel('Total Nilai UTS + UAS')
    plt.ylabel('Total Score')

    # Tambahkan hyperplane
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = svc.decision_function(xy).reshape(XX.shape)
    ax.contour(XX, YY, Z, colors='k', levels=[0], linestyles=['-'])

    st.pyplot(fig)



# 3. Fungsi utama untuk menjalankan Streamlit
def app():
    st.markdown('<div class="custom-title">🎓 Prediksi Beasiswa</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-subtitle">Data Siswa dan Hasil Perhitungan</div>', unsafe_allow_html=True)
    
    df = get_data()
    display_results(df)
    # Menampilkan form update data siswa
    update_student_form()



if __name__ == "__main__":
    app()
