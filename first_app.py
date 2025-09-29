"""Introductory Gradio interface that collects a name and slider value."""

import gradio as gr


def greet(name, multiply):
    """Return a short greeting and repeat the exclamation mark."""
    return "Hello, " + name + "!" * int(multiply)


demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],  # Use built-in components for quick prototypes.
    outputs=["text"],
)

demo.launch()
