from flask import Flask ,request
from addtest import add
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.INFO)
app=Flask(__name__)
CORS(app)

@app.route("/", methods=["GET","POST"])
def fn():
    if(request.method=="POST"):
        a=int(request.json["a"])
        b=int(request.json["b"])
        logging.info(f"{a} , {b}")
        return str(add(a,b))
    


if(__name__ =="__main__"):
    app.run(host="0.0.0.0" , port=5000)