

        
        
class Solution():
    def isValid(self, s: str) -> bool:
        if(len(s)%2!=0):return False
        for _ in range(0,len(s),2):
            if ("()"  in s or "[]"  in s or "{}"  in s):
                s=s.replace("()","").replace("[]","").replace("{}","")
            else:return False
        return True

    

v="(){}}{"
sol=Solution()
print(sol.isValid(v))
