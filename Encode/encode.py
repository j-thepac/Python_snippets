"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 



docker run -it --name encode -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python encode.py


docker 

"""

def duplicate_encode(word:str):
    word=word.lower()
    res= [")" if(word.count(i)>1) else "(" for i in word ]
    return("".join(res))

    # for i in word:
    #     if(word.count(i)>1):
    #         res=res+")"
    #     else:
    #         res=res+"("
    # return res

assert(duplicate_encode("Supralapsarian")==")()))()))))()(")
assert(duplicate_encode("din")=="(((")
assert(duplicate_encode("recede")=="()()()")
assert(duplicate_encode("(( @")=="))((")

print("done")