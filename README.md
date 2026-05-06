
AI-Powered YouTube Content Generator

Script generation + voiceovers, fully automated

🐍 Python ⚡ Streamlit 🧠 LLaMA 3.1 🎙️ ElevenLabs

Features

✍️

One-click scripts

Generate engaging video scripts from any topic instantly.

🔊

Realistic voiceovers

Convert scripts to high-quality audio via ElevenLabs.

🖥️

Interactive UI

Clean Streamlit interface with inline audio playback.

Technologies

Streamlit

UI, input & audio playback

OpenRouter (LLaMA 3.1)

AI script generation

ElevenLabs API

Text-to-speech synthesis

Python + Transformers

Backend & model inference

Setup

1

Clone the repository

git clone https://github.com/<username>/ai-youtube-generator.git
cd ai-youtube-generator

2

Create & activate a virtual environment

python -m venv venv
venv\\Scripts\\activate   # Windows
source venv/bin/activate  # macOS/Linux

3

Install dependencies

pip install -r requirements.txt

4

Add your API keys

\# script.py
openai.api\_key = "your\_openrouter\_api\_key"

# text\_to\_speech.py
elevenlabs\_api\_key = "your\_elevenlabs\_api\_key"

5

Run the app

streamlit run app.py

Project Structure

📄

app.py

Streamlit app entry point

🧠

script.py

Script generation logic

🎙️

text\_to\_speech.py

ElevenLabs voiceover generation

📦

requirements.txt

Python dependencies

📝

script.txt

Generated script (runtime)

🔉

output.wav

Generated audio (runtime)

ℹ️

Runs entirely on **CPU** — no GPU required. Ideal for automation channels, Reels/Shorts, and educational content creators.
