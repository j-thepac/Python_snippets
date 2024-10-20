from django.shortcuts import render
from app.container import Solution
# Create your views here.


def fn(request):
    if(request.method=="GET"):
        return render(request,"1.html")
    else:
        ip=request.POST["a"]
        data=[int(i) for i in ip.split(",")]
        sol=Solution()
        res=sol.maxArea(data)
        return render(request,"1.html",{"result":res})