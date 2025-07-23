# File: app.py

import gradio as gr
from Brain import get_brain_response
from Patient import record_voice_to_text
from Doctor import text_to_speech, stop_speech
from PIL import Image
import os

# Global variable to hold image
image_path = "download.jpeg"

def handle_text_input(text):
    response = get_brain_response(text)
    text_to_speech(response)
    return response, image_path

def handle_voice_input():
    question = record_voice_to_text()
    response = get_brain_response(question)
    text_to_speech(response)
    return response, image_path

def stop_audio():
    stop_speech()
    return "Speech Stopped."

with gr.Blocks() as demo:
    gr.Markdown("# 🩺 Doctor AI - Image-Based Voice Consultation")

    with gr.Row():
        with gr.Column():
            img_display = gr.Image(label="Uploaded Image", value=image_path, interactive=False, width=300)
            input_method = gr.Radio(["Text", "Voice"], label="Choose Input Method", value="Text")
            text_box = gr.Textbox(label="Enter Your Question")
            ask_button = gr.Button("Ask Doctor")
            voice_button = gr.Button("Record Voice")
            stop_button = gr.Button("Stop Speech")

        with gr.Column():
            response_output = gr.Textbox(label="Doctor's Response")
            image_preview = gr.Image(label="Diagnostic Image", value=image_path, interactive=False, width=300)

    ask_button.click(fn=handle_text_input, inputs=text_box, outputs=[response_output, image_preview])
    voice_button.click(fn=handle_voice_input, outputs=[response_output, image_preview])
    stop_button.click(fn=stop_audio, outputs=response_output)

demo.launch()
