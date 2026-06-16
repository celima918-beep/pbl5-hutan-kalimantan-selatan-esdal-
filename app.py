import streamlit as st
import pandas as pd

# Konfigurasi halaman utama aplikasi
st.set_page_config(
    page_title="Eco-Forest Valuation - Kalsel",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Panel Informasi Kelompok dan Logo Kampus pada bagian atas Sidebar
st.sidebar.image(
    "https://www.unisba.ac.id/wp-content/uploads/2022/09/logo-unisba-300x300.png",
    width=120
)
st.sidebar.markdown("### **UNIVERSITAS ISLAM BANDUNG**")
st.sidebar.markdown("**Fakultas Ekonomi dan Bisnis**")
st.sidebar.markdown("Program Studi Ekonomi Pembangunan")

st.sidebar.markdown("---")
st.sidebar.markdown("**ANGGOTA KELOMPOK:**")
st.sidebar.write("1. Ina Rani Amelia (10090224002)")
st.sidebar.write("2. Nayla Dwi Safitri (10090224013)")
st.sidebar.write("3. Celi Maulidi Aprilia (10090224027)")
st.sidebar.markdown("---")

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

# Navigasi menu utama berdasarkan rencana induk pilar aplikasi
st.sidebar.title("Eco-Forest Valuation")
st.sidebar.write("Aplikasi Pembelajaran Ekonomi Sumber Daya Hutan")
st.sidebar.write("Referensi Teoretis: Tietenberg & Lewis Chapter 13")

menu = st.sidebar.radio(
    "Pilih Modul Pembelajaran:",
    ["Fase 1: Teori Dasar", "Modul 1: Kalkulator TEV", "Modul 2: Analisis Trade-off", "Modul 3: Kebijakan PES", "Modul 4: Kasus Interaktif"]
)

# Tampilan Alur Belajar Pengguna pada Sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("Rencana Alur Belajar")
st.sidebar.caption("Fase 1: Teori -> Fase 2: Valuasi -> Fase 3: Simulasi -> Fase 4: Evaluasi")

# FASE 1: TEORI DASAR
if menu == "Fase 1: Teori Dasar":
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
    
    st.subheader("Simulasi Kompensasi Finansial Finansial")
    st.write("Gerakkan slider untuk menentukan besaran nilai insentif karbon yang diberikan kepada masyarakat sekitar hutan guna menghentikan laju degradasi hutan lahan Kalimantan Selatan.")
    
    insentif_input = st.slider("Besaran Insentif Karbon Tambahan (Rupiah/Hektar)", 0, 5000000, 1500000)
    
    # Menghitung titik keseimbangan sederhana penahanan deforestasi
    laju_deforestasi_awal = 4.5
    efek_penurunan = (insentif_input / 5000000) * 4.0
    laju_deforestasi_akhir = max(0.5, laju_deforestasi_awal - efek_penurunan)
    
    st.metric(label="Estimasi Laju Deforestasi Sisa (% Per Tahun)", value=f"{laju_deforestasi_akhir:.2f} %")
    
    if laju_deforestasi_akhir < 1.5:
        st.success("Titik keseimbangan tercapai. Kompensasi finansial berhasil menghentikan mayoritas aktivitas alih fungsi lahan secara liar.")
    else:
        st.warning("Nilai kompensasi finansial belum cukup kuat untuk menghentikan aktivitas alih fungsi lahan oleh komunitas lokal.")

# MODUL 4: KASUS INTERAKTIF
elif menu == "Modul 4: Kasus Interaktif":
    st.header("Modul 4: Eksplorasi Kasus Riil")
    st.write("Analisis kasus nyata pengelolaan ekosistem hutan berdasarkan prinsip ekonomi lingkungan.")
    
    pilihan_kasus = st.selectbox(
        "Pilih Studi Kasus Ekosistem:",
        ["Nilai Serapan Karbon Hutan Produksi", "Peran Ekologis Lebah dalam Penyerbukan", "Fungsi Proteksi Hidrologis Hutan Lindung Kalsel"]
    )
    
    if pilihan_kasus == "Nilai Serapan Karbon Hutan Produksi":
        st.write("Hutan Produksi Tetap Kalimantan Selatan seluas 394.563,75 hektar memiliki peran ganda. Selain memproduksi kayu bulat sebesar 477.250,17 meter kubik, kawasan ini berperan sebagai carbon sink yang menahan pelepasan emisi ke atmosfer.")
    elif pilihan_kasus == "Peran Ekologis Lebah dalam Penyerbukan":
        st.write("Lebah hutan menyediakan jasa pengatur (regulating services) yang menjaga keberlangsungan reproduksi tanaman hutan. Nilai ekonomi dihitung menggunakan metode biaya pengganti (replacement cost) jika proses penyerbukan harus digantikan teknologi buatan manusia.")
    elif pilihan_kasus == "Fungsi Proteksi Hidrologis Hutan Lindung Kalsel":
        st.write("With luas mencapai 308.221,52 hektar, kawasan Hutan Lindung Kalimantan Selatan bertindak sebagai penyimpan air tanah alami. Keberadaan ekosistem ini meminimalkan pengeluaran biaya infrastruktur pengendali banjir di hilir.")
