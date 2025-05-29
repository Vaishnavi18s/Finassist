from fastapi import FastAPI, Request
from gtts import gTTS
import os

app = FastAPI()

@app.post("/voice/speak")
async def voice_speak(request: Request):
    body = await request.json()
    text = body["text"]
    tts = gTTS(text)
    tts.save("response.mp3")
    return {"audio_file": "response.mp3"}