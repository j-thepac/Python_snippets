class Solution():
    def productExceptSelf(self, nums: list[int]) -> list[int]:
  
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        ans = [0] * len(nums)
        prefix[0] = 1
        suffix[-1] = 1
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]
        return ans

    def productExceptSelf21(self, nums: list[int]) -> list[int]:
        return [ prod(nums[0:i])*prod(nums[i+1:])   for i in range(0,len(nums))]

    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(0,len(nums)):
            temp=1
            for j in range(0,len(nums)):
                if i==j:continue
                temp=temp*nums[j]
            res.append(temp)
        return res


s=Solution()

print(s.productExceptSelf([1,2,3,4]))