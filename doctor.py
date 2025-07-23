import os
import pygame
from gtts import gTTS

# Global stop flag
is_speaking = False
audio_path = "temp_response.mp3"

def text_to_speech(response_text):
    global is_speaking, audio_path

    try:
        # Stop previous playback if running
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        # Delete previous file if exists and not in use
        if os.path.exists(audio_path):
            try:
                os.remove(audio_path)
            except PermissionError:
                print("⚠️ Could not delete old audio file. Retrying with new name.")
                audio_path = "temp_response_new.mp3"  # Now this updates the outer variable too

        # Generate new TTS audio
        tts = gTTS(text=response_text)
        tts.save(audio_path)

        # Initialize and play with pygame
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        is_speaking = True

        print("🩺 Doctor's response:", response_text)

    except Exception as e:
        print(f"❌ Error in text-to-speech: {e}")

def stop_speech():
    global is_speaking
    if is_speaking:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        is_speaking = False
