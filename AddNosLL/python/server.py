from flask import Flask,request
from flask_cors import CORS
from AddNosLL import Solution,ListNode
app=Flask(__name__)
CORS(app)
@app.route("/",methods=["POST"])
def fn():
    l1=request.json["l1"]
    nl1=createListNode(l1)

    l2=request.json["l2"]
    nl2=createListNode(l2)

    sol=Solution()
    sol.addTwoNumbers(nl1,nl2)
    return sol.resultList[:-1]

def createListNode(l1:str)->ListNode:
    ll=[int(i) for i in l1.split(",")]
    nl1=ListNode(ll[0])
    for i in ll[1:]:nl1.append(i)
    return nl1



if(__name__=="__main__"):
    app.run(host="0.0.0.0",port=5000,debug=True)