from flask import Flask,request,json
from flask_cors import CORS
from circle import circle_of_numbers

app=Flask(__name__)
CORS(app)



@app.route("/",methods=["POST"])
def fn():
    print(request.json)
    n=int(request.json["n"])
    fst=int(request.json["fst"])
    return str(circle_of_numbers(n,fst))


if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)