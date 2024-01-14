from flask import Flask,request
from flask_cors import CORS
from trickertreat import candies
import json

app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    data=request.json["data"]
    return str(candies(json.loads(data)))

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)