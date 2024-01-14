from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
from climbgrade import sort_grades
import os

app=Flask(__name__)
CORS(app)
api=Api(app)


class Climb(Resource):
    def post(self):
        
        lst=eval(request.json["data"])
        result=sort_grades(lst)
        return result
    
api.add_resource(Climb,"/")

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)