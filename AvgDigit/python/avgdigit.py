def digits_average(x):    
    from math import ceil
    x=str(x)
    if x==1:return x
    while len(x)!=1:
        x=fn(x)
    print(x)
    return int(x[0])
    
def fn(x):
    from math import ceil
    res=[]
    l=[int(i) for i in str(x)]
    p1,p2=0,1 
    while p2<len(l)and p1<p2:
        res.append( ceil((l[p1]+l[p2]) /2)   )
        p1+=1
        p2+=1
    
    return ''.join(str(i) for i in res)


assert(digits_average(89)== 9)