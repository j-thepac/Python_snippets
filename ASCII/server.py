from flask_restful import Api,Resource
from flask import Flask,request
from ascii import convert
app=Flask(__name__)
api=Api(app)
import logging
logging.basicConfig(level=logging.INFO)


class A(Resource):
    def post(self):
        print
        logging.info(f"{request.json}")
        data=request.json["data"]
        return convert(data)

api.add_resource(A,"/")
if(__name__=="__main__"):
    app.run(host="0.0.0.0" ,port=4321)