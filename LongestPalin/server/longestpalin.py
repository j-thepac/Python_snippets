"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(0,len(s)):
            temp=""
            for j in range(i,len(s)+1):
                temp2=s[i:j]
                if(temp2==temp2[::-1]):temp=temp2
            if(len(temp)>len(res)):res=temp
        return res






sol=Solution()
assert(sol.longestPalindrome(s = "babad")=="bab")
print("Done")
