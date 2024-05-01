from django.shortcuts import render
import json
# from django import re

# Create your views here.
def getCT(request):
    if(request.method=="GET"):
       return render(request,"1.html")
    else:
        lst=request.POST["data"]
        lst=json.loads(lst)
        res= [ sum(lst[0:i]) for i in range(1,len(lst)+1) ]
        return render(request,"2.html",{"res":res})