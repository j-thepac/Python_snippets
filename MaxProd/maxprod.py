"""
Task
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

Notes
Array/list size is at least 2.

Array/list numbers could be a mixture of positives, negatives also zeroes .

Input >> Output Examples
adjacentElementsProduct([1, 2, 3]); ==> return 6
Explanation:
The maximum product obtained from multiplying 2 * 3 = 6, and they're adjacent numbers in the array.

docker run -it --name maxprod -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python maxprod.py

docker build -t maxprod:v1 .
docker-compose up
"""
def adjacent_element_product(array):
    max=array[0]*array[1]
    for i in range(0,len(array)-1,1):
        if(array[i]*array[i+1]>max):
            max= array[i]*array[i+1]
    return max

assert(adjacent_element_product([5, 8])== 40)
assert(adjacent_element_product([1, 2, 3])== 6)
assert(adjacent_element_product([1, 5, 10, 9])== 90)
assert(adjacent_element_product([4, 12, 3, 1, 5])== 48)
assert(adjacent_element_product([5, 1, 2, 3, 1, 4])== 6)
assert(adjacent_element_product([3, 6, -2, -5, 7, 3])== 21)
assert(adjacent_element_product([9, 5, 10, 2, 24, -1, -48])== 50)
assert(adjacent_element_product([5, 6, -4, 2, 3, 2, -23])== 30)
assert(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])== -14)
assert(adjacent_element_product([5, 1, 2, 3, 1, 4])== 6)
assert(adjacent_element_product([1, 0, 1, 0, 1000])== 0)
assert(adjacent_element_product([1, 2, 3, 0])== 6)
print("done")