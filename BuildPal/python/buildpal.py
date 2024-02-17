"""
Task
Given a string str, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example
For str = "abcdc", the output should be "abcdcba".

Input/Output
[input] string str

A string consisting of lowercase latin letters.

Constraints: 3 ≤ str.length ≤ 10.

[output] a string
"""
def build_palindrome(st):
    for i in range(0,len(st)):
        temp=st+st[0:i][::-1]
        if(temp == temp[::-1]):return temp
    


assert(build_palindrome("abcdc")=="abcdcba")
assert(build_palindrome("ababab")=="abababa")
print("DOne")
