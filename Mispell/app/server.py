from flask import Flask,request
from flask_cors import CORS
from mispell import mispelled
app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    result=mispelled(request.json["data1"],request.json["data2"])
    return str(result)


if (__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)