"""
In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.

Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.

For example: 
solve("abc") = True, because it contains a,b,c
solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
solve("dabc") = True, because it contains a, b, c, d
solve("abbc") = False, because b does not occur once.
solve("v") = True

docker run -it --name consecutive -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python consecutive.py

docker build -t consecutive:v1 .
"""


def solve2(st):
    if len(set(st)) < len(st) : return False
    order=sorted(st)
    first=ord(order[0])
    res=[ord(i)-first for i in order]
    for i,j in enumerate(res):
        if i!=j:return False
    return True


def solve(st):
    alpha="".join(chr(i) for i in range(97,122))
    st="".join(sorted(st))
    if st not in alpha:return False
    return True

assert(solve("abc")==True)
assert(solve("abd")== False)
assert(solve("dabc")==True)
assert(solve("abbc")== False)
print("done")