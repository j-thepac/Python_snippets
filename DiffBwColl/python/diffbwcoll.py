"""
The collections can contain any character and can contain duplicates.

Example
A = [a, a, t, e, f, i, j]

B = [t, g, g, i, k, f]

difference = [a, e, g, j, k]
"""


# return a sorted list with the difference
def diff(a, b):
    return sorted(list(set(a).symmetric_difference(b)))




assert(diff(['a','b'], ['a','b'])==[])
a = ['a','b']
b = []
assert(diff(a, b)==a)


a = []
b = ['a','b']
assert(diff(a, b)==b)




a = ['a','b','z']
b = ['a','b']
assert(diff(a, b)==['z'])


a = ['a','b','z','d','e','d']
b = ['a','b', 'j','j']
assert(diff(a, b)==['d','e','j','z'])

print("Done")