

def number(lines):
    res=[]
    for i,j in enumerate(lines,1):res.append("{}: {}".format(i,j))
    return res



assert number([])== []
assert number(["a", "b", "c"])== ["1: a", "2: b", "3: c"]