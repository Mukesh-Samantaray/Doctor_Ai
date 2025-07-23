import google.generativeai as genai
from dotenv import load_dotenv
import os

# Configure API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def get_brain_response(question, image_bytes):
    try:
        prompt = (
            "You are a helpful doctor. Answer clearly based on the image and question."
        )
        response = model.generate_content([
            {"text": prompt},
            {"text": question},
            {
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_bytes
                }
            }
        ])
        return response.text
    except Exception as e:
        print(f"❌ Gemini Error: {e}")
        return "Sorry, could not generate a response."
