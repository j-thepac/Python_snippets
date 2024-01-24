from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
import json
from Share import share_price



app=Flask(__name__)
CORS(app)

api=Api(app)
class ShareRsc(Resource):
    def post(self):
        invested, changes = request.json["invested"], request.json["changes"]
        changes=json.loads((changes))
        result= share_price(invested,changes)
        return result
    
api.add_resource(ShareRsc,"/")
if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)