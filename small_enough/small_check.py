"""
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.
"""

def small_enough(array, limit):
    return all(list(map(lambda x:x<=limit,array)))

assert (small_enough([78, 33, 22, 44, 88, 9, 6], 87) == False)
assert (small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == True)
print("done ")