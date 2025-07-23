import os
import base64
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables and configure API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load image
image_path = "download.jpeg"
with open(image_path, "rb") as f:
    image_data = f.read()

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

def get_brain_response(question):
    try:
        # Combine prompt and image
        doctor_prompt = (
            "You are a medical imaging specialist. Based on the image provided, "
            "respond to the user's question in a clear, helpful, and medically sound manner."
        )

        response = model.generate_content([
            {"text": doctor_prompt},
            {"text": question},
            {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_data
                }
            }
        ])

        return response.text

    except Exception as e:
        print(f"❌ Error in generating response: {e}")
        return "🩺 Doctor's response: Sorry, there was an error processing your request."
