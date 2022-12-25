"""
For example if you get "22" return "b", if you get "222" you will return "c". If you get "2222" return "ca".

Further details:

0 is a space in the string.
1 is used to separate letters with the same number.
always transform the number to the letter with the maximum value, as long as it does not have a 1 in the middle. So, "777777" -->  "sq" and "7717777" --> "qs".
you cannot return digits.
Given a empty string, return empty string.
Return a lowercase string.
Examples:
"443355555566604466690277733099966688"  -->  "hello how are you"
"55282"                 -->  "kata"
"22266631339277717777"  -->  "codewars"
"66885551555"           -->  "null"
"833998"                -->  "text"
"000"                   -->  "   "

"""
d={
    "":""
   ,"1":""
    ,"0":" "
    ,"2":"a"
    ,"22":"b"
    ,"222":"c"

    ,"3":"d"
    ,"33":"e"
    ,"333":"f"

    ,"4":"g"
    ,"44":"h"
    ,"444":"i"
    
    ,"5":"j"
    ,"55":"k"
    ,"555":"l"
    
    ,"6":"m"
    ,"66":"n"
    ,"666":"o"
    
    ,"7":"p"
    ,"77":"q"
    ,"777":"r"
    ,"7777":"s"
    
    ,"8":"t"
    ,"88":"u"
    ,"888":"v"
    
    ,"9":"w"
    ,"99":"x"
    ,"999":"y"
    ,"9999":"z"}

import re

def phone_words(string_of_nums):
    print(string_of_nums)
    if(string_of_nums==""):return ""
    l=stringToList(string_of_nums)  
    res=""
    # print(l)
    for i in l:res=res+numToLetter(i)
    print(res)
    return (res)

def numToLetter(n:str)->str:
    fours=["9","7"]
    three=["2","3","4","5","6","8"]
    if(n[0] in fours and len(n)>4):
        times=len(n)//4
        rem=len(n)%4
        key= n[:4]
        return (d[key]*times+d[n[0]*rem])
    elif(n[0] in three and len(n)>3):
        times=len(n)//3
        rem=len(n)%3
        key= n[:3]
        return (d[key]*times+d[n[0]*rem])
    elif(n[0] in ("0","1")):return (d[n[0]]*len(n))
    else:return (d[n])

def stringToList(s:str)->list[str]:
    l=[]
    count=1
    res=""
    for i in range(0,len(s)-1):
        if(s[i]!=s[i+1]):
            l.append(s[i]*count)
            count=1
        else:count=count+1
    l.append(s[-1]*count)
    return l



assert(phone_words("443355555566604466690277733099966688")=="hello how are you")
assert(phone_words("55282")== "kata")
assert(phone_words("44460208337777833777")== "im a tester")
assert(phone_words("22266631339277717777")== "codewars")
assert(phone_words("66885551555")== "null")
assert(phone_words("833998")== "text")
assert(phone_words("000")== "   ")
assert(phone_words("7999844666166")== "python")
assert(phone_words("55886444833")== "kumite")
assert(phone_words("271755533")== "apple")
assert(phone_words("")== "")
assert(phone_words("111")== "")