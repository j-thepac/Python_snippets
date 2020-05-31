"""
There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of n with 1<=n<=1500.

Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

Good Luck!!!

"""

def solve(n):
    res=0
    if n%10!=0:return -1
    for i in [500,200,100,50,20,10]:
        if(n//i!=0):
            res=res+n//i
            n=n%i
    return res


assert(solve(770)==4)
assert(solve(550)==2)
assert(solve(10)==1)
assert(solve(1250)==4)
assert(solve(1500)==3)

assert(solve(125)==-1)
assert(solve(666)==-1)
assert(solve(42)==-1)