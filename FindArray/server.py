from flask import Flask,request,json,render_template
from findarray import find_array
app=Flask(__name__)

@app.route("/",methods=["POST"])
def fn():
    arr1=request.json["arr1"]
    arr2=request.json["arr2"]
    if(type(arr1)==str):arr1=eval(arr1)
    if(type(arr2)==str):arr2=eval(arr2)
    res=find_array(arr1,arr2)
    return res


if(__name__=="__main__"):
    app.run(host="localhost",port=4321)
