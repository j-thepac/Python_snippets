from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
from reducefraction import reduce_fraction
import json
app=Flask(__name__)
CORS(app)

api=Api(app)
class Reduce(Resource):
    def post(self):
        data=request.json["data"]
        if(type(data)==str):data=json.loads(data)
        print(data)
        result=reduce_fraction(data)
        return list(result)
    
api.add_resource(Reduce,"/")
if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)
