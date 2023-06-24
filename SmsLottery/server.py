from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
from smslottery import validate_bet


from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]


class Data(BaseModel):
    game:str
    text:str

app= FastAPI()
# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def fn(d:Data):
    if(isinstance(d.game,str)):
        d.game=eval(d.game)
    j=validate_bet(d.game,d.text)

    if(j is None):return "None"
    return j



if(__name__=="__main__"):
    uvicorn.run("server:app",host="localhost",port=4321)