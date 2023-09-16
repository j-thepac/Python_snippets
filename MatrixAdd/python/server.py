

from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
from matrixadd import matrix_addition
import logging 
import json

logging.basicConfig(level=logging.INFO)
app=Flask(__name__)
CORS(app)
api=Api(app)

class MatrixAdd(Resource):
    def post(self):
        a=request.json[0]["a"]
        b=request.json[0]["b"]
        if(type(a)==str):
            a=eval(a)
            b=eval(b)
        logging.info(f"a = {a}")
        return (matrix_addition(a,b))


api.add_resource(MatrixAdd,"/")

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)

