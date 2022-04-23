"""
A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
13 + 53 + 33 = 153

Write a method is_narcissistic(i) (in Haskell: isNarcissistic :: Integer -> Bool) which returns whether or not i is a Narcissistic Number.


docker :
docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python nar.py

docker build -t nar:v1 .
docker run -it fddaa8f78d7e

docker-compose up
"""
def is_narcissistic(i):
    l=list(str(i))
    res = sum([int(i)**len(l) for i in l])
    if(res == i):return True
    else:return False


assert(is_narcissistic(153)== True)
assert(is_narcissistic(201)== False)
assert(is_narcissistic(259)== False)
assert(is_narcissistic(371)== True)
assert(is_narcissistic(407)== True)
assert(is_narcissistic(595)== False)
assert(is_narcissistic(825)== False)
assert(is_narcissistic(1634)== True)

print("DOne")