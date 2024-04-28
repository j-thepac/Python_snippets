#  uvicorn "server:app" --reload --host 0.0.0.0 --port 5000

from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from stringscramble import scramble

origins = ["*"]
class Data(BaseModel):
    strng:str
    array:list[int]

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/")
def fn(data:Data):
    res=scramble(data.strng,data.array)
    return res



if(__name__ =="__main__"):
    uvicorn.run("server:app",host="0.0.0.0",port=5000)