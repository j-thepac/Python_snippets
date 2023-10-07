from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
from pluck import pluck

origins = ["*"]
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Obj(BaseModel):
    data: List[Dict[str, Any]]
    name:str


@app.post("/")
def fn(obj:Obj,r:Request):
    # payload=obj.dict()
    data=obj.data
    name=obj.name
    return pluck(data,name)

if(__name__ == "__main__"):
    uvicorn.run("server:app",host="0.0.0.0",port=5000)