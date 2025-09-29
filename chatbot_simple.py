"""Gradio chatbot that streams user prompts to the Gemini API."""

import gradio as gr
from google import genai
from dotenv import load_dotenv

# Load environment variables so the Google API key is available at runtime.
load_dotenv()

# Set up the Gemini client once; Gradio will reuse the same instance.
client = genai.Client()


def generate_reply(message, history):
    """Forward the latest user message to Gemini and return the text reply."""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message,
    )
    return response.text


chatbot = gr.ChatInterface(
    fn=generate_reply,
    title="Gemini Chatbot",
    description="Ask questions and Gemini will respond in real time.",
    type="messages",  # Provide the full conversation for richer responses.
)


chatbot.launch()
