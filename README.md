# AI-Powered-Youtube-Content-Generator

This project allows users to automatically generate YouTube video scripts and voiceovers based on
any topic they provide.
It leverages state-of-the-art language models (LLaMA 3.1 via OpenRouter) for script generation and
Parler-TTS for text-to-speech synthesis.

Features:
- Generate engaging YouTube video scripts with one click
- Select from multiple voice styles (Friendly, Serious, Announcer, etc.)
- Convert scripts into realistic voiceovers
- Clean and interactive UI using Streamlit

 Technologies Used:
- Streamlit - UI for input, output, and audio playback
- OpenRouter (LLaMA 3.1 8B Instruct) - for AI-generated scripts
- Parler-TTS (Mini v1) - lightweight, CPU-friendly TTS
- Python - backend logic and orchestration
- Torch + Transformers - for model inference

  How to Set Up and Run:
1. Clone the repository:
 git clone https://github.com/<Ayushpatel77>/ai-youtube-generator.git
 cd ai-youtube-generator
2. Create and activate a virtual environment: 
  python -m venv venv
 venv\Scripts\activate # For Windows
3. Install the dependencies:
 pip install -r requirements.txt
4. Add your OpenRouter API key in script.py:
 openai.api_key = "your_openrouter_api_key"
5. Run the app:
 streamlit run app.py

Project Structure:
- app.py - Streamlit app
- script.py - Script generation logic
- text_to_speech.py - Parler-TTS voice generation
- requirements.txt - Required packages
- script.txt - Generated script (runtime)
- output.wav - Generated voice (runtime)
- README.md - Project documentation

Notes:
- This project runs entirely on CPU - no GPU required.
- Ideal for automation channels, reels/shorts, or educational content creators.


