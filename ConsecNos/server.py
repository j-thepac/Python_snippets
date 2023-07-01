from flask import Flask,request
from consecnos import consecutive
app=Flask(__name__)

@app.route("/",methods=["POST"])
def fn():
    ip= str(request.data)
    print(ip)
    return str(consecutive(ip))
    

if(__name__=="__main__"):
    app.run(host="localhost",port=4321)