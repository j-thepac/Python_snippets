
#
from fastapi import FastAPI,Request
import uvicorn
from pydantic import BaseModel

class Person(BaseModel):
    name:str

app=FastAPI()

@app.get("/test/{id}")
def fn(id:int,request:Request):
    if(request.headers["Content-type"]=="application/json"):
        print("headers=application/json", id,sep=" ")
        return "working"

@app.post("/test/{id}")
def fn2(id:int,person:Person,request:Request):
    if(request.headers["Content-type"]=="application/json"):
        print("headers=application/json", id,person,sep=" ")

#
if(__name__=="__main__"):
    uvicorn.run("app:app",host="0.0.0.0",port=9999,reload=True)

