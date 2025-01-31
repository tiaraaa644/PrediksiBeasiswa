import streamlit as st
import mysql.connector
import os
import pandas as pd
from io import BytesIO
import time
import base64
from base64 import b64encode
from laporan_hasil_prediksi import app as laporan_hasil_prediksi_app
import matplotlib.pyplot as plt
import logging


# Fungsi untuk membuat koneksi ke database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=st.secrets["DB_HOST"],
            database=st.secrets["DB_DATABASE"],
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"]
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None
    
def get_file_download_link(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
        b64 = base64.b64encode(file_data).decode()  # encoding file ke base64
        return f"data:application/octet-stream;base64,{b64}"


# Fungsi untuk mendapatkan data guru berdasarkan nama
def get_teacher_class_by_name(teacher_name):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (teacher_name,))
        user = cursor.fetchone()
        connection.close()
        return user
    return None

# Fungsi untuk mengambil data guru berdasarkan nama
def get_teacher_class_by_name(teacher_name):
    # Cek data guru yang sesuai dengan nama dari session state
    if teacher_name == st.session_state["user"]['username']:
        return st.session_state["user"]  # Mengembalikan data guru yang ditemukan
    return None


# Fungsi untuk memuat data siswa sesuai kelas yang diampu
def load_student_data(class_name):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM data_siswa WHERE kelas = %s"
        cursor.execute(query, (class_name,))
        data = cursor.fetchall()
        connection.close()
        return data
    return []

# Fungsi untuk memuat data akademik siswa sesuai kelas yang diampu
def load_academic_data(class_name):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM data_akademik WHERE kelas = %s"
        cursor.execute(query, (class_name,))
        data = cursor.fetchall()
        connection.close()
        return data
    return []

# Fungsi untuk memuat data non-akademik siswa sesuai kelas yang diampu
def load_non_academic_data(class_name):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM data_non_akademik WHERE kelas = %s"
        cursor.execute(query, (class_name,))
        data = cursor.fetchall()
        connection.close()
        return data
    return []

# Fungsi untuk manajemen data siswa sesuai kelas yang diampu
def manage_student_data(user):
    st.subheader("Manajemen Data Siswa")
    class_name = user['kelas_tertuju']
    tab1, tab2, tab3 = st.tabs(["Data Siswa", "Data Akademik", "Data Non-Akademik"])

    # Tab Data Siswa
    with tab1:
        data_siswa = load_student_data(class_name)
        if data_siswa:
            st.table(data_siswa)
        else:
            st.write("Tidak ada data siswa untuk kelas ini.")

    # Tab Data Akademik
    with tab2:
        data_akademik = load_academic_data(class_name)
        if data_akademik:
            st.table(data_akademik)
        else:
            st.write("Tidak ada data akademik untuk kelas ini.")

    # Tab Data Non-Akademik
    with tab3:
        data_non_akademik = load_non_academic_data(class_name)
        if data_non_akademik:
            st.table(data_non_akademik)
        else:
            st.write("Tidak ada data non-akademik untuk kelas ini.")


def display_results(data):
    # CSS untuk memperkecil font dan mempercantik tampilan
    st.markdown("""
        <style>
            .custom-title {
                font-size: 24px;
                font-weight: bold;
                display: flex;
                align-items: center;
                gap: 10px;
                color: #4CAF50;
            }
            .custom-subtitle {
                font-size: 18px;
                font-weight: bold;
                display: flex;
                align-items: center;
                gap: 8px;
                color: #2196F3;
            }
            .custom-icon {
                font-size: 20px;
                margin-right: 8px;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📋Tampil Data Siswa</div>', unsafe_allow_html=True)
    if data:
        try:
            # Konversi data menjadi DataFrame untuk tampilan rapi
            df = pd.DataFrame(data)
            # Pastikan urutan kolom sesuai kebutuhan
            if not df.empty:
                df = df[['nis', 'nama', 'jenis_kelamin', 'kelas']]
                df.columns = ["NIS", "Nama", "Jenis Kelamin", "Kelas"]
            # Tampilkan tabel scrollable tanpa indeks
            st.dataframe(df.style.hide(axis="index"), height=400)
        except Exception as e:
            st.error(f"Terjadi kesalahan saat menampilkan data: {e}")
    else:
        st.warning("Tidak ada data yang tersedia.")

# Fungsi untuk input data siswa
def input_student_data(class_name):
    # Judul dengan ikon
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>👥Data Siswa</div>', unsafe_allow_html=True)
    
    # Subjudul dengan ikon
    st.markdown('<div class="custom-subtitle"><span class="custom-icon"></span> ➕Tambah Data Siswa</div>', unsafe_allow_html=True)
    
    # Form input data siswa
    with st.form(key="student_form"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            nis = st.text_input("NIS")
        with col2:
            nama = st.text_input("Nama")
        with col3:       
            jenis_kelamin = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
        with col4:
            kelas = st.selectbox("Kelas", ["X TKR", "X TKJ", "X MP","X AK", "XI BC", "XI TKR", "XI TKJ", "XI MP","XI AK", "XI BC",])
        
        submit_button = st.form_submit_button("Simpan")
    

        if submit_button:
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                query = """INSERT INTO data_siswa (nis, nama, jenis_kelamin, kelas) 
                           VALUES (%s, %s, %s, %s)"""
                cursor.execute(query, (nis, nama, jenis_kelamin, kelas))
                connection.commit()
                connection.close()
                st.success("Data siswa berhasil disimpan!")
                st.rerun()  # Refresh halaman setelah data disimpan

                # Menampilkan data siswa setelah form input
    data_siswa = load_student_data(class_name)
    display_results(data_siswa)  # Menampilkan data siswa dengan tampilan yang rapi


# Fungsi untuk input data akademik siswa
def input_academic_data(class_name):
    # Judul dengan ikon
   # Judul dengan ikon dan teks bold
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📚 <b>Data Akademik</b></div>', unsafe_allow_html=True)

# Subjudul dengan ikon dan teks bold
    st.markdown('<div class="custom-subtitle"><span class="custom-icon"></span> ➕ <b>Tambah Data Akademik</b></div>', unsafe_allow_html=True)

    with st.form(key="academic_data_form"):
        # Membuat dua kolom untuk input data
        col1, col2 = st.columns(2)
        
        with col1:
            nis = st.text_input("NIS")
            nama = st.text_input("Nama")
            kelas = st.text_input("Kelas")
        
        with col2:
            total_nilai_uts = st.number_input("Total Nilai (UTS)", min_value=0)
            total_nilai_uas = st.number_input("Total Nilai (UAS)", min_value=0)
            semester = st.selectbox("Semester", 
                                    ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"])
        
        # File uploader untuk rapor
        unggah_rapor_1 = st.file_uploader("Unggah Rapor 1 (PDF)", type=["pdf"], key="rapor_1")
        unggah_rapor_2 = st.file_uploader("Unggah Rapor 2 (PDF)", type=["pdf"], key="rapor_2")

        submit_button = st.form_submit_button("Simpan Data Akademik")

    # Proses submit form
    if submit_button:
        if not unggah_rapor_1 or not unggah_rapor_2:
            st.error("Harap unggah kedua file rapor!")
        else:
            try:
                os.makedirs("uploads", exist_ok=True)

                # Simpan file rapor ke folder uploads
                rapor_1_name = unggah_rapor_1.name
                rapor_2_name = unggah_rapor_2.name

                with open(f"uploads/{rapor_1_name}", "wb") as f:
                    f.write(unggah_rapor_1.getbuffer())
                with open(f"uploads/{rapor_2_name}", "wb") as f:
                    f.write(unggah_rapor_2.getbuffer())

                st.success(f"File berhasil disimpan: {rapor_1_name}, {rapor_2_name}")

                # Simpan data ke database
                connection = create_connection()
                if connection:
                    try:
                        cursor = connection.cursor()
                        query = """INSERT INTO data_akademik 
                                (nis, nama, kelas, total_nilai_uts, total_nilai_uas, semester, unggah_rapor_1, unggah_rapor_2)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                        cursor.execute(query, (nis, nama, kelas, total_nilai_uts, total_nilai_uas, semester, rapor_1_name, rapor_2_name))
                        connection.commit()
                        st.success("Data akademik berhasil disimpan!")
                    except Exception as db_err:
                        st.error(f"Kesalahan saat menyimpan data ke database: {db_err}")
                    finally:
                        cursor.close()
                        connection.close()
            except Exception as e:
                st.error(f"Kesalahan saat menyimpan file: {e}")

# Menampilkan data akademik sesuai dengan kelas yang diampu
    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    # Menampilkan data akademik
    st.markdown('<div class="custom-title"><span class="custom-icon"></span><b>📋Tampil Data Akademik</b></div>', unsafe_allow_html=True)
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Mengambil kelas yang diampu oleh guru yang login
            teacher_class = st.session_state["user"]['kelas_tertuju']
            # Menyesuaikan query untuk hanya mengambil data dari kelas yang relevan
            query = f"SELECT nis, nama, kelas, total_nilai_uts, total_nilai_uas, semester, unggah_rapor_1, unggah_rapor_2 FROM data_akademik WHERE kelas = %s"
            cursor.execute(query, (teacher_class,))
            rows = cursor.fetchall()
            cursor.close()

            if rows:
                # Membuat list untuk data
                data = []
                for row in rows:
                    nis, nama, kelas, uts, uas, semester, rapor_1, rapor_2 = row

                    # Menyiapkan link download untuk rapor
                    rapor_1_link = ""
                    rapor_2_link = ""
                    if rapor_1 and os.path.exists(f"uploads/{rapor_1}"):
                        with open(f"uploads/{rapor_1}", "rb") as f:
                            rapor_1_link = f'<a href="data:application/pdf;base64,{base64.b64encode(f.read()).decode()}" download="{rapor_1}">Unduh Rapor 1</a>'

                    if rapor_2 and os.path.exists(f"uploads/{rapor_2}"):
                        with open(f"uploads/{rapor_2}", "rb") as f:
                            rapor_2_link = f'<a href="data:application/pdf;base64,{base64.b64encode(f.read()).decode()}" download="{rapor_2}">Unduh Rapor 2</a>'

                    # Menambahkan data ke list
                    data.append([nis, nama, kelas, uts, uas, semester, rapor_1_link, rapor_2_link])

                # Membuat DataFrame
                df = pd.DataFrame(data, columns=["NIS", "Nama", "Kelas", "Total Nilai UTS", "Total Nilai UAS", "Semester", "Rapor 1", "Rapor 2"])
                # Styling dan render tabel dengan Streamlit
                st.markdown(
                    """
                    <style>
                    .dataframe-container {
                        overflow-y: auto;
                        max-height: 500px;
                        border: 1px solid #ddd;
                        padding: 15px;
                        color : #333;
                        width : 100%;
                        border-radius : 4px;
                        background-color : #f8f8f8;
                        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1)

                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        font-family: 'Arial', sans-serif;
                        background-color: #fff;
                    }
                    th {
                        position: sticky;
                        top:0;
                        background-color: #444;
                        color : white;
                        font-size: 16px;
                        padding: 12px;
                        text-align: left;
                        z-index: 1;
                    }
                    th, td {
                        padding: 10px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                        font-size: 14px;
                    }
                     tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                    td {
                        color: #555;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="dataframe-container">{df.to_html(escape=False, index=False)}</div>',
                    unsafe_allow_html=True,
                )

            else:
                st.warning("Tidak ada data akademik yang tersedia untuk kelas ini.")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengambil data: {e}")
        finally:
            connection.close()
    else:
        st.error("Gagal membuat koneksi ke database.")



# Fungsi untuk menghitung nilai berdasarkan bobot
def calculate_score(alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas):
    # Penalti Alfa
    alfa_uts_score = max(0, 3 - (alfa_uts * 0.1))
    alfa_uas_score = max(0, 3 - (alfa_uas * 0.1))

    # Rata-rata Alfa
    rata_rata_alfa = (alfa_uts_score + alfa_uas_score) / 2

    # Rata-rata Ekstrakurikuler dan Kepribadian
    rata_rata_ekstrakurikuler = (ekstrakurikuler_uts + ekstrakurikuler_uas) / 2
    rata_rata_kepribadian = (kepribadian_uts + kepribadian_uas) / 2

    # Menghitung skor total berdasarkan bobot
    skor_alfa = rata_rata_alfa * 0.5
    skor_ekstrakurikuler = rata_rata_ekstrakurikuler * 0.3
    skor_kepribadian = rata_rata_kepribadian * 0.2

    skor_total = skor_alfa + skor_ekstrakurikuler + skor_kepribadian
    return skor_total

# Fungsi untuk mengonversi file gambar menjadi base64
def get_base64_encoded_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} tidak ditemukan.")
    with open(file_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode("utf-8")
    return encoded

def calculate_certificate_score(tipe, tingkat=None, sifat=None, juara=None):
    scores = {
        "Kedinasan": {
            "Internasional": {"berjenjang": [100, 97, 94], "tidak berjenjang": [92, 89, 86]},
            "Nasional": {"berjenjang": [91, 88, 85], "tidak berjenjang": [83, 80, 77]},
            "Provinsi": {"berjenjang": [82, 79, 76], "tidak berjenjang": [74, 71, 68]},
            "Kota/Kab": {"berjenjang": [73, 70, 67], "tidak berjenjang": [65, 62, 59]}
        },
        "Organisasi": {
            "Internasional": {"berjenjang": [92, 89, 86], "tidak berjenjang": [84, 81, 78]},
            "Nasional": {"berjenjang": [83, 80, 77], "tidak berjenjang": [75, 72, 69]},
            "Provinsi": {"berjenjang": [74, 71, 68], "tidak berjenjang": [66, 63, 60]},
            "Kota/Kab": {"berjenjang": [65, 61, 59], "tidak berjenjang": [57, 54, 51]}
        },
        "Jambore": {
            "Internasional": 100,
            "Nasional": 67,
            "Provinsi": 43,
            "Kota/Kab": 33
        },
        "Tidak Ada Sertifikat": 0
    }

    # Logika untuk menghitung skor berdasarkan tipe sertifikat
    if tipe == "Tidak Ada Sertifikat":
        return 0
    elif tipe == "Jambore":
        return scores[tipe].get(tingkat, 0)
    else:
        return scores[tipe][tingkat][sifat][juara - 1]

# Fungsi untuk menghitung skor non-akademik berdasarkan nilai UTS dan UAS
def calculate_non_academic_score(value_uts, value_uas):
    value_mapping = {3: 95, 2: 80, 1: 70}
    skor_uts = value_mapping.get(value_uts, 0)
    skor_uas = value_mapping.get(value_uas, 0)
    avg_value = (skor_uts + skor_uas) / 2
    return avg_value

# Fungsi untuk menghitung skor gabungan dan memberikan bobot
def calculate_weighted_score(skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian):
    return (
        (skor_alfa * 0.40) +
        (skor_sertifikat * 0.30) +
        (skor_ekstrakurikuler * 0.15) +
        (skor_kepribadian * 0.15)
    )

# Fungsi untuk input data non-akademik siswa
def input_non_academic_data(class_name):
    semester_list = ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"]

    # Menampilkan form input data non-akademik
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # Judul utama dengan ikon
    # Styling dan rendecr tabel dengan Streamlit

   # Judul dengan ikon dan teks bold
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📚 <b>Data Non-Akademik</b></div>', unsafe_allow_html=True)
    st.write("")
    # Judul utama dengan ikon untuk Tabel Skala Nilai
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📊<b>Skala Nilai Ekstrakurikuler dan Alfa</b></div>', unsafe_allow_html=True)
    # Penjelasan tambahan
    st.markdown("""
    Tabel ini menunjukkan skala nilai yang digunakan untuk mengkonversi nilai kualitatif dari aspek ekstrakurikuler dan alfa menjadi nilai skala kuantitatif. 
    Skala ini digunakan dalam proses perhitungan dan prediksi untuk menentukan kelayakan penerima beasiswa.
    """)
    # Data untuk tabel skala nilai
    data = {
    'Kategori': ['A (Sangat Baik)', 'B (Baik)', 'C (Cukup)'],
    'Nilai Skala': [3, 2, 1]
    }

    # Membuat DataFrame
    df = pd.DataFrame(data)

    # Fungsi untuk memberikan style warna pada kolom 'Nilai Skala'
    def highlight_values(val):
        color = '#a6e22e' if val == 3 else '#f7dc6f' if val == 2 else '#e74c3c'
        return f'background-color: {color}'

    # Menerapkan style pada DataFrame
    styled_df = df.style.applymap(highlight_values, subset=['Nilai Skala'])

    # Menampilkan tabel dengan warna
    st.dataframe(styled_df)

    # Subjudul dengan ikon dan teks bold
    st.markdown('<div class="custom-subtitle"><span class="custom-icon"></span> ➕ <b>Tambah Data Non-Akademik</b></div>', unsafe_allow_html=True)
    semester_list = ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"]

    with st.form(key="non_academic_form"):
        # Input dasar
        col1, col2, col3 = st.columns(3)
        with col1:
            nis = st.text_input("NIS")
        with col2:
            nama = st.text_input("Nama")
        with col3:
            kelas = st.text_input("Kelas")

        semester_update = st.selectbox("Semester", semester_list)

        st.markdown("**Presensi**")
        col4, col5 = st.columns(2)
        with col4:
            alfa_uts = st.number_input("Alfa (UTS)", min_value=0, value=0, step=1)
        with col5:
            alfa_uas = st.number_input("Alfa (UAS)", min_value=0, value=0, step=1)

        st.markdown("**Ekstrakurikuler**")
        col6, col7 = st.columns(2)
        with col6:
            ekstrakurikuler_uts = st.number_input("Ekstrakurikuler (UTS)", min_value=0, value=0, step=1)
        with col7:
            ekstrakurikuler_uas = st.number_input("Ekstrakurikuler (UAS)", min_value=0, value=0, step=1)

        st.markdown("**Kepribadian**")
        col8, col9 = st.columns(2)
        with col8:
            kepribadian_uts = st.number_input("Kepribadian (UTS)", min_value=0, value=0, step=1)
        with col9:
            kepribadian_uas = st.number_input("Kepribadian (UAS)", min_value=0, value=0, step=1)

        # Input Sertifikat (opsional)
        st.markdown("**Sertifikat**")
        sertifikat_tipe = st.selectbox("Tipe Sertifikat (Opsional)", ["Kedinasan", "Organisasi", "Jambore", "Tidak Ada Sertifikat"])
        sertifikat_tingkat = st.selectbox("Tingkat Sertifikat", ["Internasional", "Nasional", "Provinsi", "Kota/Kab"]) if sertifikat_tipe != "Tidak Ada Sertifikat" else None
        sertifikat_berjenjang = None
        if sertifikat_tipe not in ["Jambore", "Tidak Ada Sertifikat"]:
            sertifikat_berjenjang = st.selectbox("Berjenjang atau Tidak", ["berjenjang", "tidak berjenjang"])
        sertifikat_juara = st.selectbox("Juara Sertifikat", [1, 2, 3]) if sertifikat_tipe != "Tidak Ada Sertifikat" else None

        uploaded_file = st.file_uploader("Unggah Sertifikat (Opsional)", type=["jpg", "jpeg", "png"])

        # Tombol Simpan
        submit_button = st.form_submit_button("Simpan Data Non-Akademik")

    st.markdown('</div>', unsafe_allow_html=True)

    # Validasi dan Simpan Data
    if submit_button:
        if not (nis and nama and kelas):
            st.error("NIS, Nama, dan Kelas wajib diisi!")
        else:
            try:
                # Perhitungan Skor Sertifikat (jika ada sertifikat)
                skor_sertifikat = 0 if sertifikat_tipe == "Tidak Ada Sertifikat" else calculate_certificate_score(
                    tipe=sertifikat_tipe,
                    tingkat=sertifikat_tingkat,
                    sifat=sertifikat_berjenjang,
                    juara=sertifikat_juara
                )

                # Gabungkan nilai Alfa (UTS dan UAS) menjadi skor_alfa
                gabungan_alfa = (alfa_uts + alfa_uas)
                skor_alfa = 5 if gabungan_alfa == 0 else 3 if gabungan_alfa <= 3 else 0

                # Gabungkan nilai Ekstrakurikuler (UTS dan UAS) menjadi skor_ekstrakurikuler
                skor_ekstrakurikuler = calculate_non_academic_score(ekstrakurikuler_uts, ekstrakurikuler_uas)

                # Gabungkan nilai Kepribadian (UTS dan UAS) menjadi skor_kepribadian
                skor_kepribadian = calculate_non_academic_score(kepribadian_uts, kepribadian_uas)

                # Hitung total skor dengan bobot
                total_score = calculate_weighted_score(skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian)

                # Simpan ke database
                connection = create_connection()
                if connection:
                    try:
                        cursor = connection.cursor()
                        query = """INSERT INTO data_non_akademik (nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, unggah_sertifikat, skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        cursor.execute(query, (nis, nama, kelas, semester_update, alfa_uts, alfa_uas, ekstrakurikuler_uts, 
                                           ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, uploaded_file.name if uploaded_file else None, 
                                           skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score))
                        connection.commit()
                        st.success("Data non-akademik berhasil disimpan!")
                    except Exception as e:
                        st.error("Kesalahan saat menyimpan data ke database")
                    finally:
                        cursor.close()
                        connection.close()
            except Exception as e:
                st.error(f"kesalahan saat menyipmpan file: {e}")
                    


    # Menampilkan Data Non-Akademik untuk kelas yang relevan
    st.text("")  # Menambah baris kosong
    st.markdown('<div class="custom-title"><span class="custom-icon"></span><b>📋Tampil Data Non-Akademik</b></div>', unsafe_allow_html=True)
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Mendapatkan kelas yang diampu oleh guru dari session state
            teacher_class = st.session_state["user"]['kelas_tertuju']
            # Query hanya mengambil data non-akademik untuk kelas yang relevan
            query = (
                f"SELECT nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts,"
                f"ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, unggah_sertifikat, "
                f"skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score "
                f"FROM data_non_akademik WHERE kelas = %s"
            )
            cursor.execute(query, (teacher_class,))
            rows = cursor.fetchall()
            cursor.close()

            if rows:
                data = []
                for row in rows:
                    nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas, \
                    kepribadian_uts, kepribadian_uas, sertifikat, skor_alfa, skor_sertifikat, skor_ekstrakurikuler, \
                    skor_kepribadian, total_score = row

                    # Cek keberadaan sertifikat
                    if sertifikat:
                        sertifikat_path = os.path.join("uploads", sertifikat)
                        if os.path.exists(sertifikat_path):
                            with open(sertifikat_path, "rb") as f:
                                encoded_file = base64.b64encode(f.read()).decode()
                                download_link = f'<a href="data:image/png;base64,{encoded_file}" download="{sertifikat}">Unduh Sertifikat</a>'
                        else:
                            download_link = "Sertifikat Tidak Tersedia"
                    else:
                        download_link = "Tidak Ada Sertifikat"

                    # Tambahkan data ke list
                    data.append([nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas,
                                 kepribadian_uts, kepribadian_uas, download_link, skor_alfa, skor_sertifikat, 
                                 skor_ekstrakurikuler, skor_kepribadian, total_score])

                # Membuat DataFrame
                df = pd.DataFrame(data, columns=[
                    "NIS", "Nama", "Kelas", "Semester", "Alfa (UTS)", "Alfa (UAS)", "Ekstrakurikuler (UTS)",
                    "Ekstrakurikuler (UAS)", "Kepribadian (UTS)", "Kepribadian (UAS)", "Sertifikat",
                    "Skor Alfa", "Skor Sertifikat", "Skor Ekstrakurikuler", "Skor Kepribadian", "Total Skor"])

                # Styling dan render tabel dengan Streamlit
                st.markdown(
                    """
                    <style>
                    .dataframe-container {
                        overflow-y: auto;
                        max-height: 500px;
                        border: 1px solid #ddd;
                        padding: 15px;
                        color : #333;
                        width : 100%;
                        border-radius : 4px;
                        background-color : #f8f8f8;
                        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1)

                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        font-family: 'Arial', sans-serif;
                        background-color: #fff;
                    }
                    th {
                        position: sticky;
                        top:0;
                        background-color: #444;
                        color : white;
                        font-size: 16px;
                        padding: 12px;
                        text-align: left;
                        z-index: 1;
                    }
                    th, td {
                        padding: 10px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                        font-size: 14px;
                    }
                     tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                    td {
                        color: #555;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<div class="dataframe-container">{df.to_html(escape=False, index=False)}</div>',
                    unsafe_allow_html=True,
                )


            else:
                st.warning("Tidak ada data non-akademik yang tersedia.")
        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengambil data: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        st.error("Gagal membuat koneksi ke database.")

# def fetch_data():
    # Query untuk mengambil data siswa, akademik, dan non-akademik
    query_siswa = "SELECT nis, nama, kelas FROM data_siswa"
    query_akademik = "SELECT nis, total_nilai_uts, total_nilai_uas FROM data_akademik"
    query_non_akademik = "SELECT nis, total_score FROM data_non_akademik"
    
    # Menggunakan koneksi dengan context manager
    with create_connection() as connection:
        if connection:
            logging.debug("Koneksi berhasil, mulai mengambil data.")
            try:
                df_siswa = pd.read_sql(query_siswa, connection)
                df_akademik = pd.read_sql(query_akademik, connection)
                df_non_akademik = pd.read_sql(query_non_akademik, connection)
                logging.debug("Data berhasil diambil.")
            except Exception as e:
                logging.error(f"Kesalahan saat mengambil data: {e}")
                st.error(f"Kesalahan saat mengambil data: {e}")
                return None, None, None
        else:
            logging.error("Gagal membuat koneksi ke database.")
            st.error("Gagal membuat koneksi ke database.")
            return None, None, None
    
    return df_siswa, df_akademik, df_non_akademik

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
# 3. Fungsi halaman laporan_hasil_prediksi
def laporan_hasil_prediksi(df):
    # Menampilkan siswa yang terpilih berdasarkan prediksi
    selected_students = pd.DataFrame()
    for kelas in df['kelas'].unique():
        kelas_df = df[df['kelas'] == kelas]
        top_student = kelas_df.nlargest(1, 'total_skor_akhir')  # Memilih 1 siswa teratas berdasarkan total skor
        selected_students = pd.concat([selected_students, top_student])

    # Menampilkan 1 siswa teratas per kelas
    st.write(selected_students[['nis', 'nama', 'kelas', 'total_skor_akhir', 'layak_beasiswa_prediksi']])

# Fungsi utama untuk dashboard guru
def app():
    # Sidebar untuk menu
    with st.sidebar:
        # Judul sidebar dengan ikon
        st.markdown('<div style="font-size: 18px; font-weight: bold; color: #2C3E50;">🎓 SMK HUTAMA BEKASI 🎓</div>', unsafe_allow_html=True)
        st.markdown('<hr style="border: 1px solid #BDC3C7;">', unsafe_allow_html=True)
        
        # Menampilkan nama guru
        teacher_name = st.session_state["user"]['username']
        st.text_input("👨‍🏫 Nama Guru", value=teacher_name, disabled=True)  # Nama guru otomatis terisi dan tidak bisa diubah

        # Pilihan menu
        menu = st.selectbox("📂 Pilih Menu", ["Dashboard", "Manajemen Data Siswa", "Laporan Hasil Prediksi"])

    # Cek guru berdasarkan nama yang ada di session state
    user = get_teacher_class_by_name(teacher_name)

    # Menampilkan ucapan selamat datang dan informasi kelas
    if user:
        class_name = user['kelas_tertuju']
        
        # Logika untuk menu yang dipilih
    if menu == "Dashboard":
        # Judul Dashboard
        st.markdown('<div style="font-size:30px; font-weight:bold; color:#2C3E50;">📊Dashboard guru</div>', unsafe_allow_html=True)
        st.write("")    
        
        # Deskripsi Singkat tentang Aplikasi
        st.markdown('''
        <div style="font-size:14px; color:#4CAF50; font-weight: bold; border-radius: 8px;">
            Selamat datang di Dashboard Aplikasi Prediksi Beasiswa. Pilih menu di samping untuk memulai.
        </div>
        ''', unsafe_allow_html=True)

        # Statistik Utama
        total_siswa = 100
        layak = 53
        tidak_layak = 47

        st.write("")
        st.markdown('<div style="font-size:18px; font-weight:bold;">➡️ Statistik Utama</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Siswa", total_siswa)
        col2.metric("Siswa Layak", layak)
        col3.metric("Siswa Tidak Layak", tidak_layak)

        # Data untuk visualisasi
        data_visual = pd.DataFrame({
            "Kelayakan": ["Layak", "Tidak Layak"],
            "Jumlah": [layak, tidak_layak]
        })

        # Data siswa yang diterima beasiswa
        data_beasiswa = pd.DataFrame({
        "Nama": [
        "Gian Luigi Farrel", "Arka Sandi Aqillah", "Khalishah Salsabila", 
        "Rizka Wulan Putri", "Win Jauza Hanifah", "Ihsan Hafidh", 
        "Indriani Komala Sari", "Siti Ramona Setiadi", "Adjeng Ardhia Regita Putri", 
        "Saskia Klodiyah"
        ],
        "Kelas": [
        "X TKR", "X TKJ", "X MP", "X BC", "X AK", 
        "XI TKR", "XI TKJ", "XI MP", "XI BC", "XI AK"
        ],
        "Total Skor Akhir": [
        2051.3, 2168.6, 2136.7, 2075.95, 2103.7, 
        1930.75, 1946.95, 1962.7, 1970.7, 1972.5
        ]
        })

        # Visualisasi diagram batang
        st.write("")
        st.markdown('<div style="font-size:18px; font-weight:bold;">➡️ Skor Akhir 10 Siswa Penerima Beasiswa</div>', unsafe_allow_html=True)
        st.write("")

        fig_bar, ax_bar = plt.subplots(figsize=(8, 6))
        ax_bar.barh(
        data_beasiswa["Nama"], 
        data_beasiswa["Total Skor Akhir"], 
        color="#4CAF50"
        )
        ax_bar.set_xlabel("Total Skor Akhir", fontsize=12)
        ax_bar.set_ylabel("Nama Siswa", fontsize=12)
        ax_bar.set_title("Total Skor Akhir 10 Siswa yang Layak Menerima Beasiswa", fontsize=14)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        st.pyplot(fig_bar)

    elif menu == "Manajemen Data Siswa":
        # Menambah baris kosong
        st.text("")
        st.text("") 
        
        # Dropdown untuk memilih jenis input data
        input_data_option = st.selectbox(
            "➕ Pilih Jenis Data yang Akan Dikelola",
            ["Input Data Siswa", "Input Data Akademik", "Input Data Non-Akademik"]
        )
        
        # Menampilkan input form berdasarkan pilihan
        if input_data_option == "Input Data Siswa":
            input_student_data(class_name)
        elif input_data_option == "Input Data Akademik":
            input_academic_data(class_name)
        elif input_data_option == "Input Data Non-Akademik":
            input_non_academic_data(class_name)

    elif menu == "Laporan Hasil Prediksi":
        laporan_hasil_prediksi_app()  # Memanggil fungsi laporan hasil prediksi

    elif menu == "Logout":
        # Clear session state dan kembali ke halaman login
        st.session_state.clear()
        st.session_state["page"] = "login"
        st.success("Anda telah keluar!")  # Pesan logout sukses



    # Tombol logout di sidebar
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.session_state["page"] = "login"

        
# Menjalankan aplikasi
if __name__ == "__main__":
    app()

    
