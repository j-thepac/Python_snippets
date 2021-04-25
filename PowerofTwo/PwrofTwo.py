def powers_of_two(n):
    return list(map(lambda x:2**x,list(range(0,n+1))))


assert (powers_of_two(1)== [1, 2])
assert(powers_of_two(4)== [1, 2, 4, 8, 16])

print("Done")