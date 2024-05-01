from django.shortcuts import render

# Create your views here.
def encode(message, key):
    f=lambda x:ord(x)-96
    res1= list(map(f,message))
    key= list(str(key)*len(res1))
    return [i+int(j) for i,j in zip(res1,key)]

def encodeView(request):
    if(request.method=="GET"):return render(request,"1.html")
    else:
        message=request.POST["message"]
        key=request.POST["key"]
        result= encode(message=message,key=key)
        return render(request,"2.html",{"result":result})