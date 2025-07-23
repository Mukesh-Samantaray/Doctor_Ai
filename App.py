# Streamlit_App.py
import streamlit as st
from patient import record_voice_to_text
from doctor import text_to_speech, stop_speech
from Brain import get_brain_response
# from PIL import Image

st.set_page_config(page_title="🧠 Doctor Ai", layout="centered")
st.title("🧠 Doctor Ai")

st.sidebar.header("User Options")
input_mode = st.sidebar.radio("Choose Input Type", ["Text", "Voice"])

uploaded_image = st.file_uploader("📤 Upload Medical Image (JPEG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", width=300)
    with open("download.jpeg", "wb") as f:
        f.write(uploaded_image.read())

    st.success("✅ Image uploaded and saved successfully.")

    if input_mode == "Text":
        user_question = st.text_input("💬 Ask your question about the image")
        if st.button("Submit Question") and user_question:
            with st.spinner("Generating response..."):
                ai_response = get_brain_response(user_question)
            st.markdown(f"**🩺 Doctor's Text Response:** {ai_response}")
            text_to_speech(ai_response)
            if st.button("🔇 Stop Audio"):
                stop_speech()

    elif input_mode == "Voice":
        record_button = st.button("🎙️ Record Voice")
        if record_button:
            with st.spinner("Listening..."):
                user_question = record_voice_to_text()
            st.markdown(f"**🗣️ You said:** {user_question}")
            with st.spinner("Generating response..."):
                ai_response = get_brain_response(user_question)
            st.markdown(f"**🩺 Doctor's Text Response:** {ai_response}")
            text_to_speech(ai_response)
            if st.button("🔇 Stop Audio"):
                stop_speech()
