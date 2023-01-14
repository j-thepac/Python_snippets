"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""



def isValid2(s: str) -> bool:
    s=s.replace("()","").replace("[]","").replace("{}","")
    if(len(s)%2!=0):return False
    if(s.count("(")!=s.count(")") or s.count("[")!=s.count("]") or s.count("{") != s.count("}")):return False
    l=list(s)
    while(len(l)!=0):
        m=(len(l)//2)
        if(l[m-1]=='(' and l[m]==')' or l[m-1]=='[' and l[m]==']' or l[m-1]=="{" and l[m]=='}'):
            del l[m]
            del l[m-1]
        else: return False
    return True


def isValid(s: str) -> bool:
    if(len(s)%2!=0):return False
    if(s.count("(")!=s.count(")") or s.count("[")!=s.count("]") or s.count("{") != s.count("}")):return False
    while (len(s)>0):
        count=len(s)
        s=s.replace("()","").replace("[]","").replace("{}","")
        if(len(s)==count): return False
    return True



assert (isValid("[([[]])]")==True)
assert (isValid("(([]){})")==True)
assert (isValid("()[]{}")==True)
# assert(isValid("(]")==False)
