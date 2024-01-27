from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from ap import find_missing
import json
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    seq:str

@app.post("/")
def fn(r:Request,data:Data):
    seq=data.seq
    seq=json.loads(seq)
    print(seq,type(seq[0]))
    result = find_missing(seq)
    return str(result)

if(__name__ == "__main__"):
    uvicorn.run("server:app",host="0.0.0.0",port=5000)