# voice_backend.py
from gtts import gTTS
from io import BytesIO

def tts_bytes(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp.read()


