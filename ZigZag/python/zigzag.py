"""
deepak
count =0 1 2
0d   a 
1e p k
2e 


ABCD
=
AC
BD

s = "PAYPALISHIRING", numRows = 3
result= PAHNAPLSIIGYIR
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):return s
        if(numRows==2): return s[::2]+s[1::2]
        d={}
        flag=0
        count=0
        for i in s:
            if flag==0:
                if(count not in d):d[count]=""
                d[count]=d[count]+i
                count+=1
                if(count==numRows):
                    flag=1
                    count=numRows-2

            elif flag:
                d[count]=d[count]+i
                if(count==1):
                    flag=0
                    count=0
                else:count-=1

        return "".join(d.values())

