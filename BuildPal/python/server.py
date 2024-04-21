from flask import Flask, request
from flask_cors import CORS
from buildpal import build_palindrome
app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    data=request.json["data"]
    result=build_palindrome(data)
    return result


if(__name__ =="__main__"):
    app.run(host="0.0.0.0",port=5000)