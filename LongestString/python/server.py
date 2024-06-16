from flask_restful import Api,Resource
from flask import Flask,request
from flask_cors import CORS
from longeststring import Solution


app=Flask(__name__)
api=Api(app)
CORS(app)

class LongestString(Resource):
    def post(self):
        s=request.json["data"]
        print(s)
        return Solution().lengthOfLongestSubstring(s)

api.add_resource(LongestString,"/")
if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)
