# text_to_speech.py
import requests
import json

API_KEY = "YOUR API KEY"#GET API KEY FROM OPEN ROUTER
VOICE_ID = "EXAVITQu4vr4xnSDxMaL"

def generate_tts(text: str) -> str:
    # Your text-to-speech code here
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_turbo_v2",
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        audio_path = "output.wav"
        with open(audio_path, "wb") as f:
            f.write(response.content)
        return audio_path
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")
