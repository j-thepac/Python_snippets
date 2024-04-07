# uvicorn server:app --reload --host 0.0.0.0 --port 5000

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from CharCount import validate_word

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Data(BaseModel):
    data:str

@app.post("/")
def fn(data:Data):
    result=validate_word(data.data)
    return result