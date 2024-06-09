# uvicorn --reload --host 0.0.0.0 --port 5000 server:app

from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from diffbwcoll import diff as dff
import json

origins = ["*"]
class Data(BaseModel):
    a:list[int]
    b:list[int]

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def fn(r:Request,data:Data):
    return dff(data.a,data.b)