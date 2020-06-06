"""
A trick I learned in elementary school to determine whether or not a number was divisible by three is to add all of the integers in the number together and to divide the resulting sum by three. If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.

Given a series of numbers as a string, determine if the number represented by the string is divisible by three.

You can expect all test case arguments to be strings representing values greater than 0.

Example:

"123"      -> true
"8409"     -> true
"100853"   -> false
"33333333" -> true
"7"        -> false
"""

def divisible_by_three(st):
    if len(str(st))<2:
        return 1 if (int(st)%3)==0 else 0
    from functools import reduce
    return True if (reduce(lambda x,y:int(x)+int(y),str(st))%3==0) else False


def basic_tests():
    assert(divisible_by_three('123')== True)
    assert(divisible_by_three('19254')== True)
    assert(divisible_by_three('88')== False)
    assert(divisible_by_three('1')== False)


basic_tests()