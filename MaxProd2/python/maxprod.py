"""

Max prod

Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
# l=[2,3,-2,4]
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        mx,mn=1,1
        res=0
        for num in nums:
            t = (num , mx*num , mn*num)
            mx = max(t)
            mn = min(t)
            res=max(res,mx)
        return res

l=[-1,2,3,4,-5]
# l=[-2,3,-4]
s=Solution()
print(s.maxProduct(l))
#)