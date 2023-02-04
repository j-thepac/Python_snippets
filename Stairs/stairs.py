"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs( n: int) -> int:
    from itertools import permutations
    l=[1]*n
    s=0
    for i in range(0,len(l)):
        s=s+len(set(permutations(l)))
        l=l[2:]
        l.append(2)
        if(sum(l) != n):break
    return s


assert(climbStairs(3)==3)
assert(climbStairs(2)==2)
assert(climbStairs(2)==2)
assert(climbStairs(4)==5)
assert(climbStairs(5)==8)

print("DOne")