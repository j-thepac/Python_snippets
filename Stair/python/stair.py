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
 

Constraints:

1 <= n <= 45

"""


class Solution:
    def climbStairs(self,n:int) -> int:
        temp=[1,2]
        if n<3:return n
        for i in range(3,n+1):temp.append(temp[-1]+temp[-2])
        return temp[-1]

    def climbStairs_old(self, n: int) -> int:
        from itertools import permutations
        res=[]
        l=[1 for i in range(0,n)]
        res=1
        while True:
            t1=l.pop(0)
            if t1==2: break
            
            t2=l.pop(0)
            if t2==2: break

            l.append(2)
            if sum(l)!= n or list(permutations(l))[0] == list(permutations(l))[1]: break

            res=res+len(list(permutations(l)))
        return res


s=Solution()
assert(s.climbStairs(35) == 14930352 )