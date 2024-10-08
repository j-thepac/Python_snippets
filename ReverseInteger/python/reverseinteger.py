'''

7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        res= int(str(abs(x))[::-1])
        if(x <0 and res > 2147483648) or (x>0 and res >2147483647): return 0
        if(x<0):return res*-1
        else: return res


# x=123
# sol=Solution()
# assert(sol.reverse(x))
# print("Done")