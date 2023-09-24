"""
Your task is to implement a function that examines a given string composed of binary digits (0s and 1s). The function should return True if:

Every consecutive sequence of ones is immediately followed by an equal-length consecutive sequence of zeroes, and the number of ones is equal to the number of zeroes.

A leading zero always results in a False outcome.

Here are some examples to illustrate the expected behavior of the function: Examples

- For the input "110011100010," the function should return True because every consecutive sequence of ones (e.g., "11," "111," "1") is followed by an equal-length consecutive sequence of zeroes.

- For the input "101010110," the function should return False because the sequence of ones ("11") is not followed by an equal-length consecutive sequence of zeroes.

- "111100001100" # True 

- "111" # False

- "00110100001111 # False, although the number of zeroes and ones is equal, 
the consecutive sequence of ones (e.g., "11," "1," "1111") is not followed 
by an equal-length consecutive sequence of zeroes.
Notes

The input string will only contain digits 0 or 1.
The length of the input string (txt) will be greater than zero.
"""











from itertools import groupby

def same_length(txt):
    if(len(txt)==1 or txt[0]=="0"):return False
    l=[]
    for k,g in groupby(txt):l.append(len(list(g)))
    if(len(l)%2!=0):return False 
    for i in range(1,len(l)+1,2):
        if(l[i-1]!=l[i]):return False
    return True
        

assert(same_length('0')== False)
assert(same_length('10')== True)
assert(same_length('1010')== True)
assert(same_length('1001')== False)
assert(same_length('101')== False)
assert(same_length('110010')== True)
assert(same_length('10010')== False)
assert(same_length('110')== False)
assert(same_length('11001')== False)
assert(same_length('1011100010')== True)
assert(same_length('11100011000')== False)
assert(same_length('11101010010010')== False)
assert(same_length('00110100001111')== False)
assert(same_length('1100111000100')== False)
assert(same_length('00110011100010')== False)


print("done")