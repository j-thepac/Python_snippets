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

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=sorted(nums)
        n=len(nums)-1
        res=set()
        x=1
        y=n
        for i in range(0,len(l)):
            x=0
            y=n
            while x<=y:
                if(l[i]+l[x]+l[y] ==0  ):
                    res.add((l[i],l[x],l[y]))
                x+=1
                y-=1
        return res
'''
# res=[]
# def fn(l,tempRes,idx):
#     if(len(tempRes)==3 and sum(tempRes)==0):
#         if(tempRes not in res):res.append(tempRes[:])
#         return
#     elif(len(tempRes)==3):
#         return
#     for i in range(idx,len(l)):
#         tempRes.append(l[i])
#         fn(l,tempRes,i+1)
#         tempRes.pop()

class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        tempRes,res=[],[]
        self.fn(sorted(nums),tempRes,res,0)
        return res
    
    def fn(self,l,tempRes,res,idx):
        if(len(tempRes)==3 and sum(tempRes)==0):
            if(tempRes not in res):res.append(tempRes[:])
            return
        elif(len(tempRes)==3 ):
            return
        for i in range(idx,len(l)):
            if(len(tempRes)==2):
                if(tempRes[0]>0 and tempRes[1]>0 and l[i]>0):return
                elif(tempRes[0]<0 and tempRes[1]<0 and l[i]<0):return
            tempRes.append(l[i])
            self.fn(l,tempRes,res,i+1)
            tempRes.pop()





sol=Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
# l=sorted([-1,0,1,2,-1,-4])
# fn(sorted(l),[],0)
# print(res)