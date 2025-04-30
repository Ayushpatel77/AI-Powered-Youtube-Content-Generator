
import streamlit as st
from script import generate_youtube_script   # your OpenRouter script generator
from script import save_script_to_file
from text_to_speech import synthesize_from_text

st.set_page_config(page_title="🎬 AI YouTube Content Generator")

st.title("🎬 AI-Powered YouTube Content Generator")
st.subheader("Generate both script and voice from your topic in one click")

# 1) Topic input
topic = st.text_input("📌 Enter the topic for your video:")

# 2) Style selection
style = st.selectbox("🎭 Choose Voice Style", [
    "Default", "Serious", "Friendly", "Aggressive", "Announcer"
])

# 3) Generate Script & Voice
if st.button("🚀 Generate Script & Voice"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating script..."):
            script = generate_youtube_script(topic)
            save_script_to_file(script)
        st.success("Script generated!")
        st.text_area("📝 Your Script", script, height=300)

        with st.spinner("Synthesizing voice..."):
            audio_path = synthesize_from_text(script, style)
        st.success("Audio generated!")
        st.audio(audio_path, format="audio/wav")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & Parler-TTS")
