"""
Complete the function which accepts a string and return an array of character(s) that have the most spaces to their right and left.

Notes:

the string can have leading/trailing spaces - you should not count them
the strings contain only unique characters from a to z
the order of characters in the returned array doesn't matter
Examples
"a b  c"                        -->  ["b"]
"a bcs           d k"           -->  ["d"]
"    a b  sc     p     t   k"   -->  ["p"]
"a  b  c  de"                   -->  ["b", "c"]
"     a  b  c de        "       -->  ["b"]
"abc"                           -->  ["a", "b", "c"]

"""
import re
from itertools import groupby

def loneliest(strng:str):
    l= re.findall("[a-zA-Z]*",(strng.strip()))
    res=[]
    # spaces=[]
    for k,g in groupby(l):
        if( k=="" ):
            size=len(list(g))
            res.append(size)
            # spaces.append(f"z{size}")
        else:res.append(k)
    m=0
    res2=[]
    for i in range(1,len(res),2):
        if(i > m)

    # print(res)
    # res=res[:-1]
    # print(res)
    # print((spaces))
    # max=0
    # newres=""
    # for i in range(0,len(res)):
    #     if(isinstance(i,int)):
    #         if(i>max and len(res[i+1])==1):
    #             max=i
    #             newres

    # print(res)

loneliest('abc d   ef  g   h i j      ')
# loneliest('abc')

# assert(sorted(loneliest('a'))==['a'] )
# assert(sorted(loneliest('abc d   ef  g   h i j      '))== ['g'])
# assert(sorted(loneliest('a   b   c '))== ['b'])
# assert(sorted(loneliest('  abc  d  z    f gk s '))== ['z'])
# assert(sorted(loneliest('a  b  c  de  '))== ['b', 'c'])
# assert(sorted(loneliest('abc'))== ['a', 'b', 'c'])