from gtts import gTTS, gTTSError
import io

from fastapi import FastAPI, Response, HTTPException
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
    try:
        text = item.text
        if not text:
            raise ValueError("Text cannot be empty")

        language = 'id'
        voice = gTTS(text=text, lang=language, slow=False)
        audio = io.BytesIO()
        voice.write_to_fp(audio)
        audio.seek(0)
        
        return Response(content=audio.read(), media_type="audio/mpeg")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except gTTSError as ge:
        raise HTTPException(status_code=400, detail=f"gTTS error: {str(ge)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
