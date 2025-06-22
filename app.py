import streamlit as st

st.title("AI Rekomendasi Aktivitas Harian 🌤")

mood = st.selectbox("Bagaimana mood kamu hari ini?", ["Senang", "Sedih", "Lelah", "Stres"])
cuaca = st.selectbox("Bagaimana cuaca di tempatmu?", ["Cerah", "Hujan", "Berawan"])
waktu = st.selectbox("Sekarang jam berapa?", ["Pagi", "Siang", "Sore", "Malam"])

def rekomendasi_aktivitas(mood, cuaca, waktu):
    if mood == "Lelah" and cuaca == "Hujan" and waktu == "Malam":
        return "Rebahan sambil nonton film dan minum coklat hangat ☕🎬"
    elif mood == "Senang" and cuaca == "Cerah":
        return "Keluar rumah, jalan santai atau ngopi bareng teman ☕🚶‍♂"
    elif mood == "Stres":
        return "Coba meditasi ringan atau dengarkan musik menenangkan 🎧🧘"
    elif mood == "Sedih":
        return "Tulis jurnal atau hubungi teman dekat untuk ngobrol 💌"
    else:
        return "Lakukan aktivitas ringan yang bikin nyaman seperti baca buku atau tidur siang 📖😴"

if st.button("Dapatkan Rekomendasi"):
    hasil = rekomendasi_aktivitas(mood, cuaca, waktu)
    st.success(f"Rekomendasi Aktivitas: {hasil}")