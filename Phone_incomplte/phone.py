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
    "1":""
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
    fours=["9","7"]
    v=string_of_nums
    l=[re.findall(v[x]+"+",v[x:])[0] for x in range(0,len(v)) if(v[x]!=v[x-1])]
    # i=0
    # res=[]
    # for i in l:
    #     if(i[0] in fours and len(l[i])>4):
    #         res.append()
    res1= [d[i] for i in l]
    # print(res1)
    return "".join(res1)


assert(phone_words("443355555566604466690277733099966688")=="hello how are you")
# assert(phone_words("55282")== "kata")
# assert(phone_words("44460208337777833777")== "im a tester")
# assert(phone_words("22266631339277717777")== "codewars")
# assert(phone_words("66885551555")== "null")
# assert(phone_words("833998")== "text")
# assert(phone_words("000")== "   ")
# assert(phone_words("7999844666166")== "python")
# assert(phone_words("55886444833")== "kumite")
# assert(phone_words("271755533")== "apple")
# assert(phone_words("")== "")
# assert(phone_words("111")== "")