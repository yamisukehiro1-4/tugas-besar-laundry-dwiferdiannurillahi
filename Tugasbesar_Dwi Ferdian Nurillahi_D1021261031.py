
import streamlit as st

# ==========================================
# APLIKASI LAUNDRY KILOAN
# DESAIN DARK BLUE ANIME
# ==========================================

st.set_page_config(
    page_title="NIGHTWASH | Laundry Kiloan",
    page_icon="🧺",
    layout="wide"
)

# ==========================================
# CSS DESAIN
# ==========================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #080f1e, #101d33, #0b1425);
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* HEADER */

.hero {
    background: linear-gradient(120deg, #101e36, #174b83);
    padding: 35px;
    border-radius: 22px;
    border: 1px solid #2875c7;
    box-shadow: 0 8px 30px #00000055;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 5px;
}

.hero p {
    color: #a9d4ff;
    font-size: 15px;
}

/* KARTU */

.card {
    background: linear-gradient(145deg, #17263d, #101b2d);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #294b72;
    box-shadow: 0 6px 20px #00000030;
    margin-bottom: 20px;
}

/* JUDUL */

h2, h3 {
    color: #d8eaff !important;
}

/* INPUT */

.stTextInput label,
.stNumberInput label {
    color: #d8eaff !important;
    font-weight: 600;
}

.stTextInput input,
.stNumberInput input {
    background-color: #0c1729 !important;
    color: white !important;
    border: 1px solid #367fc5 !important;
    border-radius: 10px !important;
}

/* TOMBOL */

div.stButton > button {
    background: linear-gradient(100deg, #1769bd, #258fe8);
    color: white;
    border: none;
    border-radius: 11px;
    height: 48px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    background: linear-gradient(100deg, #258fe8, #45aaff);
    color: white;
    border: 1px solid #80c7ff;
}

/* METRIC */

[data-testid="stMetric"] {
    background: #0c192c;
    padding: 16px;
    border-radius: 13px;
    border: 1px solid #28517c;
}

[data-testid="stMetricLabel"] {
    color: #a9c9e9 !important;
}

[data-testid="stMetricValue"] {
    color: #55b5ff !important;
}

/* TOTAL BAYAR */

.total-box {
    background: linear-gradient(120deg, #07519b, #087fc7);
    border: 1px solid #62baff;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 5px 25px #087fc755;
}

.total-box h3 {
    color: #dceeff !important;
}

.total-box h1 {
    color: white;
    font-size: 43px;
    font-weight: 900;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #7294b9;
    padding: 25px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# FUNGSI PERHITUNGAN
# ==========================================

def rupiah(nilai):
    return "Rp " + f"{nilai:,.0f}".replace(",", ".")


def hitung_biaya(nim, berat):

    tarif = 5000 + (int(nim[-1]) * 500)

    jumlah_genap = sum(
        1 for angka in nim
        if int(angka) % 2 == 0
    )

    diskon = jumlah_genap

    biaya_normal = berat * tarif

    potongan = biaya_normal * diskon / 100

    total = biaya_normal - potongan

    return (
        tarif,
        jumlah_genap,
        diskon,
        biaya_normal,
        potongan,
        total
    )


# ==========================================
# HEADER APLIKASI
# ==========================================

st.markdown("""
<div class="hero">

    <h1>🌙 NIGHTWASH</h1>

    <h3>LAUNDRY KILOAN</h3>

    <p>
        PREMIUM LAUNDRY SERVICE
        <br>
        Bersih maksimal, praktis, dan terpercaya.
    </p>

    <p>⚡ SMART CALCULATION SYSTEM</p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# ILUSTRASI ANIME
# ==========================================

st.markdown("""
<div style="
background:linear-gradient(100deg,#101e36,#183b63);
border:1px solid #2869a5;
border-radius:18px;
padding:18px;
text-align:center;
margin-bottom:22px;
">

<div style="font-size:65px;">🧥 🧺 🌌</div>

<h3 style="color:#69baff;">
NIGHTWASH LAUNDRY
</h3>

<p style="color:#b5d9ff;">
Your Clothes, Our Priority.
</p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "hasil" not in st.session_state:
    st.session_state.hasil = None

if "error" not in st.session_state:
    st.session_state.error = ""

if "nim_input" not in st.session_state:
    st.session_state.nim_input = ""

if "berat_input" not in st.session_state:
    st.session_state.berat_input = 1


def reset_data():
    st.session_state.nim_input = ""
    st.session_state.berat_input = 1
    st.session_state.hasil = None
    st.session_state.error = ""


# ==========================================
# FORM INPUT
# ==========================================

st.markdown("""
<div class="card">
<h3>👤 DATA PELANGGAN</h3>
<p style="color:#9fc8ee;">
Masukkan identitas dan berat cucian Anda.
</p>
</div>
""", unsafe_allow_html=True)

nim = st.text_input(
    "NIM (10 Digit Angka)",
    max_chars=10,
    placeholder="Contoh: 2411001347",
    key="nim_input"
)

berat = st.number_input(
    "Berat Cucian (kg)",
    min_value=0,
    step=1,
    key="berat_input"
)

col1, col2 = st.columns(2)

with col1:
    tombol_hitung = st.button(
        "⚡ HITUNG BIAYA",
        use_container_width=True
    )

with col2:
    st.button(
        "↻ RESET",
        on_click=reset_data,
        use_container_width=True
    )


# ==========================================
# VALIDASI DAN PROSES
# ==========================================

if tombol_hitung:

    st.session_state.hasil = None
    st.session_state.error = ""

    if len(nim) != 10 or not nim.isdigit():

        st.session_state.error = (
            "NIM tidak valid! Harus tepat 10 digit angka."
        )

    elif berat <= 0 or not float(berat).is_integer():

        st.session_state.error = (
            "Berat cucian harus bilangan bulat lebih dari 0 kg!"
        )

    else:

        hasil = hitung_biaya(nim, int(berat))

        st.session_state.hasil = (
            nim,
            int(berat),
            hasil
        )


# ==========================================
# PESAN ERROR
# ==========================================

if st.session_state.error:
    st.error(st.session_state.error)


# ==========================================
# HASIL PERHITUNGAN
# ==========================================

if st.session_state.hasil:

    nim_hasil, berat_hasil, data = (
        st.session_state.hasil
    )

    tarif, jumlah_genap, diskon, normal, potongan, total = data

    st.markdown("---")

    st.markdown("""
    <div class="card">
        <h3>📊 RINCIAN PERHITUNGAN</h3>
        <p style="color:#9fc8ee;">
        Hasil perhitungan biaya laundry pelanggan.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("**NIM:**", nim_hasil)
    st.write("**Berat Cucian:**", berat_hasil, "kg")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "💰 Tarif per kg",
            rupiah(tarif)
        )

        st.metric(
            "📦 Biaya Normal",
            rupiah(normal)
        )

        st.metric(
            "🔢 Jumlah Digit Genap",
            f"{jumlah_genap} digit"
        )

    with col2:

        st.metric(
            "🏷️ Persen Diskon",
            f"{diskon}%"
        )

        st.metric(
            "✂️ Potongan",
            rupiah(potongan)
        )

    st.markdown(f"""
    <div class="total-box">

        <h3>💎 TOTAL PEMBAYARAN</h3>

        <h1>{rupiah(total)}</h1>

        <p style="color:#d9efff;">
        Terima kasih telah menggunakan NIGHTWASH.
        </p>

    </div>
    """, unsafe_allow_html=True)


# ==========================================
# INFORMASI RUMUS
# ==========================================

with st.expander("📖 LIHAT RUMUS PERHITUNGAN"):

    st.write(
        "Tarif per kg = Rp5.000 + (digit terakhir NIM × Rp500)"
    )

    st.write(
        "Diskon = jumlah digit genap dalam NIM × 1%"
    )

    st.write(
        "Biaya normal = berat cucian × tarif per kg"
    )

    st.write(
        "Potongan = persentase diskon × biaya normal"
    )

    st.write(
        "Total bayar = biaya normal − potongan"
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">

    <h3 style="color:#58aaff;">
    🌙 NIGHTWASH LAUNDRY
    </h3>

    PYTHON & STREAMLIT PROJECT

    <br><br>

    © 2026 | Premium Laundry Calculation System

</div>
""", unsafe_allow_html=True)
