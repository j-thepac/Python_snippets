"""
Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.

The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.
"""
def mygcd(x, y):
    if (x==1 and y==1):return 1
    minimum= (min(x,y)//2)+1
    res1= [i for i in range(1,minimum)  if(x%i==0 and y%i==0)]
    return max(res1)

assert(mygcd(30,12)==6)
assert(mygcd(8,9)==1)
assert(mygcd(1,1)==1)
print("done")