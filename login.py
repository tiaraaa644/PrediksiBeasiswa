import streamlit as st
import mysql.connector
from mysql.connector import Error
import importlib  # Untuk memuat file lain secara dinamis

# Fungsi koneksi ke database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="db_prediksi_beasiswa"
        )
        return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None

# Fungsi autentikasi pengguna
def authenticate_user(username, password):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        connection.close()
        return user
    return None

# Fungsi login
def login():
    st.markdown("<h1 style='text-align: center;'>🏫 Login 🏫</h1>", unsafe_allow_html=True)
    username = st.text_input("Username", placeholder="Masukkan username Anda")
    password = st.text_input("Password", type="password", placeholder="Masukkan password Anda")

    if st.button("Login"):
        # Menggunakan autentikasi berbasis database
        user = authenticate_user(username, password)
        if user:
            st.session_state["user"] = user  # Simpan informasi pengguna ke session state
            st.session_state["logged_in"] = True  # Tandai sebagai pengguna yang sudah login

            # Redirect berdasarkan role pengguna
            if user['role'] == 'Admin':
                st.session_state["page"] = "main"  # Arahkan ke halaman admin (main.py)
                st.success(f"Login berhasil sebagai {user['role']}!")
            elif user['role'] == 'Guru':  # Arahkan langsung ke dashboard guru
                # Simpan kelas yang diajarkan oleh guru
                st.session_state["kelas_tertuju"] = user.get('kelas_tertuju', 'Tidak ada kelas yang diajarkan')
                st.session_state["page"] = "dashboard_guru"
                st.success(f"Login berhasil sebagai {user['role']}! Anda mengajar di kelas {st.session_state['kelas_tertuju']}.")
            elif user['role'] == 'Siswa':  # Arahkan langsung ke dashboard guru
                # Simpan kelas yang diajarkan oleh guru
                st.session_state["page"] = "dashboard_siswa"  # Arahkan ke halaman admin (main.py)
                st.success(f"Login berhasil sebagai {user['role']}!")
            else:
                st.error("Role tidak dikenali!")  # Menangani jika ada role yang tidak dikenali
        else:
            st.error("Username atau password salah!")

# Fungsi untuk memuat halaman lain
def load_page(page_name):
    try:
        page_module = importlib.import_module(page_name)  # Mengimpor modul berdasarkan nama
        if hasattr(page_module, "app"):  # Memastikan bahwa halaman memiliki fungsi app()
            page_module.app()
        else:
            st.error(f"Halaman {page_name} tidak memiliki fungsi 'app()'.")
    except ModuleNotFoundError:
        st.error(f"Halaman {page_name} tidak ditemukan.")

# Tentukan halaman berdasarkan session state
if "user" not in st.session_state or not st.session_state.get("logged_in", False):
    st.session_state["page"] = "login"  # Jika belum login, arahkan ke halaman login

# Menampilkan halaman sesuai dengan session state
page = st.session_state.get("page", "login")

# Menampilkan halaman login atau halaman lain sesuai session state
if page == "login":
    login()
elif page == "main":
    load_page("main")  # Arahkan ke halaman 'main' jika admin login
elif page == "dashboard_guru":
    load_page("dashboard_guru")  # Arahkan ke halaman 'dashboard_guru' jika guru login
elif page == "dashboard_siswa":
    load_page("dashboard_siswa")  # Arahkan ke halaman 'dashboard_guru' jika guru login


