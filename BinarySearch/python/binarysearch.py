'''

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

'''


class Solution:
    j=0
    def search(self, nums: list[int], target: int) -> int:
        if len(nums)==0:return (-1)
        if len(nums)==1:
            if(nums[0]!=target):return -1
            else: return self.j
        m=len(nums)//2
        if(target==nums[m]):return self.j+m
        elif(target<nums[m]):return self.search(nums[:m],target)
        else:
            self.j=self.j+m
            return self.search(nums[m:],target)


nums = [-1,0,3,5,9,12]
sol=Solution()
print(sol.search(nums,2))