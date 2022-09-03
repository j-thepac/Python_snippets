"""
Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.
"""
from collections import Counter
def sum_no_duplicates(l):
    d=Counter(l)
    sum=0
    for k,v in d.items():
        if(v==1):sum=sum+k
    return sum
    

assert(sum_no_duplicates([1, 1, 2, 3])== 5)
assert(sum_no_duplicates([1, 1, 2, 2, 3])== 3)
print("done")
