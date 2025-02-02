from flask import Flask,request
from flask_restful import Api,Resource
from flask_cors import CORS
from stair import Solution

app=Flask(__name__)
api=Api(app)
CORS(app)
class A(Resource):
    def post(self):
        data=request.json["data"]
        data =int(data)
        s=Solution()
        res= s.climbStairs(data)
        print(res)
        return res


api.add_resource(A,"/")

if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000)

