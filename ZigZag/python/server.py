from flask import Flask,request
from flask_cors import CORS
from zigzag import Solution

app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    s=request.json["s"]
    numRows=int(request.json["numRows"])
    sln=Solution()
    result=sln.convert(s=s,numRows=numRows)
    return result


if(__name__ =="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)