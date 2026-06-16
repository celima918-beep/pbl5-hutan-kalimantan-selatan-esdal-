import streamlit as st
import pandas as pd

# Konfigurasi halaman utama aplikasi
st.set_page_config(
    page_title="Eco-Forest Valuation - Kalsel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Navigasi menu utama berdasarkan rencana induk pilar aplikasi
st.sidebar.title("Eco-Forest Valuation")
st.sidebar.write("Aplikasi Pembelajaran Ekonomi Sumber Daya Hutan")
st.sidebar.write("Referensi Teoretis: Tietenberg & Lewis Chapter 13")

menu = st.sidebar.radio(
    "Pilih Modul Pembelajaran:",
    ["Halaman Utama & Teori", "Modul 1: Kalkulator TEV", "Modul 2: Analisis Trade-off", "Modul 3: Kebijakan PES", "Modul 4: Kasus Interaktif"]
)

# Tampilan Alur Belajar Pengguna pada Sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("Rencana Alur Belajar")
st.sidebar.caption("Fase 1: Teori -> Fase 2: Valuasi -> Fase 3: Simulasi -> Fase 4: Evaluasi")

# Data input berdasarkan berkas DATA PBL5.xlsx dan BPS Kalimantan Selatan
data_kalsel = {
    "Hutan Lindung": 308221.52,
    "Suaka Alam & Pelestarian Alam": 267541.98,
    "Hutan Production Terbatas": 31220.48,
    "Hutan Produksi Tetap": 394563.75,
    "Hutan Produksi Dapat Dikonversi": 38663.39,
    "Nilai Kayu": 6991011291,
    "Nilai Karbon": 379053921,
    "Nilai Oksigen": 2117993021
}

# HALAMAN UTAMA & TEORI DASAR
if menu == "Halaman Utama & Teori":
    # Bagian Identitas Kampus dan Kelompok di Halaman Depan Utama
    col_logo, col_judul = st.columns([1, 4])
    with col_logo:
        st.image(
            "https://www.unisba.ac.id/wp-content/uploads/2022/09/logo-unisba-300x300.png",
            width=140
        )
    with col_judul:
        st.title("UNIVERSITAS ISLAM BANDUNG")
        st.subheader("Fakultas Ekonomi dan Bisnis | Ekonomi Pembangunan")
        st.write("Tugas Kelompok: Aplikasi Pembelajaran Ekonomi Sumber Daya Hutan (Kalimantan Selatan)")

    st.markdown("---")
    st.subheader("ANGGOTA KELOMPOK")
    
    col_mhs1, col_mhs2, col_mhs3 = st.columns(3)
    with col_mhs1:
        st.info("**Ina Rani Amelia**\n\nNPM: 10090224002")
    with col_mhs2:
        st.info("**Nayla Dwi Safitri**\n\nNPM: 10090224013")
    with col_mhs3:
        st.info("**Celi Maulidi Aprilia**\n\nNPM: 10090224027")

    st.markdown("---")
    st.header("Teori Dasar Ekonomi Ekosistem Hutan")
    st.write("Pembelajaran berfokus pada pemahaman jenis jasa lingkungan berdasarkan literatur ekonomi sumber daya alam.")
    
    st.subheader("Klasifikasi Database Jasa Lingkungan")
    
    # Tabel Klasifikasi Jasa Lingkungan
    teori_data = {
        "Kategori Ekosistem": ["Provisioning", "Regulating", "Cultural", "Supporting"],
        "Definisi Singkat": [
            "Penyedia barang fisik langsung",
            "Pengatur proses alamiah bumi",
            "Manfaat rekreasi & spiritual",
            "Proses dasar kelangsungan hidup"
        ],
        "Contoh Data di Aplikasi": [
            "Kayu, hasil hutan bukan kayu, air",
            "Penyerapan karbon, penyerbukan lebah",
            "Ekowisata hutan tropis, estetika lanskap",
            "Siklus nutrisi tanah, fotosintesis"
        ],
        "Nilai Valuasi Finansial": [
            "Harga pasar komoditas",
            "Biaya pengganti (replacement cost)",
            "Travel cost method / WTP",
            "Valuasi tidak langsung"
        ]
    }
    df_teori = pd.DataFrame(teori_data)
    st.table(df_teori)
    
    st.subheader("Komposisi TEV Hutan Tropis Ideal")
    st.write("Sebagian besar nilai ekonomi hutan terletak pada jasa pengatur hidrologi dan karbon sebesar 45 persen. Nilai guna langsung seperti kayu komersial hanya menyumbang sekitar 25 persen dari total nilai ekonomi.")

# MODUL 1: KALKULATOR TEV
elif menu == "Modul 1: Kalkulator TEV":
    st.header("Modul 1: Kalkulator Total Economic Value (TEV)")
    st.write("Mengukur nilai guna langsung, tidak langsung, nilai pilihan, dan nilai eksistensi hutan Kalimantan Selatan secara kuantitatif.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Parameter Luas Lahan Hutan Kalsel (BPS)")
        luas_lindung = st.number_input("Luas Hutan Lindung (ha)", value=data_kalsel["Hutan Lindung"])
        luas_produksi = st.number_input("Luas Hutan Produksi Tetap (ha)", value=data_kalsel["Hutan Produksi Tetap"])
        luas_suaka = st.number_input("Luas Suaka Alam (ha)", value=data_kalsel["Suaka Alam & Pelestarian Alam"])
        
        total_luas = luas_lindung + luas_produksi + luas_suaka
        st.metric("Total Luas Lahan Terhitung (ha)", f"{total_luas:,.2f}")

    with col2:
        st.subheader("Panel Kalkulasi Nilai Ekonomi Non-Pasar")
        st.write("Nilasi dasar di bawah ini diambil langsung dari hasil penelitian untuk wilayah Kalimantan Selatan.")
        
        val_kayu = st.number_input("Nilai Ekonomi Kayu (Rp/tahun)", value=data_kalsel["Nilai Kayu"])
        val_karbon = st.number_input("Nilai Serapan Karbon (Rp/tahun)", value=data_kalsel["Nilai Karbon"])
        val_oksigen = st.number_input("Nilai Fungsi Oksigen (Rp/tahun)", value=data_kalsel["Nilai Oksigen"])
        
        # Perhitungan Total Nilai Ekonomi Terproyeksi
        total_tev = val_kayu + val_karbon + val_oksigen
        st.subheader("Hasil Proyeksi TEV")
        st.metric("Total Economic Value (Rp/Tahun)", f"Rp {total_tev:,.2f}")
        
    st.info("Kalkulator ini membuktikan bahwa nilai ekonomi hutan tidak hanya bersumber dari kayu yang ditebang, melainkan dari fungsi regulasi lingkungan yang dihasilkannya.")

# MODUL 2: ANALISIS TRADE-OFF
elif menu == "Modul 2: Analisis Trade-off":
    st.header("Modul 2: Simulasi Trade-off Lahan")
    st.write("Simulasi perbandingan ekonomi antara konversi lahan hutan menjadi kawasan eksploitasi vs mempertahankan hutan lestari.")
    
    st.subheader("Perbandingan Nilai Bersih Lahan")
    st.write("Jika pembuat kebijakan hanya menghitung hasil kayu komersial atau konversi lahan pertanian short-term, fungsi hutan tampak kecil. Perhitungan TEV mengubah indikator tersebut.")
    
    # Standar nilai berdasarkan data ekonomi riil yang diolah
    nilai_kayu_saja = data_kalsel["Nilai Kayu"]
    nilai_konversi_pertanian = data_kalsel["Nilai Kayu"] * 1.5
    nilai_hutan_lestari_tev = data_kalsel["Nilai Kayu"] + data_kalsel["Nilai Karbon"] + data_kalsel["Nilai Oksigen"]
    
    chart_data = pd.DataFrame({
        "Skenario Pengelolaan Lahan": ["Hasil Kayu Saja", "Konversi Pertanian/Tambang", "Hutan Lestari (TEV)"],
        "Nilai Proyeksi Ekonomi (Rp)": [nilai_kayu_saja, nilai_konversi_pertanian, nilai_hutan_lestari_tev]
    })
    
    st.bar_chart(data=chart_data, x="Skenario Pengelolaan Lahan", y="Nilai Proyeksi Ekonomi (Rp)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Sisi Eksploitasi Lahan**")
        st.write("Menghasilkan aliran kas pasar yang cepat secara jangka pendek melalui alih fungsi lahan. Namun skenario ini mengabaikan eksternalitas negatif jangka panjang seperti bencana banjir dan hilangnya habitat.")
    with col2:
        st.markdown("**Sisi Konservasi Berkelanjutan**")
        st.write("Menghasilkan laba bersih sosial jangka panjang yang jauh lebih besar. Skenario mempertahankan hutan menjamin keberadaan perlindungan hidrologis, penyerapan karbon, dan keanekaragaman hayati.")

# MODUL 3: KEBIJAKAN PES
elif menu == "Modul 3: Kebijakan PES":
    st.header("Modul 3: Kebijakan Payment for Ecosystem Services (PES)")
    st.write("Simulasi instrumen pasar karbon dan pembayaran jasa air bersih untuk menjaga kelestarian ekosistem.")
    
    st.
