from gtts import gTTS
import io

def text_to_speech_bytes(response_text):
    try:
        # Generate TTS in memory
        tts = gTTS(text=response_text)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        return mp3_fp
    except Exception as e:
        print(f"❌ TTS Error: {e}")
        return None
