"""
You are given two arrays arr1 and arr2, where arr2 always contains integers.

Write a function such that:

For arr1 = ['a', 'a', 'a', 'a', 'a'], arr2 = [2, 4] the function returns ['a', 'a']

For arr1 = [0, 1, 5, 2, 1, 8, 9, 1, 5], arr2 = [1, 4, 7] the function returns [1, 1, 1]

For arr1 = [0, 3, 4], arr2 = [2, 6] the function returns [4]

For arr1=["a","b","c","d"] , arr2=[2,2,2], the function returns ["c","c","c"]

For arr1=["a","b","c","d"], arr2=[3,0,2] the function returns ["d","a","c"]

Note that when an element inside arr2 is greater than the index of the last element of arr1 no element of arr1 should be added to the resulting array. If either arr1 or arr2 is empty, you should return an empty arr (empty list in python, empty vector in c++). Note for c++ use std::vector arr1, arr2.
"""

def find_array(arr1, arr2):
    if(len(arr2)==0 or len(arr1)==0):return []
    res = [ arr1[i]  for i in arr2  if(i< len(arr1)) ]
    return res


assert(find_array(['a', 'a', 'a', 'a', 'a'], [2, 4])== ['a', 'a'])
assert(find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7])== [1, 1, 1])
assert(find_array([1, 2, 3, 4, 5], [0])== [1])
assert(find_array(['this', 'is', 'test'], [0, 1, 2])== ['this', 'is', 'test'])
assert(find_array([0, 3, 4], [2, 6])== [4])
assert(find_array([1], [])== [])
assert(find_array([], [2])== [])
assert(find_array([], [])== [])

print("done")