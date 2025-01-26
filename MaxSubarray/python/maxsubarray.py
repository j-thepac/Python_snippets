'''
 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        mx=max(nums)
        n=nums[0]
        for i in nums[1:]:
            temp=(i,mx)
            
        return mx

l = [-2,1,-3,4,-1,2,1,-5,4]
l= [-2,-3,-1] #-1
l= [1,2,-1,-2,2,1,-2,1,4,-5,4] #6
l=[6,-5,11]
s=Solution()
res=s.maxSubArray(l)
print(res)