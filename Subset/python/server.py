from flask_restful import Api,Resource
from subset import est_subsets
from flask import Flask,request
import logging
logging.basicConfig(level=logging.INFO)
app=Flask(__name__)
api=Api(app)
import json


class Subs(Resource):
    def post(self):
        ip=request.json["data"]
        logging.info("working - ")
        if(type(ip)!=list):
            ip=json.loads(ip)
        result = est_subsets(ip)
        return result


api.add_resource(Subs,"/")

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)