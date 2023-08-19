"""
Given a set of elements (integers or string characters, characters only in RISC-V)== where any element may occur more than once, return the number of subsets that do not contain a repeated element.

Let's see with an example:

set numbers = {1, 2, 3, 4}
The subsets are:

{{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4}, {1,3,4}, {2,3,4}, {1,2,3,4}}
There are 15 subsets. As you can see, the empty set, {}, is not counted.

Let's see an example with repetitions of an element:

set letters = {a, b, c, d, d}
The subsets for this case (including only those that have no repeated elements inside) will be:

{{a}, {b}, {c}, {d}, {a,b}, {a,c}, {a,d}, {b,c}, {b,d}, {c,d}, {a,b,c}, {a,b,d}, {a,c,d}, {b,c,d}, {a,b,c,d}}
There are 15 subsets.

The function est_subsets() (javascript: estSubsets()) will calculate the number of these subsets.

It will receive the array as an argument and according to its features will output the amount of subsets that do not contain a repeated element.

est_subsets([1, 2, 3, 4]) == 15
est_subsets(['a', 'b', 'c', 'd', 'd']) == 15
Features of the random tests:

Low Performance Tests: 40
Length of the arrays between 6 and 15

High Performance Tests: 80
Length of the arrays between 15 and 100 (Python and Ruby) between 15 and 63 (C++) and between 15 and 50 in javascript and Lua
Just do it!
"""

# def est_subsets(arr):
#     if (len(arr)==0):return 0
#     s=set(arr)
#     from itertools import combinations
#     sum=0
#     for i in range(1,len(arr)+1):
#         sum=sum+len(list(combinations(list(s) , i)))
#     return sum

def est_subsets(arr):
    if (len(arr)==0):return 0

    s=list(set(arr))
    if(len(s)==1):return 1
    
    from functools import reduce
    res=0
    for i in range(1,len(s)+1):
        num=list(range(len(s),0,-1))[0:i]
        deno=list(range(1,i+1))
        tempA=reduce(lambda x,y: x*y,num)
        tempB=reduce(lambda x,y: x*y,deno)
        res=res+(tempA/tempB)
    return res



assert(est_subsets([1, 2, 3, 4])== 15)
assert(est_subsets(['a', 'b', 'c', 'd', 'd'])== 15)
assert(est_subsets( [2, 3, 4, 5, 5, 6, 6, 7, 8, 8])== 127)
arr = ['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b', 'd', 'j', 'j', 'n', 'm', 'm']
assert(est_subsets(arr)== 511)


print("Done")