from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from LetterBomb import alphabet_war


app=FastAPI()
class Data(BaseModel):
    data:str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def fn(r:Request,obj:Data):
    fight=obj.data
    result=alphabet_war(fight)
    return result

if(__name__=="__main__"):
    uvicorn.run("server:app", host="0.0.0.0",port=5000)