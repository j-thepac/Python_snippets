"""
Given a varying number of integer arguments, return the digits that are not present in any of them.

Example:

[12, 34, 56, 78]  =>  "09"
[2015, 8, 26]     =>  "3479"
Note: the digits in the resulting string should be sorted.

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python unused.py
docker build -t unused:v1 .


"""
def unused_digits(*numbers):
    l=set("".join([str(i) for i in range(0,11)]))
    ip= set("".join([str(i) for i in numbers]))
    res = list(l.difference(ip))
    final_res=("".join(sorted(res)))
    return final_res

assert(unused_digits(12, 34, 56, 78)== "09")
assert(unused_digits(2015, 8, 26)== "3479")
assert(unused_digits(276, 575)== "013489")
assert(unused_digits(643)== "0125789")
assert(unused_digits(864, 896, 744)== "01235")
print("done")