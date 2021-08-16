"""
all((1, 2, 3, 4, 5), greater_than_9) -> false
all((1, 2, 3, 4, 5), less_than_9)    -> True
"""

def all(seq, fun): 
    r=(list(map(lambda x:fun(x) , seq)))
    if False in r:
        return False
    else:
        return True

greater_than_9 = lambda x: x>9
less_than_9 = lambda x: x<9
assert(all((1, 2, 3, 4, 5), greater_than_9)== False)
assert(all((1, 2, 3, 4, 5), less_than_9)== True)
print("done")
