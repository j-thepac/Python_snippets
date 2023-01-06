"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


def twoSum(nums: list[int], target: int) -> list[int]:
    for i in nums:
        find=target-i
        if(find in nums[nums.index(i)+1:]):
                if(i==find):
                    a=nums.index(i)
                    nums[a]="x"
                    return [a,nums.index(find)]
                return [nums.index(i),nums.index(find)]



assert(twoSum([2,7,11,15] , 9)==[0,1])
print("done")