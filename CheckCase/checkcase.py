"""
Write a function that will check if two given characters are the same case.

If any of characters is not a letter, return -1
If both characters are the same case, return 1
If both characters are letters and not the same case, return 0
Examples
'a' and 'g' returns 1
'A' and 'C' returns 1
'b' and 'G' returns 0
'B' and 'g' returns 0
'0' and '?' returns -1

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python checkcase.py
docker build -t checkcase:v1 .

docker-compose up
docker-compose down
"""


def same_case(a:str, b:str): 
    if (ord(a)  in range(97,123) and ord(b) in range(97,123) ):return 1
    elif (ord(a)  in range(65,91) and ord(b)  in range(65,91) ):return 1
    elif (a.isalpha() ==False or b.isalpha()==False):return -1
    return 0



assert(same_case('C', 'B')== 1)
assert(same_case('b', 'a')== 1)
assert(same_case('d', 'd')== 1)
assert(same_case('A', 's')== 0)
assert(same_case('c', 'B')== 0)
assert(same_case('b', 'Z')== 0)
assert(same_case('\t', 'Z')== -1)
assert(same_case('H', ':')== -1)
print("done")