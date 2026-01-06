# 🎧 AI Audio Book Generator

An **AI-powered Audio Book Generator** that transforms text-based documents into **natural-sounding audio** using **Generative AI** and **Text-to-Speech technology**.  
The application supports multiple document formats and provides a simple, interactive web interface built with **Streamlit**.

---

## Features

- Upload documents in **PDF, DOCX, or TXT** format  
- AI-driven text enhancement using **Google Gemini API**  
- Convert enriched text into **high-quality audio**  
- Download generated audio files instantly  
- Clean and user-friendly **Streamlit web interface**  
- Secure API key management using **environment variables**

---

## Tech Stack

- **Frontend & Backend**: Streamlit (Python)  
- **Generative AI**: Google Gemini API  
- **Document Processing**: PyPDF, python-docx  
- **Text-to-Speech**: gTTS  
- **Version Control**: Git & GitHub  
- **Deployment**: Streamlit Community Cloud  

---

## ⚙️ Installation & Setup (Local)

### Clone the Repository
```bash
git clone https://github.com/Ksr958/AI-AudioBook-Generator.git
cd AI-AudioBook-Generator
Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

Install Dependencies
pip install -r requirements.txt

Configure Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Run the Application
streamlit run app.py

