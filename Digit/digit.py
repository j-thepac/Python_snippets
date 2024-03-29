"""
The goal of this Kata is to reduce the passed integer to a single digit (if not already) by converting the number to binary, taking the sum of the binary digits, and if that sum is not a single digit then repeat the process.

If the passed integer is already a single digit there is no need to reduce
n will be an integer such that 0 < n < 10^20
For example given 5665 the function should return 5:

5665 --> (binary) 1011000100001
1011000100001 --> (sum of binary digits) 5


123456789 --> (binary) 111010110111100110100010101
111010110111100110100010101 --> (sum of binary digits) 16
16 --> (binary) 10000
10000 --> (sum of binary digits) 1

docker run -it --name digit -v $PWD:/home/app/ -w /home/app/ -p 5000:5000 python:3.9-slim python digit.py
docker build -t digit:v1 .

"""


#Can use count as well
def single_digit(n):
    while(n>=10):
        n=sum([int(i) for i in list(format(n,"b"))])
    return n





assert(single_digit(5665)== 5)
assert(single_digit(123456789)== 1)
assert(single_digit(443566)== 2)
print("done")

