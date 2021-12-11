
"""
Given a sequence of numbers, find the largest pair sum in the sequence.

For example

[10, 14, 2, 23, 19] -->  42 (= 23 + 19)
[99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
Input sequence contains minimum two elements and every element is an integer.

docker
docker run -it --name largest_sum_pair  -v $PWD:/home/app/ -w /home/app python:3.8-slim python largest_sum_pair.py



"""

def largest_pair_sum(numbers):
    sorte=sorted(numbers,reverse=True)
    return (sorte[0]+sorte[1])
    # your code here

assert(largest_pair_sum([1, 2, 3, 4, 6, -1, 2])==10)
assert(largest_pair_sum([-10, -8, -16, -18, -19])== -18)
print("working")