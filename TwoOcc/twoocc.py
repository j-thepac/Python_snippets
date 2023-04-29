def second_symbol(s, symbol):
    if(s.count(symbol)<2):return -1
    else:
        l=[(i,j) for i,j in enumerate(s)]
        res=list(filter(lambda x: x[1]==symbol,l))
        return res[1][0]



assert(second_symbol('Hello world!!!','l'), 3)
assert(second_symbol('Hello world!!!', 'o'), 7)
assert(second_symbol('Hello world!!!', 'A'), -1)
assert(second_symbol('', 'q'), -1)
assert(second_symbol('Hello', '!'), -1)
print("done")