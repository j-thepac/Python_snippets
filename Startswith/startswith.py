"""
Challenge: Given two null-terminated strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix" string. Return true or false.

Example:

startsWith("hello world!", "hello"); // should return true
startsWith("hello world!", "HELLO"); // should return false
startsWith("nowai", "nowaisir"); // should return false
Addendum: For this problem, an empty "prefix" string should always return true for any value of "string".

If the length of the "prefix" string is greater than the length of the "string", return false.

docker run -it -v $PWD:/home/app/ -w /home/app -p 5000:5000 python:3.9-slim python startswith.py


docker build -t startswith:v1 .
"""
def starts_with(st, prefix): 
    return True if (st[0:len(prefix)] == prefix) else False


assert(starts_with("", "")== True)
assert(starts_with("abc", "")== True)
assert(starts_with("", "abc")== False)

print("done")