# AI-Powered-Youtube-Content-Generator

This project allows users to automatically generate YouTube video scripts and voiceovers based on
any topic they provide.
It leverages state-of-the-art language models (LLaMA 3.1 via OpenRouter) for script generation and
for script generation and ElevenLabs API for text-to-speech synthesis.


Features:
- Generate engaging YouTube video scripts with one click
- Convert scripts into realistic voiceovers using ElevenLabs
- Convert scripts into realistic voiceovers
- Clean and interactive UI using Streamlit

 Technologies Used:
- Streamlit - UI for input, output, and audio playback
- OpenRouter (LLaMA 3.1 8B Instruct) - for AI-generated scripts
- ElevenLabs API – For high-quality text-to-speech voice generation
- Python - backend logic and orchestration
- Torch + Transformers - for model inference

  Getting Started
1. Clone the repository
bashgit clone https://github.com/<your-username>/ai-youtube-generator.git
cd ai-youtube-generator
2. Create and activate a virtual environment
bashpython -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3. Install dependencies
bashpip install -r requirements.txt
4. Configure your API keys
In script.py:
pythonopenai.api_key = "your_openrouter_api_key"
In text_to_speech.py:
pythonelevenlabs_api_key = "your_elevenlabs_api_key"
5. Run the app
bashstreamlit run app.py

📁 Project Structure
ai-youtube-generator/
├── app.py               # Streamlit application entry point
├── script.py            # Script generation logic (OpenRouter / LLaMA)
├── text_to_speech.py    # Voiceover generation (ElevenLabs API)
├── requirements.txt     # Python dependencies
├── script.txt           # Generated script output (runtime)
├── output.wav           # Generated audio output (runtime)
├── screenshots/         # UI screenshots
└── README.md            # Project documentation

📸 Screenshot
Show Image

Notes:
- This project runs entirely on CPU - no GPU required.
- Ideal for automation channels, reels/shorts, or educational content creators.


