from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from reverseinteger import Solution
app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    x:int

@app.post("/")
async def fn(r:Request,data:Data):
    x=data.x
    sol=Solution()
    res=sol.reverse(x)
    return res

if(__name__ =="__main__"):
    uvicorn.run("server:app",host="0.0.0.0",port=5000)