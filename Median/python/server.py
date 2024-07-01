from fastapi import FastAPI,Request
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from median import Solution

origins = ["*"]
app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class Data(BaseModel):
    data1:str
    data2:str

@app.post("/")
def fn(data:Data):
    data1=[ int(i) for i in data.data1.split(",")]
    data2=[ int(i) for i in data.data2.split(",")]
    sol=Solution()
    return sol.findMedianSortedArrays(data1,data2)

if(__name__ =="__main__"):
    uvicorn.run("server:app",host="0.0.0.0",port=5000)