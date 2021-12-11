"""
Description
For this Kata you will be given an array of numbers and another number n. You have to find the sum of the n largest numbers of the array and the product of the n smallest numbers of the array, and compare the two.

If the sum of the n largest numbers is higher, return "sum"
If the product of the n smallest numbers is higher, return "product"
If the 2 values are equal, return "same"

Note The array will never be empty and n will always be smaller than the length of the array.

Example
sum_or_product([10, 41, 8, 16, 20, 36, 9, 13, 20], 3) # => "product"
Explanation
The sum of the 3 highest numbers is 41 + 36 + 20 = 97

The product of the lowest 3 numbers is 8 x 9 x 10 = 720

The product of the 3 lowest numbers is higher than the sum of the 3 highest numbers so the function returns "product"

docker :
docker run -it --name sumprod -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python sumprod.py

"""
from functools import reduce

def sum_or_product(array, n):
    highest=sum(sorted(array,reverse=True)[0:n])
    lowest_list=sorted(array,reverse=False)[0:n]
    lowest=reduce(lambda x,y:x*y,lowest_list)
    if (highest>lowest):return "sum"
    elif (lowest>highest):return "product"
    else: return "same"



assert(sum_or_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)== "sum")
assert(sum_or_product([10, 41, 8, 16, 20, 36, 9, 13, 20], 3)== "product")
assert(sum_or_product([10, 20, 3, 30, 5, 4], 3)== "same")
assert(sum_or_product([23, 7, 12, 9, 12, 17, 3, 8, 5, 2, 23], 3)== "sum")
assert(sum_or_product([13, 8, 22, 39, 12, 6, 14, 19, 4, 7, 33], 4)== "product")
assert(sum_or_product([-10, 42, 5, -7, 3, 18], 4)== "product")
assert(sum_or_product([-4, -1, 5, -7, -2, 6, 20, 23, 7], 4)== "same")
assert(sum_or_product([-13, 2, -15, 5, -17, 3], 3)== "sum")
assert(sum_or_product([-100, -70, -50, -20, 10, 40, 70, 100], 6)== "product")
assert(sum_or_product([4, 8, 12, 7, 8, -2, 3, -10], 2)== "same")
print("done")