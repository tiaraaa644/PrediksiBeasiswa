import streamlit as st
import mysql.connector
import pandas as pd

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

# Fungsi untuk mengambil data dari database
def fetch_data(query):
    conn = create_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Fungsi utama untuk menampilkan halaman
def app():
   # Menampilkan judul dengan font yang lebih kecil, emoji, dan warna hijau daun
    st.markdown('<h3 style="font-size: 20px; color: #4CAF50;  font-weight: bold; ">📊 Histori Data Siswa, Akademik, dan Non-Akademik 📚</h3>', unsafe_allow_html=True)

   # Menu Pilihan untuk memilih jenis histori tanpa sidebar
    menu = ["Data Siswa", "Data Akademik", "Data Non-Akademik"]
    choice = st.selectbox("Pilih Tabel", menu)
    
    # Menampilkan data tanpa aksi berdasarkan pilihan menu
    if choice == "Data Siswa":
        st.header("Data Siswa")
        query = "SELECT * FROM data_siswa ORDER BY timestamp DESC"
        data_siswa = fetch_data(query)
        if data_siswa:
            # Convert to pandas dataframe for better table rendering
            df_siswa = pd.DataFrame(data_siswa)
            # Display the table in Streamlit with dynamic sorting
            st.dataframe(df_siswa)
        else:
            st.write("Tidak ada data untuk ditampilkan.")

    elif choice == "Data Akademik":
        st.header("Data Akademik")
        query = "SELECT * FROM data_akademik ORDER BY timestamp DESC"
        data_akademik = fetch_data(query)
        if data_akademik:
            # Convert to pandas dataframe for better table rendering
            df_akademik = pd.DataFrame(data_akademik)
            # Display the table in Streamlit with dynamic sorting
            st.dataframe(df_akademik)
        else:
            st.write("Tidak ada data untuk ditampilkan.")

    elif choice == "Data Non-Akademik":
        st.header("Data Non-Akademik")
        query = "SELECT * FROM data_non_akademik ORDER BY timestamp DESC"
        data_non_akademik = fetch_data(query)
        if data_non_akademik:
            # Convert to pandas dataframe for better table rendering
            df_non_akademik = pd.DataFrame(data_non_akademik)
            # Display the table in Streamlit with dynamic sorting
            st.dataframe(df_non_akademik)
        else:
            st.write("Tidak ada data untuk ditampilkan.")

# Menjalankan aplikasi
if __name__ == "__main__":
    app()
