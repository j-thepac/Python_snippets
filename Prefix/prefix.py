"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs: list[str]) -> str:
    m=sorted(strs,key=lambda x:len(x))[0]
    i=1
    while True:
        find=m[:i]
        res=all(list(map(lambda x: find in x[0:len(m)] , strs)))
        if(res==False):break
        i=i+1
    return m[:i-1]

def longestCommonPrefix2(strs: list[str]) -> str:
    m=sorted(strs,key=lambda x:len(x))[0]
    i=1
    while True:
        find=m[:i]
        res=all(list(map(lambda x: find in x[0:len(m)] , strs)))
        if(res==False):break
        i=i+1
    return m[:i-1]


assert(longestCommonPrefix(["flower","flow","flight"])=='fl')
assert(longestCommonPrefix(["dog","racecar","car"])=="")
print("Done")