import streamlit as st

st.set_page_config(
    page_title="Laundry Kiloan",
    page_icon="🧺",
    layout="centered"
)

# -------------------- DESAIN / CSS --------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef5ff 0%, #f8fbff 55%, #edf8f2 100%);
}
.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.hero {
    background: linear-gradient(120deg, #103b78, #1676c5);
    padding: 28px;
    border-radius: 18px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 8px 22px rgba(16, 59, 120, .18);
}
.hero h1 { color: white; margin: 0; }
.hero p { color: #e3efff; margin-bottom: 0; }
.section-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #dce8f5;
    box-shadow: 0 4px 14px rgba(20, 55, 90, .06);
    margin-bottom: 16px;
}
.result-card {
    background: #e5f7e9;
    border: 1px solid #b8e6c2;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
}
.result-label {
    color: #24643a;
    font-size: 14px;
    font-weight: 600;
}
.result-value {
    color: #14532d;
    font-size: 30px;
    font-weight: 800;
}
div.stButton > button {
    border-radius: 10px;
    min-height: 45px;
    font-weight: 700;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# -------------------- FUNGSI --------------------
def rupiah(nilai):
    return "Rp " + f"{nilai:,.0f}".replace(",", ".")


def hitung_biaya(nim, berat):
    tarif = 5000 + int(nim[-1]) * 500
    jumlah_genap = sum(int(angka) % 2 == 0 for angka in nim)
    diskon = jumlah_genap
    biaya_normal = berat * tarif
    potongan = biaya_normal * diskon / 100
    total = biaya_normal - potongan

    return tarif, jumlah_genap, diskon, biaya_normal, potongan, total


# -------------------- HEADER --------------------
st.markdown("""
<div class="hero">
    <h1>🧺 LAUNDRY KILOAN</h1>
    <p>Aplikasi perhitungan biaya laundry yang mudah, cepat, dan praktis.</p>
</div>
""", unsafe_allow_html=True)

# Inisialisasi nilai form
if "hasil_laundry" not in st.session_state:
    st.session_state.hasil_laundry = None
if "error_laundry" not in st.session_state:
    st.session_state.error_laundry = ""

# -------------------- FORM INPUT --------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("📝 Data Pelanggan")

with st.form("form_laundry"):
    nim = st.text_input(
        "NIM (10 digit angka)",
        max_chars=10,
        placeholder="Contoh: 2411001347"
    )
    berat = st.number_input(
        "Berat cucian (kg)",
        min_value=0,
        step=1,
        value=1
    )

    col1, col2 = st.columns(2)
    with col1:
        hitung = st.form_submit_button("🧮 Hitung Biaya", use_container_width=True)
    with col2:
        reset = st.form_submit_button("↩️ Reset", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if reset:
    st.session_state.hasil_laundry = None
    st.session_state.error_laundry = ""
    st.rerun()

if hitung:
    st.session_state.hasil_laundry = None
    st.session_state.error_laundry = ""

    if len(nim) != 10 or not nim.isdigit():
        st.session_state.error_laundry = "NIM harus terdiri dari tepat 10 digit angka."
    elif berat <= 0:
        st.session_state.error_laundry = "Berat cucian harus berupa bilangan bulat lebih dari 0 kg."
    else:
        st.session_state.hasil_laundry = (nim, int(berat), hitung_biaya(nim, int(berat)))

if st.session_state.error_laundry:
    st.error(st.session_state.error_laundry)

# -------------------- HASIL --------------------
if st.session_state.hasil_laundry:
    nim_hasil, berat_hasil, data = st.session_state.hasil_laundry
    tarif, jumlah_genap, diskon, normal, potongan, total = data

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("📊 Rincian Perhitungan")
    st.caption(f"NIM: {nim_hasil}  |  Berat cucian: {berat_hasil} kg")

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Tarif per kg", rupiah(tarif))
        st.metric("Biaya normal", rupiah(normal))
        st.metric("Jumlah digit genap", f"{jumlah_genap} digit")
    with c2:
        st.metric("Persen diskon", f"{diskon}%")
        st.metric("Potongan", rupiah(potongan))

    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">TOTAL YANG HARUS DIBAYAR</div>
        <div class="result-value">{rupiah(total)}</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- KETERANGAN --------------------
with st.expander("ℹ️ Lihat rumus perhitungan"):
    st.write("Tarif per kg = Rp5.000 + (digit terakhir NIM × Rp500)")
    st.write("Diskon = jumlah digit genap pada NIM × 1%")
    st.write("Biaya normal = berat cucian × tarif per kg")
    st.write("Potongan = persentase diskon × biaya normal")
    st.write("Total bayar = biaya normal − potongan")

st.caption("Tugas Besar Python dan Streamlit | Aplikasi Laundry Kiloan")
