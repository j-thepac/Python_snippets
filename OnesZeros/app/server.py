from flask import Flask,request,render_template
from onezero import same_length
from flask_cors import CORS
app=Flask(__name__)
CORS(app)


@app.route("/",methods=["GET","POST"])
def fn():
    if request.method=="GET":
        return render_template("1.html")

    elif request.method=="POST":
        data=str(request.form["1"])
        print(data)
        result=str(same_length((data)))
        print(result)
        return render_template("1.html",result=result)


if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)