"""Gemini-powered Gradio chatbot that remembers previous user inputs."""

from collections.abc import Iterable

import gradio as gr
from google import genai
from dotenv import load_dotenv

# Ensure the Google API key is available for the Gemini client.
load_dotenv()

client = genai.Client()


def _to_text(content):
    """Normalize Gradio message content into a plain string."""
    if isinstance(content, str):
        return content
    if isinstance(content, Iterable):
        parts = []
        for part in content:
            text = part.get("text") if isinstance(part, dict) else None
            if text:
                parts.append(text)
        return "\n".join(parts)
    return ""


def remember(message, history):
    """Send the full conversation to Gemini and return its reply."""
    conversation = history + [{"role": "user", "content": message}]
    contents = []
    for entry in conversation:
        contents.append(
            {
                "role": entry.get("role", "user"),
                "parts": [{"text": _to_text(entry.get("content", ""))}],
            }
        )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents,
    )
    return response.text


chatbot = gr.ChatInterface(
    fn=remember,
    title="Chatbot with Memory",
    description="Gemini replies while keeping the full conversation context.",
    type="messages",
)


chatbot.launch()
