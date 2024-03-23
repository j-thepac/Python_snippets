from flask import Flask,request
from flask_cors import CORS
from az import gimme_the_letters


app=Flask(__name__)
CORS(app)


@app.route("/",methods=["POST"])
def fn():
    data=request.json["data"]
    return gimme_the_letters(data)

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)