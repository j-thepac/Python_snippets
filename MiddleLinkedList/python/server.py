
from flask import Flask,request
from flask_cors import CORS
from main import Solution,ListNode
app=Flask(__name__)
CORS(app)

@app.route("/",methods=["POST"])
def fn():
    l=request.json["data"]
    if isinstance(l,str):
        l=[ int(i) for i in l.split(",")]
    s=Solution()
    node=ListNode(l[0])
    for i in l[1:]:
        node.append(i)

    s=Solution()
    res=s.middleNode(node)
    lres=[]
    while (res):
        lres.append(res.val)
        res=res.next
    print(lres)
    return lres


if(__name__ =="__main__"):
    app.run(host='0.0.0.0',port=5000)
