"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2 


docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python sumdigit.py
docker build -t sumdigit:v1 .

docker-compose up
"""

def digital_root(n):
    while(n>9):n=sum([int(i) for i in str(n)])
    return n
assert(digital_root(16) == 7)
assert(digital_root(942) == 6)
assert(digital_root(132189) == 6)
assert(digital_root(493193) == 2)
print("done")
