
"""
Make a function "add" that will be able to sum elements of list continuously and return a new list of sums.

For example:

add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like 
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]

"""

def add(lst):
    return [sum(lst[0:i]) for i in range(1,len(lst)+1)]

assert(add([5,10,15,20,25,30,35,40])==[5, 15, 30, 50, 75, 105, 140, 180])
assert(add([6,12,18,24,30,36,42])==[6, 18, 36, 60, 90, 126, 168])
assert(add([7,14,21,28,35,42,49,56])==[7, 21, 42, 70, 105, 147, 196, 252])
assert(add([8,16,24,32,40,48,56,64])==[8, 24, 48, 80, 120, 168, 224, 288])
assert(add([9,18,27,36,45,54])==[9, 27, 54, 90, 135, 189])

print("Done")
