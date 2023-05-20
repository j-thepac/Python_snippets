
"""


Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.

"""

def expanded_form(num):
    s=str(num)
    res=[]
    for i,j in enumerate(s[::-1]):
        res.append(10**i*int(j))
    res=list(filter(lambda x: x>0 , res))[::-1]
    finalRes = " + ".join([str(i) for i in res])
    return finalRes


def expanded_form2(num):
    s=str(num)
    from itertools import product
    l=[10**i for i in range(len(s)-1,-1,-1) ]
    res=[]
    for i,j in zip(s,l):
        res.append(int(i)*j)
    res=list(filter(lambda x: x>0,res))
    finalres = (" + ".join([str(i) for i in res]))
    return finalres



assert(expanded_form(12)== '10 + 2');
assert(expanded_form(42)== '40 + 2');
assert(expanded_form(70304)== '70000 + 300 + 4');
print("Done")