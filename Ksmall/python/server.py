from flask import Flask,request,json,jsonify
from flask_cors import CORS
from flask_restful import Api,Resource
from ksmall import Solution,TreeNode

app=Flask(__name__)
api=Api(app)
CORS(app)
class A(Resource):
    def post(self):
        req=request.json
        l=req["root"]
        if isinstance(l,str):l=[int(i) for i in l.split(",")]
        t=TreeNode(l[0])
        for i in l[1:]:
            t.append(i)

        s=Solution()
        res=s.kthSmallest(t,int(req["k"]))
        return res

api.add_resource(A,"/")
if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)