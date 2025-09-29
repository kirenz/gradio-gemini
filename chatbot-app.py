import gradio as gr
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()


def generate_reply(message, history):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message
    )
    return response.text


gr.ChatInterface(
    fn=generate_reply,
    title="Gemini Chatbot",
    description="Stelle Fragen an das Gemini-Modell.",
    type="messages",
).launch()
