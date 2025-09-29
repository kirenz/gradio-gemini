from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# Only run this block for Gemini Developer API
client = genai.Client()

MODEL_ID = 'gemini-2.0-flash'

response_1 = client.models.generate_content(
    model=MODEL_ID,
    contents='Hello, how are you',
)

print(response_1)


