import streamlit as st
import mysql.connector
import os
import pandas as pd
from io import BytesIO
import time
import base64
from base64 import b64encode
from streamlit_option_menu import option_menu
import datetime



# Fungsi untuk membuat koneksi ke database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",        # Ganti dengan host database Anda
            user="root",             # Ganti dengan username database Anda
            password="",             # Ganti dengan password database Anda
            database="db_prediksi_beasiswa"   # Ganti dengan nama database Anda
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None



# Fungsi untuk mengecek apakah NIS sudah ada
def is_nis_exists(nis):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data_siswa WHERE nis = %s", (nis,))
        return cursor.fetchone() is not None
    finally:
        cursor.close()
        connection.close()

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

# Fungsi untuk mengambil data akademik berdasarkan NIS
def get_data(nis):
    connection = create_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM data_akademik WHERE nis = %s", (nis,))
        return cursor.fetchone()
    finally:
        cursor.close()
        connection.close()



# Fungsi untuk memuat data siswa dari database
def load_student_data():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM data_siswa"
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return data
    return []

def display_results(data):
    st.subheader("Data Siswa")
    if data:
        try:
            # Konversi data menjadi DataFrame untuk tampilan rapi
            df = pd.DataFrame(data)
            # Pastikan urutan kolom sesuai kebutuhan
            if not df.empty:
                df = df[['nis', 'nama', 'jenis_kelamin', 'kelas']]
                df.columns = ["NIS", "Nama", "Jenis Kelamin", "Kelas",]
            # Tampilkan tabel scrollable tanpa indeks
            st.dataframe(df.style.hide(axis="index"), height=400)
        except Exception as e:
            st.error(f"Terjadi kesalahan saat menampilkan data: {e}")
    else:
        st.warning("Tidak ada data yang tersedia.")

        
# Fungsi untuk menampilkan data akademik siswa
def load_academic_data():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM data_akademik"  # Ganti dengan tabel data akademik Anda
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return data
    return []

# Fungsi untuk menampilkan data non-akademik siswa
def load_non_academic_data():
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM data_non_akademik"  # Ganti dengan tabel data non-akademik Anda
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return data
    return []

# Fungsi untuk mengelola data siswa
def manage_student_data():
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
            
            # Cek apakah NIS sudah ada dalam database
            check_query = "SELECT COUNT(*) FROM data_siswa WHERE nis = %s"
            cursor.execute(check_query, (nis,))
            result = cursor.fetchone()
            
            if result[0] > 0:
                st.warning("NIS sudah terdaftar! Gunakan NIS lain atau periksa kembali data siswa.")
            else:
                insert_query = """INSERT INTO data_siswa (nis, nama, jenis_kelamin, kelas) 
                                  VALUES (%s, %s, %s, %s)"""
                cursor.execute(insert_query, (nis, nama, jenis_kelamin, kelas))
                connection.commit()
                st.success("Data siswa berhasil disimpan!")
                st.rerun()
            
            connection.close()
            

    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    # Menampilkan data siswa setelah form input
    data_siswa = load_student_data()
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📋Tampil Data Siswa</div>', unsafe_allow_html=True)
    display_results(data_siswa)  # Menampilkan data siswa dengan tampilan yang rapi


    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    # Update atau Delete data siswa
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>🔄Update & Delete Data Siswa🗑️</div>', unsafe_allow_html=True)
    update_nis = st.text_input("Masukkan NIS untuk update atau hapus data")
    if update_nis:
        student_data = next((item for item in data_siswa if item["nis"] == update_nis), None)
        if student_data:
            # Form update data siswa
            with st.form(key="update_student_form"):
                nis = st.text_input("NIS", value=student_data["nis"], disabled=True)
                nama = st.text_input("Nama", value=student_data["nama"])
                jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"],
                                             index=["Laki-laki", "Perempuan"].index(student_data["jenis_kelamin"]))
                kelas = st.text_input("Kelas", value=student_data["kelas"])
                submit_button = st.form_submit_button("Update Data Siswa")

                if submit_button:
                    connection = create_connection()
                    if connection:
                        cursor = connection.cursor()
                        query = """UPDATE data_siswa SET nama = %s, jenis_kelamin = %s, kelas = %s WHERE nis = %s"""
                        cursor.execute(query, (nama, jenis_kelamin, kelas, nis))
                        connection.commit()
                        connection.close()
                        st.success("Data siswa berhasil diperbarui!")
                        st.rerun()  # Refresh setelah update

            # Form delete data siswa
            if st.button(f"Delete Data Siswa {student_data['nama']}"):
                connection = create_connection()
                if connection:
                    cursor = connection.cursor()
                    query = """DELETE FROM data_siswa WHERE nis = %s"""
                    cursor.execute(query, (update_nis,))
                    connection.commit()
                    connection.close()
                    st.success("Data siswa berhasil dihapus!")
                    st.rerun()  # Refresh setelah delete

# Fungsi utama manajemen data akademik
def manage_academic_data():
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

    # Judul utama dengan ikon
    st.markdown('<div class="custom-title"><span class="custom-icon"></span> 📚Data Akademik</div>', unsafe_allow_html=True)

    # Subjudul untuk form input data akademik
    st.markdown('<div class="custom-subtitle"><span class="custom-icon"></span>➕Tambah Data Akademik</div>', unsafe_allow_html=True)

    # 1. Form Input Data Akademik
    with st.form(key="academic_data_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            nis = st.text_input("NIS")
        with col2:
            nama = st.text_input("Nama")
        with col3:
            kelas = st.text_input("Kelas")
        
        col4, col5 = st.columns(2)
        with col4:
            total_nilai_uts = st.number_input("Total Nilai (UTS)", min_value=0)
        with col5:
            total_nilai_uas = st.number_input("Total Nilai (UAS)", min_value=0)
        
        semester = st.selectbox(
            "Semester", 
            ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"]
        )

        # File uploader untuk rapor
        unggah_rapor_1 = st.file_uploader("Unggah Rapor 1 (PDF)", type=["pdf"], key="rapor_1")
        unggah_rapor_2 = st.file_uploader("Unggah Rapor 2 (PDF)", type=["pdf"], key="rapor_2")

        submit_button = st.form_submit_button("Simpan Data Akademik")

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

    # 2. Menampilkan Data Akademik
    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📋Tampil Data Akademik</div>', unsafe_allow_html=True)
    connection = create_connection()

    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT nis, nama, kelas, total_nilai_uts, total_nilai_uas, semester, unggah_rapor_1, unggah_rapor_2 FROM data_akademik"
            cursor.execute(query)
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
                # Menambahkan kolom nomor urut
                df.insert(0, "No", range(1, len(df) + 1))
                # Styling dan render tabel dengan Streamlit
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
                st.warning("Tidak ada data akademik yang tersedia.")

        except Exception as e:
            st.error(f"Terjadi kesalahan saat mengambil data: {e}")

        finally:
            connection.close()

    else:
        st.error("Gagal membuat koneksi ke database.")



    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    # 3. Form Update dan Hapus Data Akademik
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>🔄Update & Delete Data Akademik🗑️</div>', unsafe_allow_html=True)
    update_nis = st.text_input("Masukkan NIS untuk update atau hapus data")
    # Menampilkan form update hanya setelah NIS dimasukkan
    if update_nis:
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query_check = "SELECT nama, kelas, total_nilai_uts, total_nilai_uas, semester, unggah_rapor_1, unggah_rapor_2 FROM data_akademik WHERE nis = %s"
                cursor.execute(query_check, (update_nis,))
                result = cursor.fetchone()
                if result:
                    # Jika NIS ditemukan, tampilkan form update
                    nama, kelas, total_nilai_uts, total_nilai_uas, semester, rapor_1, rapor_2 = result
                    st.info("NIS ditemukan! Silakan perbarui data.")

                    # Form update data akademik
                    with st.form(key="update_form"):
                        input_nama = st.text_input("Nama", value=nama)
                        input_kelas = st.text_input("Kelas", value=kelas)
                        input_total_nilai_uts = st.number_input("Total Nilai (UTS)", min_value=0, value=total_nilai_uts)
                        input_total_nilai_uas = st.number_input("Total Nilai (UAS)", min_value=0, value=total_nilai_uas)
                        input_semester = st.selectbox( "Semester", 
                     ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"], 
                     index=["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"].index(semester) if semester else 0)

                        # Upload File Rapor
                        unggah_rapor_1 = st.file_uploader("Unggah Rapor 1 (PDF)", type=["pdf"], key="update_rapor_1")
                        unggah_rapor_2 = st.file_uploader("Unggah Rapor 2 (PDF)", type=["pdf"], key="update_rapor_2")

                        update_button = st.form_submit_button("Update Data")
                        delete_button = st.form_submit_button("Hapus Data")

                    # Fungsi Update Data
                    if update_button:
                        connection = create_connection()
                        if connection:
                            try:
                                cursor = connection.cursor()

                                # Simpan file baru jika diunggah
                                rapor_1_name = rapor_1
                                rapor_2_name = rapor_2
                                os.makedirs("uploads", exist_ok=True)

                                if unggah_rapor_1:
                                    rapor_1_name = unggah_rapor_1.name
                                    with open(f"uploads/{rapor_1_name}", "wb") as f:
                                        f.write(unggah_rapor_1.getbuffer())

                                if unggah_rapor_2:
                                    rapor_2_name = unggah_rapor_2.name
                                    with open(f"uploads/{rapor_2_name}", "wb") as f:
                                        f.write(unggah_rapor_2.getbuffer())

                                # Query Update
                                query_update = """
                                    UPDATE data_akademik
                                    SET nama = %s, kelas = %s, total_nilai_uts = %s, total_nilai_uas = %s, semester = %s,
                                        unggah_rapor_1 = %s, unggah_rapor_2 = %s
                                    WHERE nis = %s
                                """
                                cursor.execute(query_update, (input_nama, input_kelas, input_total_nilai_uts, 
                                                             input_total_nilai_uas, input_semester, 
                                                             rapor_1_name, rapor_2_name, update_nis))
                                connection.commit()
                                st.success("Data akademik dan file rapor berhasil diperbarui!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Terjadi kesalahan saat memperbarui data: {e}")
                            finally:
                                connection.close()

                    # Fungsi Hapus Data
                    if delete_button:
                        connection = create_connection()
                        if connection:
                            try:
                                cursor = connection.cursor()

                                # Hapus file rapor dari folder jika ada
                                if rapor_1 and os.path.exists(f"uploads/{rapor_1}"):
                                    os.remove(f"uploads/{rapor_1}")
                                if rapor_2 and os.path.exists(f"uploads/{rapor_2}"):
                                    os.remove(f"uploads/{rapor_2}")

                                # Hapus data dari database
                                query_delete = "DELETE FROM data_akademik WHERE nis = %s"
                                cursor.execute(query_delete, (update_nis,))
                                connection.commit()
                                st.success("Data akademik dan file rapor berhasil dihapus!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Terjadi kesalahan saat menghapus data: {e}")
                            finally:
                                connection.close()

                else:
                    st.warning("NIS tidak ditemukan di database.")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
            finally:
                connection.close()


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

# Fungsi untuk mengelola data non-akademik
def manage_non_academic_data():
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

    semester_list = ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"]

    # Judul utama dengan ikon
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📚Data Non-Akademik</div>', unsafe_allow_html=True)
    st.write("")
    # Judul utama dengan ikon untuk Tabel Skala Nilai
    st.markdown('<div class="custom-subtitle"><span class="custom-icon"></span>📊 Skala Nilai Ekstrakurikuler dan Alfa</div>', unsafe_allow_html=True)
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

    # Subjudul untuk form input data akademik
    st.markdown('<div class="custom-subtitle"><span class="custom-icon"></span> ➕Tambah Data Non-Akademik</div>', unsafe_allow_html=True)

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
        
        # Input Lain-lain
        st.markdown("**Lain-lain**")
        lain_lain = st.text_area("Lain-lain (Opsional)")
        # Tombol Simpan
        submit_button = st.form_submit_button("Simpan Data Non-Akademik")


        # Validasi dan Simpan Data
        if submit_button:
            timestamp = datetime.datetime.now()
            if not (nis and nama and kelas):
                st.error("NIS, Nama, dan Kelas wajib diisi!")
            else:
                try:
                    # Perhitungan Skor Sertifikat (jika ada sertifikat)
                    skor_sertifikat = 0
                    if sertifikat_tipe != "Tidak Ada Sertifikat":
                        skor_sertifikat = calculate_certificate_score(
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

                    # Simpan file sertifikat ke folder uploads jika ada
                    sertifikat_file_name = None
                    if uploaded_file is not None:
                        file_path = os.path.join("uploads", uploaded_file.name)
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getbuffer())
                        sertifikat_file_name = uploaded_file.name

                    # Menambahkan link download untuk sertifikat
                    if sertifikat_file_name:
                        file_path = os.path.join("uploads", sertifikat_file_name)
                        if os.path.exists(file_path):
                            base64_file = get_base64_encoded_file(file_path)
                            download_link = f'<a href="data:image/png;base64,{base64_file}" download="{sertifikat_file_name}">Unduh Sertifikat</a>'
                            st.markdown(download_link, unsafe_allow_html=True)
                        else:
                            st.error("File sertifikat tidak ditemukan!")
                    else:
                        st.write("Tidak ada sertifikat yang diunggah.")

                    # Simpan ke database
                    connection = create_connection()
                    if connection:
                        query = """
                            INSERT INTO data_non_akademik 
                            (nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, 
                            ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, unggah_sertifikat, 
                            skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        cursor = connection.cursor()
                        cursor.execute(query, (nis, nama, kelas, semester_update, alfa_uts, alfa_uas, ekstrakurikuler_uts, 
                                               ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, sertifikat_file_name, 
                                               skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain))
                        connection.commit()
                        cursor.close()
                        st.success("Data non-akademik berhasil disimpan!")
                        st.rerun()

                except Exception as e:
                    st.error(f"Terjadi kesalahan saat mengambil data: {e}")

# 2. Menampilkan Data Non-Akademik
    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>📋Tampil Data Non-Akademik</div>', unsafe_allow_html=True)
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """SELECT nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, 
                              ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, unggah_sertifikat, 
                              skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain
                       FROM data_non_akademik"""
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            
            if rows:
                data = []
                for row in rows:
                    nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, sertifikat, skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain = row
                    if sertifikat:
                        sertifikat_path = os.path.join("uploads", sertifikat)
                        if os.path.exists(sertifikat_path):
                            with open(sertifikat_path, "rb") as f:
                                download_link = f'<a href="data:image/png;base64,{base64.b64encode(f.read()).decode()}" download="{sertifikat}">Unduh Sertifikat</a>' 
                        else:
                            download_link = "Sertifikat Tidak Tersedia"
                    else:
                        download_link = "Tidak Ada Sertifikat"

                    data.append([nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, f"{download_link}", skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain])

                df = pd.DataFrame(data, columns=["NIS", "Nama", "Kelas", "Semester", "Alfa (UTS)", "Alfa (UAS)", 
                                                 "Ekstrakurikuler (UTS)", "Ekstrakurikuler (UAS)", "Kepribadian (UTS)", 
                                                 "Kepribadian (UAS)", "Sertifikat", "Skor Alfa", "Skor Sertifikat", 
                                                 "Skor Ekstrakurikuler", "Skor Kepribadian", "Total Skor", "Lain-lain"])
                df.insert(0, "No", range(1, len(df) + 1))
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
            connection.close()

  # Form Update dan Hapus Data Non-Akademik
    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    st.text("")  # Menambah baris kosong
    st.markdown('<div class="custom-title"><span class="custom-icon"></span>🔄Update & Delete Data Non Akademik🗑️</div>', unsafe_allow_html=True)
    update_nis = st.text_input("Masukkan NIS untuk update atau hapus data")
# Memeriksa apakah ada input NIS
    if update_nis:
        connection = create_connection()  # Pastikan koneksi dilakukan jika ada NIS yang dimasukkan
    if connection:  # Pastikan koneksi berhasil
        try:
            cursor = connection.cursor()
            query_check = """
                SELECT nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, 
                       ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, unggah_sertifikat, 
                       skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain
                FROM data_non_akademik
                WHERE nis = %s
            """
            cursor.execute(query_check, (update_nis,))
            result = cursor.fetchone()

            if result:
                # Jika NIS ditemukan, tampilkan form update
                nis, nama, kelas, semester, alfa_uts, alfa_uas, ekstrakurikuler_uts, ekstrakurikuler_uas, kepribadian_uts, kepribadian_uas, unggah_sertifikat, skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, lain_lain = result
                st.info("NIS ditemukan! Silakan perbarui data non-akademik.")

                # Form update data
                with st.form(key="update_form"):
                    input_nama = st.text_input("Nama", value=nama)
                    input_kelas = st.text_input("Kelas", value=kelas)
                    input_semester = st.selectbox(
                        "Semester", ["Semester 1", "Semester 2", "Semester 3", "Semester 4"],
                        index=int(semester[-1]) - 1  # Konversi semester ke index
                    )
                    input_alfa_uts = st.number_input("Alfa (UTS)", min_value=0, value=alfa_uts)
                    input_alfa_uas = st.number_input("Alfa (UAS)", min_value=0, value=alfa_uas)
                    input_ekstrakurikuler_uts = st.number_input("Ekstrakurikuler (UTS)", min_value=0, value=ekstrakurikuler_uts)
                    input_ekstrakurikuler_uas = st.number_input("Ekstrakurikuler (UAS)", min_value=0, value=ekstrakurikuler_uas)
                    input_kepribadian_uts = st.number_input("Kepribadian (UTS)", min_value=0, value=kepribadian_uts)
                    input_kepribadian_uas = st.number_input("Kepribadian (UAS)", min_value=0, value=kepribadian_uas)

                    # Input Sertifikat (tidak wajib)
                    sertifikat_tipe = st.selectbox("Tipe Sertifikat (Opsional)", ["Kedinasan", "Organisasi", "Jambore", "Tidak Ada Sertifikat"])
                    sertifikat_tingkat = st.selectbox("Tingkat Sertifikat", ["Internasional", "Nasional", "Provinsi", "Kota/Kab"]) if sertifikat_tipe != "Tidak Ada Sertifikat" else None
                    sertifikat_berjenjang = None
                    if sertifikat_tipe != "Jambore" and sertifikat_tipe != "Tidak Ada Sertifikat":
                        sertifikat_berjenjang = st.selectbox("Berjenjang atau Tidak", ["berjenjang", "tidak berjenjang"])
                    sertifikat_juara = st.selectbox("Juara Sertifikat", [1, 2, 3]) if sertifikat_tipe != "Tidak Ada Sertifikat" else None

                    # Skor sertifikat otomatis menjadi 0 untuk tipe "Tidak Ada Sertifikat"
                    skor_sertifikat = 0 if sertifikat_tipe == "Tidak Ada Sertifikat" else calculate_certificate_score(
                        tipe=sertifikat_tipe,
                        tingkat=sertifikat_tingkat,
                        sifat=sertifikat_berjenjang,
                        juara=sertifikat_juara
                    )

                    # Input Lain-lain
                    input_lain_lain = st.text_area("Lain-lain (Opsional)", value=lain_lain if 'lain_lain' in locals() else "")


                    # Unggah sertifikat (opsional)
                    uploaded_file = st.file_uploader("Unggah Sertifikat (Opsional)", type=["jpg", "jpeg", "png"])

                    update_button = st.form_submit_button("Update Data")
                    delete_button = st.form_submit_button("Hapus Data")

                # Proses update data
                # Panggil fungsi sebelum operasi update
                if update_button:
                    try:
                        # Gabungkan nilai Alfa (UTS dan UAS) menjadi skor_alfa
                        gabungan_alfa = input_alfa_uts + input_alfa_uas
                        skor_alfa = 5 if gabungan_alfa == 0 else 3 if gabungan_alfa <= 3 else 0

                        # Menghitung skor non-akademik
                        skor_ekstrakurikuler = calculate_non_academic_score(input_ekstrakurikuler_uts, input_ekstrakurikuler_uas)
                        skor_kepribadian = calculate_non_academic_score(input_kepribadian_uts, input_kepribadian_uas)

                        # Menghitung skor gabungan dan memberikan bobot
                        total_score = calculate_weighted_score(skor_alfa, skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian)

                        # Pastikan unggah_sertifikat terisi jika file tidak ada
                        unggah_sertifikat = uploaded_file.name if uploaded_file else None

                        query_update = """
                            UPDATE data_non_akademik
                            SET nama = %s, kelas = %s, semester = %s, alfa_uts = %s, alfa_uas = %s, 
                                ekstrakurikuler_uts = %s, ekstrakurikuler_uas = %s, kepribadian_uts = %s, 
                                kepribadian_uas = %s, unggah_sertifikat = %s, skor_alfa = %s, 
                                skor_sertifikat = %s, skor_ekstrakurikuler = %s, skor_kepribadian = %s, total_score = %s, lain_lain= %s
                            WHERE nis = %s
                        """
                        cursor.execute(query_update, (
                            input_nama, input_kelas, input_semester, input_alfa_uts, input_alfa_uas,
                            input_ekstrakurikuler_uts, input_ekstrakurikuler_uas, input_kepribadian_uts,
                            input_kepribadian_uas, unggah_sertifikat, skor_alfa, 
                            skor_sertifikat, skor_ekstrakurikuler, skor_kepribadian, total_score, input_lain_lain, update_nis
                        ))
                        connection.commit()
                        st.success("Data non-akademik berhasil diperbarui!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Terjadi kesalahan saat memperbarui data: {e}")
                        connection.rollback()

                # Proses hapus data
                if delete_button:
                    try:
                        query_delete = "DELETE FROM data_non_akademik WHERE nis = %s"
                        cursor.execute(query_delete, (update_nis,))
                        connection.commit()
                        st.success("Data non-akademik berhasil dihapus!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Terjadi kesalahan saat menghapus data: {e}")
                        connection.rollback()

            else:
                st.warning("NIS tidak ditemukan di database.")
        except Exception as e:
            st.error
        finally:
            connection.close()

  

# Fungsi utama manajemen data siswa
def app():
    # Menu sidebar dengan ikon
    with st.sidebar:
        menu = option_menu(
            "Navigasi",
            ["Data Siswa", "Data Akademik", "Data Non-Akademik",  "Logout"],
            icons=["people", "book", "clipboard", "box-arrow-right"],
            menu_icon="list",
            default_index=0,
        )

    # Navigasi berdasarkan pilihan menu
    if menu == "Data Siswa":
        manage_student_data()
    elif menu == "Data Akademik":
        manage_academic_data()
    elif menu == "Data Non-Akademik":
        manage_non_academic_data()
    elif menu == "Logout":
        st.session_state.clear()
        st.session_state["page"] = "login"
        st.success("Anda telah keluar!")

 
# Jalankan aplikasi jika file ini dipanggil langsung
if __name__ == "__main__":
    app()

