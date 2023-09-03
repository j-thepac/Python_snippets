
from flask import Flask,request
from intseq import find_sequences
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


import logging
logging.basicConfig(level=logging.INFO)
@app.route("/",methods=["GET","POST"])
def fn():
    if request.method=="POST":
        data=request.json["data"]
        logging.info("received {data}")
        if(type(data)==str):data = int(data)
        return find_sequences(data)
        # logging.info(request.json)
        # return ("Working")


if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000, debug=True)