from django.shortcuts import render

# Create your views here.



def longestPalindrome(request) -> str:
    if(request.method=="GET"):return render(request,"1.html")
    else:
        s=request.POST["data"]
        res=""
        for i in range(0,len(s)):
            temp=""
            for j in range(i,len(s)+1):
                temp2=s[i:j]
                if(temp2==temp2[::-1]):temp=temp2
            if(len(temp)>len(res)):res=temp
        # return res
        return render(request,"2.html",{"result":res})