# Gradio + Gemini Learning Guide

Following the steps below will get you ready to run the examples and experiment on your own.

## Setup
- Clone this repository:
  ```bash
  git clone https://github.com/<your-account>/gradio-gemini.git
  cd gradio-gemini
  ```
- Install the dependencies with `uv` (this also creates the virtual environment if needed):
  ```bash
  uv sync
  ```

## gemini_api.py — Verify Your Gemini Setup
- Loads a Gemini client and sends a single test prompt.
- Requires a `.env` file created with your key from [Google AI Studio](https://aistudio.google.com/). For example:
  ```bash
  echo "GOOGLE_API_KEY=your-api-key" >> .env
  ```
- Run the script with:
  ```bash
  uv run python gemini_api.py
  ```

## first_app.py — Your First Gradio Interface
- Introduces `gr.Interface` with one text input and a slider.
- Demonstrates how Gradio components map to a Python function.
- Launch it locally with:
  ```bash
  uv run python first_app.py
  ```

## chatbot_random.py — Prototype Chatbot Logic
- Shows `gr.ChatInterface` using a placeholder function that returns random answers.
- Focus on understanding the `message` and `history` arguments passed to the callback.
- Start the demo with:
  ```bash
  uv run python chatbot_random.py
  ```


## chatbot_simple.py — Connect Gradio to Gemini
- Calls Gemini for every user message while presenting a full chat UI.
- Reuses the API key loaded in `gemini_api.py`, so ensure your `.env` file is in place.
- Launch the fully featured chatbot with:
  ```bash
  uv run python chatbot_simple.py
  ```


## chatbot_history.py — Add Simple Memory
- Switches `gr.ChatInterface` to `type="messages"` so Gradio supplies the entire chat transcript.
- Concatenates the roles and text from each turn before sending the prompt to Gemini, giving it conversation memory.
- Launch it with:
  ```bash
  uv run python chatbot_history.py
  ```
