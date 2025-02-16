"""
Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
"""

# 

class Solution:
    def hammingWeight(self, n: int) -> int:
        sm=0
        if n==1: return 1
        while n>=2:
            sm=sm+n%2
            n=n//2
        return sm+1

    def hammingWeight2(self, n: int) -> int:
        sm=0
        def fn(n):
            nonlocal sm
            if n<=2:
                sm+=1
                return 
            sm=sm+n%2
            fn(n//2)
        fn(n)
        return sm

 

s=Solution()
# s.fn()
print(s.hammingWeight(2147483645)) # 2147483645 , 128