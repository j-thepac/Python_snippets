"""

1010 , 0101  = 4 bits are different in 2nd 
1011 , 1010 =  1 bit is different 
82 = 1010010 
5 =  0000101

differene = 5
"""
def fn(n1,n2):
    n1= bin(n1)[2:]
    n2= bin(n2)[2:]
    if(len(n1)> len(n2)):
        diff=len(n1)-len(n2)
        n2="0"*diff+n2
    elif(len(n1)> len(n2)):
        diff=len(n1)-len(n2)
        n1="0"*diff+n1
    res=0
    for i,j in zip(n1,n2):
        if(i!=j):res=res+1
    print(res)
    return res
assert(fn(82,5)==5)
assert(fn(10,5)==4)
assert(fn(7,6)==1)