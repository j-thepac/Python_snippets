"""
You have to create a function calcType, which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are: "addition", "subtraction", "multiplication", "division".

Example:
calcT_type(1, 2, 3) -->   1 ? 2 = 3   --> "addition"

docker run -it --name calc -v $PWD:/home/app/ -w /home/app -p 5000:5000 python:3.9-slim python calc.py
docker build -t calc:v1 .
"""
def calc_type(a, b, res):
    if (a+b == res):return ("addition")
    elif (a-b == res):return ("subtraction")
    elif (a*b == res):return ("multiplication")
    else:return ("division")


assert(calc_type(1, 2, 3)== "addition")
assert(calc_type(10, 5, 5)== "subtraction")
assert(calc_type(10, 4, 40)== "multiplication")
assert(calc_type(9, 5, 1.8)== "division")
print("done")