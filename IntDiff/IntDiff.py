"""
Write a function that accepts two arguments: an array/list of integers and another integer (n).

Determine the number of times where two integers in the array have a difference of n.

For example:

[1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
[1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)

docker:
docker run -it --name -v $PWD:/home/app -w /home/app/ -p 5000:5000 python:3.9-slim python IntDiff.py

docker build -t ver:v1 .

"""
from typing import List
def int_diff(lst:List, n):
    res=[]
    for i in lst:
        temp=lst[:]
        temp.remove(i)
        # ptr=lst.index(i)
        # del temp[ptr]
        for j in temp:
            if((j-i) == n):
                res=res+[(i,j)]
    print(res)
    return len(res)

    # return len([ (i ,j) for i,j in product(lst,lst) if(i-j == n) ])
    # res=[]
    # for i,j in product(lst,lst):
    #     if((i-j) == n):
    #         res=res+[(i,j)]
    # return len(res)
assert(int_diff([ 7, 8, 7],0)==1)
assert(int_diff([1, 1, 5, 6, 9, 16, 27], 4)==3)
assert(int_diff([1, 1, 3, 3], 2)== 4)
print("done")