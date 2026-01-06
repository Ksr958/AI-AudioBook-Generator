import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found. Please set it in .env")

# Initialize the client once
client = genai.Client(api_key=API_KEY)

# Choose a stable text generation model
MODEL_NAME = "models/gemini-2.5-flash"

def enrich_text_with_gemini(text, instruction=""):
    """
    Enriches the input text using Google Gemini LLM.
    
    Args:
        text (str): Original text to enrich.
        instruction (str): Extra instructions to guide enrichment.

    Returns:
        str: Enriched text.
    """
    # Combine instruction and original text
    prompt = f"{instruction}\n\n{text}"

    # Generate enriched content
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text
