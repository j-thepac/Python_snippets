"""
Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

input:   [numerator, denominator]
output:  [reduced numerator, reduced denominator]
example: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!

"""

def reduce_fraction(fraction):
    if(fraction[0]%fraction[1]==0):return (fraction[0]/fraction[1],1)
    elif(fraction[1]%fraction[0]==0):return (1,fraction[1]/fraction[0])

    less=min(fraction)//2
    i=2
    while less>=i:
        if(fraction[0]%i==0 and fraction[1]%i==0 ):
            return reduce_fraction((fraction[0]//i ,fraction[1]//i) )
        i=i+1
    return fraction



# assert(reduce_fraction((60, 20))== (3, 1))
assert(reduce_fraction((80, 120))== (2, 3))
assert(reduce_fraction((4, 2))== (2, 1))
assert(reduce_fraction((45, 120))== (3, 8))
assert(reduce_fraction((1000, 1))== (1000, 1))
assert(reduce_fraction((1, 1))== (1, 1))
print("Done")