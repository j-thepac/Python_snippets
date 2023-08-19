from jungerstein1 import count_zeros_n_double_fact
from flask import Flask,request,json,jsonify,render_template

app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def fn():
    if(request.method=="GET"):
        return render_template("index.html")
    elif(request.method=="POST"):
        num=request.form["1"]
        result=count_zeros_n_double_fact(int(num))
        return render_template("index.html",result=result)



if(__name__ =="__main__"):
    app.run(host="0.0.0.0",port=4321,debug=True)