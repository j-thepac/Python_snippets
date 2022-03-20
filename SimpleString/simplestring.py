"""
You will be given two strings a and b consisting of lower case letters, but a will have at most one asterix character. The asterix (if any) can be replaced with an arbitrary sequence (possibly empty) of lowercase letters. No other character of string a can be replaced. If it is possible to replace the asterix in a to obtain string b, then string b matches the pattern.

If the string matches, return true else false.

For example:
solve("code*s","codewars") = true, because we can replace the asterix(*) with "war" to match the second string. 
solve("codewar*s","codewars") = true, because we can replace the asterix(*) with "" to match the second string. 
solve("codewars","codewars") = true, because the strings already match.
solve("a","b") = false
solve("*", "codewars") = true
"""
def solve(a,b):
    if("*" in a):
        import re
        res=re.findall(a.replace("*",".*"),b)
        return (len(res)>0)
    else:
        return (a == b)




assert(solve("code*s","codewars")==True)
assert(solve("codewar*s","codewars")== True)
assert(solve("code*warrior","codewars")==False)
assert(solve("c","c")==True)
assert(solve("*s","codewars")==True)
assert(solve("*s","s")== True)
assert(solve("s*","s")==True)
assert(solve("aa","aaa")== False)
assert(solve("aa*","aaa")== True)
assert(solve("aaa","aa")== False)
assert(solve("aaa*","aa")== False)
assert(solve("*","codewars")==True)
print("done")