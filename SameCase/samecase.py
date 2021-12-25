"""
Write a function that will check if two given characters are the same case.

'a' and 'g' returns 1

'A' and 'C' returns 1

'b' and 'G' returns 0

'B' and 'g' returns 0

'0' and '?' returns -1

If any of characters is not a letter, return -1.

If both characters are the same case, return 1.

If both characters are letters and not the same case, return 0.
docker run -it --name samecase -p 5000:5000 -v $PWD:/home/app -w /home/app python:3.9-slim python samecase.py
"""
def same_case(a, b): 
    if(len(a)>1 or len(b) > 1) :return -1
    elif(ord(a) not in range(65,91) and ord(a)  not in range(97,123) ):return -1
    elif(ord(b) not in range(65,91) and ord(b)  not in range(97,123) ): return -1 # (ord(b)  in range(97,123)
    if( (a.isupper() and b.islower()) or (a.islower() and b.isupper()) ):return 0
    else:return 1

assert(same_case('C', 'B')== 1)
assert(same_case('b', 'a')== 1)
assert(same_case('d', 'd')== 1)
assert(same_case('A', 's')== 0)
assert(same_case('c', 'B')== 0)
assert(same_case('b', 'Z')== 0)
assert(same_case('\t', 'Z')== -1)
print("done")