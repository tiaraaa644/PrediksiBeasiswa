import streamlit as st

# Fungsi untuk menampilkan konten berdasarkan menu yang dipilih
def app():
    # Menambahkan menu navigasi
    menu = st.sidebar.selectbox("Pilih Menu", ["Beranda", "Visi dan Misi", "Profil", "Postingan"])

    # Styling untuk tampilan
    st.markdown("""
    <style>
        .section-header {
            font-size: 28px;
            font-weight: bold;
            color: #1ABC9C; /* Warna hijau toska */
            margin-top: 20px;
            text-align: left;
        }

        .text-description {
            font-size: 18px;
            color: #34495E; /* Warna abu gelap */
            line-height: 1.8;
            text-align: justify;
        }

        .contact-info {
            font-size: 16px;
            color: #2ECC71; /* Warna hijau */
            margin-bottom: 10px;
        }

        ul {
            color: #3498DB; /* Warna biru */
        }
    </style>
    """, unsafe_allow_html=True)

    # Tampilkan konten berdasarkan menu yang dipilih
    if menu == "Beranda":
        st.markdown("<div class='section-header'>✨ Selamat Datang di SMK Hutama Bekasi ✨</div>", unsafe_allow_html=True)
        st.write("")

        # Menambahkan Gambar Berdampingan dengan st.columns()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://smkhutama.sch.id/wp-content/uploads/2020/11/gallery4.jpg", use_container_width=True)
        with col2:
            st.image("https://smkhutama.sch.id/wp-content/uploads/2020/11/paskibra2-1.jpg", use_container_width=True)
        with col3:
            st.image("https://smkhutama.sch.id/wp-content/uploads/2020/11/paskibra.jpg", use_container_width=True)

        # Menampilkan Video YouTube
        st.markdown("<div class='section-header'>🎥 Video Tentang SMK HUTAMA 🎥</div>", unsafe_allow_html=True)
        st.video("https://youtu.be/pzcajgImgOY")
        st.video("https://youtu.be/MSR3bqmdgg8")

        # Sejarah Sekolah
        st.markdown("<div class='section-header'>📜 Sejarah SMK HUTAMA 📜</div>", unsafe_allow_html=True)
        st.markdown('<div class="text-description">SMK HUTAMA didirikan pada tahun 1988, berstatus Terakreditasi “A”. Sekolah Menengah Kejuruan (SMK) Hutama berada di bawah Yayasan Pendidikan 1988 (YP88), yang merupakan Yayasan Keluarga. Sejak didirikan, SMK HUTAMA telah berkomitmen untuk menyediakan pendidikan yang berkualitas di bidang Teknologi dan Informatika.</div>', unsafe_allow_html=True)

        # Menampilkan Jurusan di SMK Hutama
        st.markdown("<div class='section-header'>📚 Jurusan di SMK HUTAMA Bekasi 📚</div>", unsafe_allow_html=True)
        st.markdown("""
        <ul>
            <li>💼 Akuntansi</li>
            <li>🖇️ Administrasi Perkantoran</li>
            <li>🎥 Broadcasting</li>
            <li>🔧 Teknik Kendaraan Ringan</li>
            <li>💻 Teknik Komputer dan Jaringan</li>
        </ul>
        """, unsafe_allow_html=True)

        # Hubungi Kami
        st.markdown("<div class='section-header'>📞 Hubungi Kami 📞</div>", unsafe_allow_html=True)
        st.markdown('<div class="text-description">Untuk informasi lebih lanjut, Anda bisa menghubungi kami melalui:</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Alamat:</strong> Jl. Raya Pendidikan No. 88, Bekasi</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Telepon:</strong> (021) 12345678</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Email:</strong> info@smkhutama.sch.id</div>', unsafe_allow_html=True)

    elif menu == "Visi dan Misi":
        st.markdown("<div class='section-header'>🌟 VISI dan MISI SMK HUTAMA 🌟</div>", unsafe_allow_html=True)
         # Visi
        st.markdown("<div class='section-header'>VISI</div>", unsafe_allow_html=True)  
        st.markdown("<div class='text-description'>Mewujudkan siswa siswi sekolah yang bertanggung jawab, unggul dalam prestasi, memiliki keterampilan, keahlian yang mantap dan berprestasi tinggi</div>", unsafe_allow_html=True)
    
    # Misi
        st.markdown("<div class='section-header'>MISI</div>", unsafe_allow_html=True)
        st.markdown("""
    <ul class='text-description'>
        <li>Menyediakan pendidikan berkualitas dalam bidang Teknologi dan Informatika.</li>
        <li>Meningkatkan keterampilan siswa dalam berbagai bidang teknologi.</li>
        <li>Menjalin kerjasama dengan industri untuk mendukung program pendidikan.</li>
        <li>Memberikan ilmu pengetahuan dan keterampilan kepada siswa agar menjadi sumber daya manusia yang berpotensi</li>
        <li>Mewujudkan peningkatan prestasi siswa untuk bersaing dalam prestasi yang dilandasi semangat tauladan yang baik</li>
    </ul>
    """, unsafe_allow_html=True)
        st.markdown("<div class='section-header'>TUJUAN SMK HUTAMA</div>", unsafe_allow_html=True)
        st.markdown("<div class='text-description'>Mewujudkan pendidikan berkualitas yang dilandasi iman dan taqwa dengan mengembangkan potensi, kreatifitas, keterampilan peserta didik yang unggul dan terdepan</div>", unsafe_allow_html=True)
     # Hubungi Kami
        st.markdown("<div class='section-header'>Hubungi Kami</div>", unsafe_allow_html=True)
        st.markdown('<div class="text-description">Untuk informasi lebih lanjut, Anda bisa menghubungi kami melalui:</div>', unsafe_allow_html=True)
        
        # Informasi Kontak
        st.markdown('<div class="contact-info"><strong>Alamat:</strong> Jl. Raya Pendidikan No. 88, Bekasi</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Telepon:</strong> (021) 12345678</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Email:</strong> info@smkhutama.sch.id</div>', unsafe_allow_html=True)
        
        # Formulir Kontak (Opsional, jika ingin memungkinkan pengguna mengirim pesan)
        st.markdown('<div class="text-description"><strong>Atau kirim pesan kepada kami:</strong></div>', unsafe_allow_html=True)
        st.write("")
        with st.form(key="contact_form"):
            name = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            message = st.text_area("Pesan")
            submit_button = st.form_submit_button(label="Kirim")
            
            if submit_button:
                st.success("Pesan Anda telah terkirim. Terima kasih!")

    elif menu == "Profil":
        st.markdown("<div class='section-header'>👩‍🏫 Profil Sekolah 👨‍🏫</div>", unsafe_allow_html=True)
        st.markdown('<div class="text-description">SMK HUTAMA didirikan pada tahun 1988, berstatus Terakreditasi “A”. Sekolah Menengah Kejuruan (SMK) Hutama berada di bawah Yayasan Pendidikan 1988 (YP88), yang merupakan Yayasan Keluarga. Sejak didirikan, SMK HUTAMA telah berkomitmen untuk menyediakan pendidikan yang berkualitas di bidang Teknologi dan Informatika.</div>', unsafe_allow_html=True)
        st.markdown("<div class='section-header'>SAMBUTAN KEPALA SMK HUTAMA</div>", unsafe_allow_html=True)
        st.markdown("""
<div style="display: flex; align-items: center;">
    <div style="flex: 1; padding-right: 20px;">
        <img src="https://smkhutama.sch.id/wp-content/uploads/2024/08/Kepsek1.jpg" alt="SMK Hutama" style="max-width: 100%; height: auto; border-radius: 10px;">
    </div>
    <div style="flex: 2; font-size: 16px; text-align: justify;">
        Assalamu’alaikum wr.wb. Puji syukur kita panjatkan kehadirat Allah SWT atas segala limpahan rahmat, taufiq dan hidayah-Nya, sehingga kita masih diberi kesempatan untuk berpartisipasi secara aktif dalam dunia pendidikan. Pembuatan website SMK HUTAMA ini dimaksudkan untuk memperkenalkan sekolah secara luas kepada masyarakat dan sebagai sarana informasi dan komunikasi antara pihak sekolah dengan siswa, guru, karyawan, alumni dan stakeholders yang memiliki kepedulian, wewenang, dan tanggung jawab dalam memajukan yongsong Generasi Emas tahun 2045 kami bersepakat dengan motto KREATIF, INOVATIF.
    </div>
</div>
""", unsafe_allow_html=True)
     # Hubungi Kami
        st.markdown("<div class='section-header'>Hubungi Kami</div>", unsafe_allow_html=True)
        st.markdown('<div class="text-description">Untuk informasi lebih lanjut, Anda bisa menghubungi kami melalui:</div>', unsafe_allow_html=True)
        
        # Informasi Kontak
        st.markdown('<div class="contact-info"><strong>Alamat:</strong> Jl. Raya Pendidikan No. 88, Bekasi</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Telepon:</strong> (021) 12345678</div>', unsafe_allow_html=True)
        st.markdown('<div class="contact-info"><strong>Email:</strong> info@smkhutama.sch.id</div>', unsafe_allow_html=True)
        
        # Formulir Kontak (Opsional, jika ingin memungkinkan pengguna mengirim pesan)
        st.markdown('<div class="text-description"><strong>Atau kirim pesan kepada kami:</strong></div>', unsafe_allow_html=True)
        st.write("")
        with st.form(key="contact_form"):
            name = st.text_input("Nama Lengkap")
            email = st.text_input("Email")
            message = st.text_area("Pesan")
            submit_button = st.form_submit_button(label="Kirim")
            
            if submit_button:
                st.success("Pesan Anda telah terkirim. Terima kasih!")  
    elif menu == "Postingan":
        st.markdown("<div class='section-header'>📰 Postingan 📰</div>", unsafe_allow_html=True)
        st.markdown('<div class="text-description">Postingan terkini akan ditampilkan di sini. Ikuti informasi terbaru mengenai kegiatan dan prestasi di SMK Hutama Bekasi.</div>', unsafe_allow_html=True)

# Menjalankan aplikasi
if __name__ == "__main__":
    app()
