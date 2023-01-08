def romanToInt(s: str) -> int:
    d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    nums=[d[i] for i in s]
    if(sorted(nums , reverse=True)!=nums):
        for i in range(1,len(nums)):
            if(nums[i-1]<nums[i]):
                nums[i-1]=-1 *nums[i-1]
    return sum(nums)


assert(romanToInt("III")==3)
assert(romanToInt("LVIII")==58)
assert(romanToInt("MCMXCIV")==1994)
#
# print(romanToInt("IV"))
assert(romanToInt("IV")==4)
print("done")
