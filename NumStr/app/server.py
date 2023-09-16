

from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from numstr import solve
origins = ["*"]

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
def fn(data:Data,r:Request):
    return(solve(data.data))


if(__name__ == "__main__"):
    uvicorn.run("server:app",host="0.0.0.0", port=5000)