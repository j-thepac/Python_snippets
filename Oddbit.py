"""
Return 1 when ANY odd bit of x equals 1; 0 otherwise.

x is unsigned.

(Assume "0 index", aka the least significant bit is considered position 0)

Assume x is 32 bits.

Example:

any_odd(2) will return 1 because at least one odd bit is 1 (0010).
ff
"""

def any_odd(x):
   binary=str.zfill( (bin(x))[2::],4)
   return 1 if "1" in binary[::2] else 0



assert(any_odd(5)== 0)#0101 ie 1234
assert(any_odd(170)== 1)
assert(any_odd(2)== 1)