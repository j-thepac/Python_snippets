"""
Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


def checkInclusion(s1: str, s2: str) -> bool:
    if(len(s1)> len(s2)):return False
    if(s1 in s2 or s1 in s2[::-1]):return True
    for i in s1:
        if(i not in s2):return False
    from itertools import permutations
    for i in list(permutations(s1)):
        if("".join(i) in s2):return True
    return False


assert(checkInclusion("ab","eidbaooo")== True)
print("Done")