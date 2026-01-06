import os
import google.genai as genai

# 1️⃣ Get API key from environment variable
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("API KEY NOT FOUND! Please set GENAI_API_KEY in your environment.")
    exit(1)

# 2️⃣ Initialize client with API key
client = genai.Client(api_key=api_key)
print("API KEY FOUND: True\n")

# 3️⃣ List all available models
print("Available models for text generation:")
all_models = client.models.list()  # Pager object

# Filter models for text generation (simple heuristic: ignore embedding/audio/image models)
text_models = [
    m for m in all_models
    if "embedding" not in m.name and "audio" not in m.name and "imagen" not in m.name
]

# Print first 5 valid models (optional)
for m in text_models[:5]:
    print(f"Name: {m.name}")
    print(f"Description: {m.description}")
    print("-" * 50)

if not text_models:
    print("No text generation capable models found!")
    exit(1)

# 4️⃣ Use the first valid text model
selected_model = text_models[0].name
print(f"\nUsing model: {selected_model}\n")

# 5️⃣ Generate content
prompt = "Explain what Python is in 2 lines."

response = client.models.generate_content(
    model=selected_model,
    contents=prompt
)

# 6️⃣ Print generated text
print("Generated content:")
print(response.text)
