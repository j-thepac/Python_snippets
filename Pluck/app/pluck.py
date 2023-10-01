"""

Implement a function which takes a sequence of objects and a property name, and returns a sequence containing the named property of each object.

For example:

pluck([{'a':1}, {'a':2}], 'a')        # -> [1,2]
pluck([{'a':1, 'b':3}, {'a':2}], 'b') # -> [3, None]
If an object is missing the property, you should just leave it as undefined/None in the output array.

"""


def pluck(objs, name): 
    return [d.get(name,None) for d in objs]


objs = [
    {'a':1, 'b':2, 'c': 3}
    , {'a':4, 'b':5, 'c': 6},{'a':7, 'b':8, 'c': 9}, {'a':10, 'b':11}]

assert(pluck(objs, 'a')== [1,4,7,10])
assert(pluck(objs, 'b')== [2,5,8,11])
assert(pluck(objs, 'c')== [3,6,9,None])
print("Done")