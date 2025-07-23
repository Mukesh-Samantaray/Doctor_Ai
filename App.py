import streamlit as st
from Brain import get_brain_response
from doctor import text_to_speech_bytes

st.set_page_config(page_title="🩺 Doctor AI", layout="centered")
st.markdown("<h1 style='text-align: center;'>🩺 Doctor AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask questions about your uploaded medical image</p>", unsafe_allow_html=True)

# Use columns for cleaner layout
col1, col2 = st.columns([1, 2])

with col1:
    image = st.file_uploader("📷 Upload an image", type=["jpg", "jpeg", "png"])

with col2:
    question = st.text_input("💬 Your question:")

# Stylish submit button
submit = st.button("🚀 Submit", use_container_width=True)

if submit:
    if image and question:
        image_bytes = image.read()

        # Generate response
        with st.spinner("🧠 Thinking..."):
            ai_response = get_brain_response(question, image_bytes)
            audio_buffer = text_to_speech_bytes(ai_response)

        # Play audio immediately near top
        if audio_buffer:
            st.markdown("### 🔊 Doctor's Voice Response:")
            st.audio(audio_buffer, format="audio/mp3")
        else:
            st.error("❌ Failed to generate voice response.")

        # Show response and image side by side
        st.markdown("---")
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.markdown("### 📜 Doctor's Text Response:")
            st.write(ai_response)

        with col_img:
            st.image(image_bytes, caption="📸 Uploaded Image", width=250)
    else:
        st.warning("📍 Please upload an image and enter a question before submitting.")
