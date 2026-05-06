# AI-Powered YouTube Content Generator

Automatically generate YouTube video scripts and voiceovers from any topic using state-of-the-art AI. This tool combines **LLaMA 3.1 via OpenRouter** for intelligent script generation with **ElevenLabs** for high-quality, realistic text-to-speech synthesis.

---

## Features

- Generate engaging YouTube video scripts with a single click
- Convert scripts into realistic voiceovers using the ElevenLabs API
- Clean and interactive UI built with Streamlit

---

## Technologies Used

| Component | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | UI for input, output, and audio playback |
| [OpenRouter](https://openrouter.ai) (LLaMA 3.1 8B Instruct) | AI-powered script generation |
| [ElevenLabs API](https://elevenlabs.io) | High-quality text-to-speech voice synthesis |
| Python | Backend logic and orchestration |
| Torch + Transformers | Model inference |

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-youtube-generator.git
cd ai-youtube-generator
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

In `script.py`, add your OpenRouter API key:

```python
openai.api_key = "your_openrouter_api_key"
```

In `text_to_speech.py`, add your ElevenLabs API key:

```python
elevenlabs_api_key = "your_elevenlabs_api_key"
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## Project Structure

```
ai-youtube-generator/
├── app.py                # Streamlit application entry point
├── script.py             # Script generation logic (OpenRouter / LLaMA)
├── text_to_speech.py     # Voiceover generation (ElevenLabs API)
├── requirements.txt      # Python dependencies
├── script.txt            # Generated script output (runtime)
├── output.wav            # Generated audio output (runtime)
├── screenshots/          # UI screenshots
└── README.md             # Project documentation
```

---

## Screenshots

### Streamlit App UI

![Streamlit UI](screenshots/Screenshot%202025-04-30%20210711.png)

---

## Notes

- Runs entirely on **CPU** — no GPU required.
- Well-suited for automation channels, Reels/Shorts creators, and educational content producers.
