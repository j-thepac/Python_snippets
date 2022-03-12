"""
You are provided with an array of positive integers and an additional integer n (n > 1).

Calculate the sum of each value in the array to the nth power. Then subtract the sum of the original array.

Examples
{1, 2, 3}, 3  -->  (1^3 + 2^3 + 3^3 ) - (1 + 2 + 3)  -->  36 - 6  -->  30
{1, 2}, 5     -->  (1^5 + 2^5) - (1 + 2)             -->  33 - 3  -->  30

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.10-slim python nth_power.py
"""
from functools import reduce
import math
def modified_sum(a, n):
    res=reduce(lambda x,y:x+math.pow(y,n),a)
    res2=reduce(lambda x,y:x+y,a)
    return (res-res2)


assert(modified_sum([1, 2, 3], 3)== 30)
assert(modified_sum([1, 2], 5)== 30)
print("done")