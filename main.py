from gtts import gTTS
import io

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=False,
    allow_methods=["POST"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/voice")
async def read_voice(item: Item):
    text = item.text
    language = 'id'
    voice = gTTS(text=text, lang=language, slow=False)
    audio = io.BytesIO()
    voice.write_to_fp(audio)
    audio.seek(0)

    return Response(content=audio.read(), media_type="audio/mpeg")