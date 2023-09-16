"""
In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number. Numbers will not have leading zeros.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

Good luck!

Please also try Simple remove duplicates
"""

import re
import math
from functools import reduce
def solve(s:str) -> int:
    l= re.findall("[0-9]*",s)
    return max([int(i) for i in l if(i != "")])


# print(solve('gh12cdy695m1'))

assert(solve('gh12cdy695m1')==695)
assert(solve('2ti9iei7qhr5')==9)
assert(solve('vih61w8oohj5')==61)
assert(solve('f7g42g16hcu5')==42)
assert(solve('lu1j8qbbb85')==85)
print("done")

