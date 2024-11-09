from flask import Flask,request
from binarysearch import Solution
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    nums=request.json["nums"]
    if(isinstance(nums,str)):
        nums=[int(i) for  i in nums.split(",") ]
    target=request.json["target"]
    if(isinstance(target,str)):target=int(target)
    res=Solution().search(nums,target)
    return str(res)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)