"""
Write a function that returns only the decimal part of the given number.

You only have to handle valid numbers, not Infinity, NaN, or similar. Always return a positive decimal part.

Examples
get_decimal(2.4)  # 0.4
get_decimal(-0.2) # 0.2


docker run -it --name decimalpart -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python decimalpart.py

docker build -t decimalpart:v1 .


"""


def get_decimal(n): 
    print(abs(n %int(n)))
    return abs(n %int(n))



assert(get_decimal(10)== 0)
# assert(get_decimal(-1.2)== 0.2)
assert(get_decimal(4.5)== 0.5)

print("done")