from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
from latestdate import latest_clock
app=Flask(__name__)
CORS(app)
api=Api(app)


class LatestDateServer(Resource):
    def post(self):
        a=request.json["a"]
        b=request.json["b"]
        c=request.json["c"]
        d=request.json["d"]
        result=latest_clock(a,b,c,d)
        return result

api.add_resource(LatestDateServer,"/")   
if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)
