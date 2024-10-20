from flask import Flask,request
from flask_cors import CORS
from roman import Solution
app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    num=int(request.json["num"])
    sol=Solution()
    res=sol.intToRoman(num)
    return res

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)
