"""Toy Gradio chatbot that ignores context and returns random replies."""

import random
import gradio as gr


def random_response(message: str, history: list) -> str:
    """Pick a random yes/no answer regardless of the prompt."""
    return random.choice(["Yes", "No"])


chatbot = gr.ChatInterface(
    fn=random_response,
    type="messages",  # Pass messages as a list of role/content dicts.
)


if __name__ == "__main__":
    chatbot.launch()
