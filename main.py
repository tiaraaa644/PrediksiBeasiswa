import streamlit as st
from manajemen_data_siswa import app as manajemen_data_siswa_app
from prediksi_beasiswa import app as prediksi_beasiswa_app
from laporan_hasil_prediksi import app as laporan_hasil_prediksi_app
from histori_data import app as histori_data_app
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import mysql.connector


# 1. Koneksi ke database dan ambil data
def get_data():
    # Koneksi ke database MySQL
    connection = mysql.connector.connect(
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
    threshold = 1890
    df['layak_beasiswa'] = df['total_skor_akhir'].apply(lambda x: 'layak' if x > threshold else 'tidak layak')

    return df

def app():

    st.sidebar.markdown("""
    <style>
        /* Styling Sidebar Header */
        .sidebar-header {
            font-size: 15px;
            font-weight: bold;
            color: #ffffff;
            background-color: #4CAF50;
            padding: 15px;
            text-align: center;
            border-radius: 8px;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }

        /* Styling Selectbox */
        .sidebar-selectbox {
            font-size: 16px;
            color: #333333;
            background-color: #f4f4f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Styling the select box options */
        .sidebar-selectbox select {
            font-size: 16px;
            color: #333;
            background-color: #ffffff;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            width: 100%;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        .sidebar-selectbox option {
            font-size: 16px;
            padding: 10px;
        }

        /* Styling for page content */
        .content-area {
            margin-top: 50px;
            text-align: center;
            font-family: Arial, sans-serif;
        }

        /* Styling for section headers */
        .section-header {
            font-size: 24px;
            font-weight: bold;
            margin-top: 30px;
        }

        /* Styling for the image */
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        /* Styling for buttons */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #45a049;
            box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar Title
    st.sidebar.markdown('<div class="sidebar-header">🏫SMK HUTAMA BEKASI🏫</div>', unsafe_allow_html=True)
    # Menampilkan selectbox untuk navigasi menu di sidebar
    menu = ["Dashboard", "Manajemen Data Siswa", "Prediksi Beasiswa", "Laporan Hasil Prediksi", "Histori Data", "Logout"]
    selected_menu = st.sidebar.selectbox(
        "", 
        menu, 
        index=0, 
        format_func=lambda x: f"➡ {x}",
        key="sidebar-menu",
    )

    # Menampilkan konten berdasarkan pilihan menu
    if selected_menu == "Dashboard":
        # Judul Dashboard
        st.markdown('<div style="font-size:30px; font-weight:bold; color:#2C3E50;">📊Dashboard Admin</div>', unsafe_allow_html=True)
        st.write("")    
        # Deskripsi Singkat tentang Aplikasi
        st.markdown('''
    <div style="font-size:14px; color:#4CAF50; font-weight: bold; border-radius: 8px;">
        Hello Admin, Selamat datang di Dashboard Aplikasi Prediksi Beasiswa. Pilih menu di samping untuk memulai.
    </div>
''', unsafe_allow_html=True)

        # Statistik Utama
        total_siswa = 100
        layak = 53
        tidak_layak = 47

        st.write("")
        st.markdown('<div style="font-size:18px; font-weight:bold;">➡ Statistik Utama</div>', unsafe_allow_html=True)
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
        st.markdown('<div style="font-size:18px; font-weight:bold;">➡ Skor Akhir 10 Siswa Penerima Beasiswa</div>', unsafe_allow_html=True)
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




    elif selected_menu == "Manajemen Data Siswa":
        manajemen_data_siswa_app()  # Memanggil fungsi app() dari manajemen_data_siswa.py

    elif selected_menu == "Prediksi Beasiswa":
        prediksi_beasiswa_app()  # Memanggil fungsi app() dari prediksi_beasiswa.py

    elif selected_menu == "Laporan Hasil Prediksi":
        laporan_hasil_prediksi_app()  # Memanggil fungsi app() dari laporan_hasil_prediksi.py
    elif selected_menu == "Histori Data":
        histori_data_app()  # Memanggil fungsi app() dari laporan_hasil_prediksi.py

    elif selected_menu == "Logout":
        # Clear session state dan kembali ke halaman login
            st.session_state.clear()  # Menghapus data session
            st.session_state["page"] = "login"
            st.success("Anda telah keluar!")         

# Jalankan aplikasi jika file ini dipanggil langsung
if __name__ == "_main_":
    app()
