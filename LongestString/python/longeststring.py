"""
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(set(s))==1):return 1
        res=[]
        for i in range(len(s)):
            temp=""
            for j in range(i,len(s)):
                if s[j] not in temp:temp+=s[j]
                else:
                    break
            res.append(len(temp))
        return max(res)


s ="abcabcbb"
sol=Solution()
assert(sol.lengthOfLongestSubstring(s)==3)
assert(sol.lengthOfLongestSubstring("bbbbb")==1)
print("Done")
        