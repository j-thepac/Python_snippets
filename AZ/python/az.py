
import string
def gimme_the_letters(sp):
    l=sp.split("-")
    if(l[0].isupper()):
       return string.ascii_uppercase[string.ascii_uppercase.index(l[0]):string.ascii_uppercase.index(l[1])+1 ]
    else:
        return string.ascii_lowercase[string.ascii_lowercase.index(l[0]):string.ascii_lowercase.index(l[1])+1 ]


assert(gimme_the_letters("a-z")== "abcdefghijklmnopqrstuvwxyz")
assert(gimme_the_letters("h-o")== "hijklmno")
assert(gimme_the_letters("Q-Z")== "QRSTUVWXYZ")
assert(gimme_the_letters("J-J")== "J")
assert(gimme_the_letters("a-b")== "ab")
assert(gimme_the_letters("A-A")== "A")
assert(gimme_the_letters("g-i")== "ghi")
assert(gimme_the_letters("H-I")== "HI")
assert(gimme_the_letters("y-z")== "yz")
assert(gimme_the_letters("e-k")== "efghijk")
assert(gimme_the_letters("a-q")== "abcdefghijklmnopq")
assert(gimme_the_letters("F-O")== "FGHIJKLMNO") 
print("Done")