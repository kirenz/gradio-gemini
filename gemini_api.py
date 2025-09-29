"""Minimal Gemini API example to verify your environment configuration."""

from google import genai
from dotenv import load_dotenv

# Load API credentials from a local .env file (e.g., GOOGLE_API_KEY).
load_dotenv()

# Instantiate the Gemini client once and send a quick hello prompt.
client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Hello, how are you",
)

print(response.text)
