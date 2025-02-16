from fastapi import FastAPI,Request
import uvicorn
from pydantic import BaseModel
from buyshare import Solution
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    data:str

@app.post("/")
def fn(r:Request,d:Data):
    # print(data["data"])
    sol=Solution()
    print(d.data)
    if type(d.data)==str:
        data= [ int(i) for i in d.data.split(",")]
        res=sol.maxProfit(data)
    else:
        res=sol.maxProfit(d.data)
    return res


if __name__=="__main__":
    uvicorn.run(host="0.0.0.0",port=5000,app="server:app")
