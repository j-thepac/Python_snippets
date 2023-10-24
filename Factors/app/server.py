from flask import Flask,render_template,request
from flask_cors import CORS
from factor import factors
import json


app=Flask(__name__)
CORS(app)


@app.route("/",methods=["GET","POST"])
def fn():
    if(request.method=="GET"):return render_template("index.html")
    else:
        data=request.form["1"]
        if(isinstance(data,str)):data=eval(data)
        result=factors(*data)
        return render_template("index.html",result=result)


if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)