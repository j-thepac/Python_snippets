

class Solution:
    def addTwoNumbers(self, l1, l2) -> list:
        s1="".join(str(i) for i in l1)
        s2="".join(str(i) for i in l2)
        res= int(s1)+int(s2)
        return [int(i) for i in (str(res))][::-1]

s=Solution()        
l1 = [2,4,3]
l2 = [5,6,4]
assert (s.addTwoNumbers(l1,l2)==[7,0,8])

print("done")


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
assert (s.addTwoNumbers(l1,l2)==[8,9,9,9,0,0,0,1])
