import sys
import torch
from transformers import AutoProcessor
from parler_tts import ParlerTTSForConditionalGeneration
import soundfile as sf

def synthesize_from_text(script: str, style_input: str = "Default") -> str:
    # Define style prompts
    style_prompts = {
        "Serious":   "Speak in a serious and authoritative tone. ",
        "Friendly":  "Speak in a casual and friendly tone. ",
        "Aggressive":"Speak in an aggressive and commanding voice. ",
        "Announcer": "Speak like a professional announcer. ",
        "Default":   ""
    }
    prompt = style_prompts.get(style_input, "") + script

    # Load model & processor (cache these globally in real use)
    processor = AutoProcessor.from_pretrained("parler-tts/parler-tts-mini-v1")
    model     = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-v1").to("cpu")

    # Tokenize & generate
    inputs = processor(text=prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs)

    # Save audio
    audio_arr = output.cpu().squeeze().numpy()
    output_path = "output.wav"
    sf.write(output_path, audio_arr, samplerate=model.config.sampling_rate)
    return output_path

