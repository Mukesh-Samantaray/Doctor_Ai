import speech_recognition as sr
import datetime

def record_voice_to_text(save_audio=True):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Recording started... Speak now.")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        print("🔇 Recording stopped.")

    try:
        if save_audio:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"patient_voice_{timestamp}.wav"
            with open(filename, "wb") as f:
                f.write(audio.get_wav_data())
            print(f"💾 Audio saved as: {filename}")

        text = recognizer.recognize_google(audio)
        print("🗣️ Recognized Speech:", text)
        return text

    except sr.UnknownValueError:
        return "Sorry, I could not understand your voice."
    except sr.RequestError:
        return "Sorry, the speech recognition service is not available."
