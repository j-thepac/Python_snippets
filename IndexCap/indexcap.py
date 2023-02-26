"""
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.

Good luck!

"""
def capitalize(s, ind):
    l=list(s)
    for i in ind:
        if(i <= len(l)):l[i]=l[i].upper()
    return "".join(l)

assert(capitalize("abcdef",[1,2,5])=='aBCdeF')
assert(capitalize("abcdef",[1,2,5,100])=='aBCdeF')
assert(capitalize("codewars",[1,3,5,50])=='cOdEwArs')
assert(capitalize("abracadabra",[2,6,9,10])=='abRacaDabRA')
assert(capitalize("codewarriors",[5])=='codewArriors')
print("done")