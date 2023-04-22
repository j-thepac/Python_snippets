"""
Your job here is to write a function (keep_order in JS/CoffeeScript, keep_order in Ruby/Crystal/Python, keep_order in Julia)== which takes a sorted array ary and a value val, and returns the lowest index where you could insert val to maintain the sorted-ness of the array. The input array will always be sorted in ascending order. It may contain duplicates.

Do not modify the input.

Some examples:
keep_order([1, 2, 3, 4, 7], 5) //=> 4
                      ^(index 4)
keep_order([1, 2, 3, 4, 7], 0) //=> 0
          ^(index 0)
keep_order([1, 1, 2, 2, 2], 2) //=> 2
                ^(index 2)


"""

def keep_order(ary, val):
    if(len(ary)==0):return 0
    elif(val < ary[0]):return 0
    elif (val > ary[-1]):return len(ary)
    else:
        ind=0
        while(val > ary[ind]):ind=ind+1
    return ind




assert(keep_order([1, 2, 3, 4, 7], 5)== 4);
assert(keep_order([1, 2, 3, 4, 7], 0)== 0);
assert(keep_order([1, 1, 2, 2, 2], 2)== 2);
assert(keep_order([1, 2, 3, 4], 5)== 4);
assert(keep_order([1, 2, 3, 4], -1)== 0);
assert(keep_order([1, 2, 3, 4], 2)== 1);
assert(keep_order([1, 2, 3, 4], 0)== 0);
assert(keep_order([1, 2, 3, 4], 1)== 0);
assert(keep_order([1, 2, 3, 4], 2)== 1);
assert(keep_order([1, 2, 3, 4], 3)== 2);
assert(keep_order([-5, -4, -2, -1, 1, 2], -2)== 2);
print("done")