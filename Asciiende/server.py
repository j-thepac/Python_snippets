from fastapi import FastAPI,Request
from asciiende import ascii_encrypt
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

class Data(BaseModel):
    data:str

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
def fn(data:Data):
    return (ascii_encrypt(data.data))


if(__name__ =="__main__"):
    uvicorn.run("server:app",host="0.0.0.0",port=4321)