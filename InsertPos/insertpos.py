"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: temp = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: temp = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: temp = [1,3,5,6], target = 7
Output: 4
"""


def searchInsert( nums: int, target: int) -> int:
    temp=nums[:]
    while len(temp)>1:
        m=len(temp)//2
        if (temp[m]>=target):temp=temp[0:m]
        else:temp=temp[m:]   
    ptrVal=temp[0]
    ptrIndex=nums.index(ptrVal)
    if (ptrVal > target):
        if( (ptrIndex-1) <0): return 0
        else: return (ptrIndex-1)
    else: return ptrIndex+1
        
    

# assert(searchInsert( [1,3,5,6], 7)==4)
# assert(searchInsert( [1,3,5,6], 2)==1)

# assert(searchInsert( [1,3,5,6], 5)==2)
assert(searchInsert( [1,3,5,6], 0)==0)
assert(searchInsert( [1,3,5,6], 0)==0)
print("DONE")