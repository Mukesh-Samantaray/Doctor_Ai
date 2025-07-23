from patient import record_voice_to_text
from Brain import get_brain_response
from doctor import text_to_speech

def run_pipeline(input):
    question_text = record_voice_to_text()

    if not question_text:
        print("❌ Could not process patient's voice. Exiting pipeline.")
        return

    print("🤖 Sending data to Doctor AI...")
    response_text = get_brain_response(question_text)

    if not response_text:
        print("❌ No response from Doctor AI. Exiting pipeline.")
        return

    text_to_speech(response_text)

if __name__ == "__main__":
    run_pipeline()
