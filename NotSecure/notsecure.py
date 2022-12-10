"""
n this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore

"""

def move_zeros(l):
    size=len(l)
    for i in range(0,l.count(0)):l.remove(0)
    for i in range(0,size-len(l)):l.append(0)
    return l



assert(move_zeros( [1, 2, 0, 1, 0, 1, 0, 3, 0, 1])==[1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
assert(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])==[9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
assert(move_zeros([0, 0])==[0, 0])
assert(move_zeros([0])==[0])
assert(move_zeros([])== [])

print("done")