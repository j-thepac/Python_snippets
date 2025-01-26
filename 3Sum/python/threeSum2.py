'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplet=[]
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                res=nums[i]+nums[l]+nums[r]
                if res==0:
                    triplet.append([nums[i],nums[l],nums[r]])                    
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    while l<r and nums[l]==nums[l+1]:
                        l+=1                    
                    l+=1
                    r-=1
                elif res<0:
                    l+=1
                else:
                    r-=1
        return triplet
        
i+search algorithm
1. if first value+p1+p2 = 0 , add to res
2. if first value+p1+p2 > 0 , 
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        for i in range(0,len(nums)):
            p1,p2=i+1,len(nums)-1
            while p1<p2:
                sm=nums[i]+nums[p1]+nums[p2]
                if(sm ==0):
                    res.append([nums[i],nums[p1],nums[p2]])
                    while p1<p2 and nums[p1]==nums[p1+1]:p1+=1
                    while p1<p2 and nums[p2]==nums[p2-1]:p2-=1
                    p1+=1
                    p2-=1
                elif(sm<0):p1+=1
                elif(sm>0):p2-=1
        return res

sol=Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))