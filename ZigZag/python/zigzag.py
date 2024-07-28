"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


  """
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(len(s)==1 or numRows == 1 ):return s
        d={}
        flag=0
        count=0
        for i in s:
            if(flag==0):
                if(count not in d):d[count]=""
                d[count]=d[count]+i
                count+=1
                if(count==numRows):
                    count=numRows-2
                    flag=1
            elif flag:
                d[count]=d[count]+i
                if(count==1):
                    flag=0
                    count=0
                else:count=-1
        return "".join(d.values())

v="PAYPALISHIRING"
sol=Solution()
assert(sol.convert(v,3)=="PAHNAPLSIIGYIR")
print("Done")
        

""" 
deepak

0d   a
1e p k
2e 
"""