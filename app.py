import streamlit as st
import os

from backend.pdf_handler import extract_text_from_pdf
from backend.doc_handler import extract_text_from_docx
from backend.text_handler import extract_text_from_txt
from backend.audio_generator import generate_audio
from backend.text_cleaner import clean_text
from backend.llm_enrichment import enrich_text_with_gemini
st.set_page_config(page_title="Audio Book Generator")

st.title("📖 Audio Book Generator 1")
st.write("Upload PDF, DOCX, or TXT and convert it into an Audio Book")

uploaded_file = st.file_uploader(
    "Upload file",
    type=["pdf", "docx", "txt"]
)

language = st.selectbox(
    "Select Language",
    ["en", "hi", "te"]
)

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1].lower()

    if file_type == "pdf":
        raw_text = extract_text_from_pdf(uploaded_file)
    elif file_type == "docx":
        raw_text = extract_text_from_docx(uploaded_file)
    else:
        raw_text = extract_text_from_txt(uploaded_file)

    cleaned_text = clean_text(raw_text)

    st.subheader("📄 Extracted Text Preview")
    st.text_area(
        "Preview",
        cleaned_text[:3000],
        height=250
    )
    extra_instruction = """
Rewrite the following text to be engaging, lively, and conversational, 
as if it is being narrated in an audiobook. 
Use simpler sentences, emphasize important points, and make it enjoyable for listeners.
"""

    enrichment_placeholder = st.empty()
    enrichment_placeholder.text("Enriching with AI...")

    try:
        final_text = enrich_text_with_gemini(cleaned_text,extra_instruction)
    except Exception as e:
        st.error(f"AI enrichment failed: {e}")
        final_text = cleaned_text

    enrichment_placeholder.text("✅ Enrichment complete")


    st.text_area("Enriched Text Preview", final_text[:3000], height=250)

    if st.button("🎧 Generate Audio Book"):
        with st.spinner("Generating audio..."):
            audio_files = generate_audio(
                final_text,  # enriched and cleaned text
                output_dir="output/audio",
                language=language
            )
            
        st.success("Audio Book Generated Successfully!")

        for audio in audio_files:
            st.audio(audio)

        # Download button
        st.download_button(
            label="⬇️ Download Audio Book",
            data=open(audio_files[0], "rb").read(),
            file_name="audiobook.mp3",
            mime="audio/mpeg"
        )
