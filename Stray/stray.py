"""
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3 

docker
docker run -it --name stray -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python stray.py

docker build -t stray:v1 .

"""

def stray(arr):
    a,b=set(arr)
    return a if(arr.count(a)==1) else b

assert(stray([1, 1, 1, 1, 1, 1, 2])== 2)
assert(stray([2, 3, 2, 2, 2])== 3)
assert(stray([3, 2, 2, 2, 2])== 3)
print("done")