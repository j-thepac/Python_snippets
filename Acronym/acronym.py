"""
Write function which takes a string and make an acronym of it.

Rule of making acronym in this kata:

split string to words by space char
take every first letter from word in given string
uppercase it
join them toghether
Eg:

Code wars -> C, w -> C W -> CW
"""



def to_acronym(inp):
    return "".join([ i[0].upper() for i in inp.split()])

tcs=[
("Code Wars", "CW"),
("Water Closet", "WC"),
("Portable Network Graphics", "PNG"),
("PHP: Hypertext Preprocessor", "PHP"),
("hyper text markup language", "HTML")
]

for tc in tcs:
    inp,out=tc
    assert(to_acronym(inp)==out)

print("done")