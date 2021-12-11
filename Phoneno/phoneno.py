"""
Write a function that accepts an array of 10 integers (between 0 and 9)== that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

docker run -it --name phoneno -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python phoneno.py
 docker build -t phoneno:v1 .
"""

def create_phone_number(n):
    n="".join(str(i) for i in n)
    return "({}) {}-{}".format(n[0:3],n[3:6],n[6:])

assert(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])== "(123) 456-7890")
assert(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])== "(111) 111-1111")
assert(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])== "(123) 456-7890")
assert(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])== "(023) 056-0890")
assert(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])== "(000) 000-0000")
print("done")