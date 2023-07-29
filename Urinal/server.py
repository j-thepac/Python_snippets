from flask import Flask,request
from urinal import get_free_urinals
app=Flask(__name__)

@app.route("/",methods=["POST"])
def fn():
    if(request.method=="POST"):
        data=request.data.decode('ascii')
        return str(get_free_urinals(data))
    

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port="4321")