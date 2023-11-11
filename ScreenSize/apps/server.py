from flask import Flask,request
from flask_cors import CORS
from screensize import find_screen_height

app=Flask("__name__")
CORS(app)

@app.route("/",methods=["POST"])
def fn():
    width=request.json["width"]
    ratio=request.json["ratio"]
    result=find_screen_height(width, ratio)
    return (result)


if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)