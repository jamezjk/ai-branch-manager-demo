import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Branch Manager", layout="centered")

st.title("🧠 AI Branch Manager – Video-Based Loan Assistance")
st.markdown("Upload your KYC video. We'll analyze and tell if you're eligible for a loan.")

uploaded_file = st.file_uploader("📤 Upload your KYC video (.mp4/.mov)", type=["mp4", "mov"])

if uploaded_file:
    st.video(uploaded_file)

    st.markdown("---")
    st.subheader("🧍 Detected Face Snapshot")
    face_img = Image.open("sample_face.jpg")  # Use any face image from your project folder
    st.image(face_img, caption="Customer Face", use_column_width=True)

    st.subheader("🗣️ Transcribed Speech")
    st.code("Hello, I'm interested in applying for a home loan. My monthly salary is ₹80,000.", language="text")

    st.subheader("📊 Loan Eligibility Result")
    st.success("✅ Eligible for ₹25 Lakhs @ 8.5% interest rate")

    st.markdown("---")
    st.caption("🔐 This is a demo version. No actual video processing is done.")
else:
    st.info("Please upload a KYC video file to start.")
