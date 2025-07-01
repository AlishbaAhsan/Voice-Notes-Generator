import streamlit as st
from voice_backend import tts_bytes

st.title("🗣️ Read Aloud")

text = st.text_area("Enter text to speak", "")

if 'audio' not in st.session_state:
    st.session_state.audio = None

if st.button("Generate & Play"):
    if text.strip():
        audio = tts_bytes(text)
        st.session_state.audio = audio
        st.audio(audio, format='audio/mp3')
    else:
        st.warning("Please enter some text.")

if st.session_state.audio:
    st.download_button(
        label="Download MP3",
        data=st.session_state.audio,
        file_name="GeneratedAudio.mp3",
        mime="audio/mp3"
    )
