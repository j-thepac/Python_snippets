"""
Write a generic function chainer
Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).

The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.

def add10(x): return x + 10
def mul30(x): return x * 30

chain(50, [add10, mul30])
# returns 1800
"""
def add10(x): return x + 10
def mul30(x): return x * 30

def chain(init_val, functions):
    for f in functions: init_val=f(init_val)
    return init_val


assert(chain(42, [])== 42)
assert(chain(50, [mul30])== 1500)
assert(chain(50, [mul30, add10])== 1510)
assert(chain(50, [add10, mul30])== 1800)
print("done")