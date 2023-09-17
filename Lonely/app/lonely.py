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

#'abc d   ef'
def loneliest(strng:str):
    strng=strng.strip()
    if len(strng)<=1 : return list(strng)
    elif strng.find(" ")==-1:return list(strng)
    
    l= re.findall("[a-zA-Z]*",strng)[:-1]
    res= countSpaces(l)
    res2=aggregateSpaces(res)
    res2=cleanList(res2)
    finalResult= accumulateMax(res2)
    print(res2,finalResult)
    return (finalResult)


# [[1,'abc'],[1,'d',3],[3,'ef']]
def countSpaces(l:list[str])->list:
    res=[]
    for k,g in groupby(l):
        if( k=="" ):
            size=len(list(g))
            res.append(size)
        else:res.append(k)
    return res

# [[1,'abc'],[4,'d'],[3,'ef']]
def aggregateSpaces(res:list):
    res2=[]
    for i in range(0,len(res),2):
        s,v=0,0
        if(i==0):
            v,s=res[0:0+2]
            res2.append([s,v])
        elif(len(res[i-1:i+2])==3):
            s1,v,s2=res[i-1:i+2]
            res2.append([s1+s2,v])
        else:
            v,s=res[0:0+2]
            res2.append([s,v])
    res2.sort(key=lambda x: x[0] , reverse=True)
    return res2

# [[4,'d'],[1,'abc']]
def cleanList(res2:list)->list:
    res2.sort(key=lambda x: x[0] , reverse=True)
    # res2=list(filter(lambda x:x[1][0],res2))
    res2=list(filter(lambda x:len(x[1])==1,res2))
    return res2

# ["d"]
def accumulateMax(res2:list)->list:
    m=res2[0][0]
    return [i[1] for i in res2 if(i[0] == m)]



# loneliest('a c')
# loneliest('abc')

assert(sorted(loneliest('a'))==['a'] )
assert(sorted(loneliest('abc d   ef  g   h i j      '))== ['g'])
assert(sorted(loneliest('a   b   c '))== ['b'])
assert(sorted(loneliest('  abc  d  z    f gk s '))== ['z'])
assert(sorted(loneliest('a  b  c  de  '))== ['b', 'c'])
assert(sorted(loneliest('abc'))== ['a', 'b', 'c'])

# assert(sorted(loneliest('qay     xwn  k d to  hlc      se  m  r'))==['c', 's'])