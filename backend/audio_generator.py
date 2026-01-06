from gtts import gTTS
import os

def generate_audio(text, output_dir="output/audio", language="en"):
    """
    Generate a single audio file from text using gTTS.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # File name
    output_file = os.path.join(output_dir, "audiobook.mp3")
    
    # Create TTS object
    tts = gTTS(text=text, lang=language)
    
    # Save directly to a single MP3
    tts.save(output_file)
    
    # Return list for compatibility with Streamlit code
    return [output_file]
