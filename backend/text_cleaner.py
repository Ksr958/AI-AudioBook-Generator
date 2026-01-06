import re

def clean_text(text: str) -> str:
    if not text:
        return ""

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove non-printable characters
    text = re.sub(r"[^\x20-\x7E]", " ", text)

    # Remove repeated punctuation
    text = re.sub(r"([.!?]){2,}", r"\1", text)

    return text.strip()
