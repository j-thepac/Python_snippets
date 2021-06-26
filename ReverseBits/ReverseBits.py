"""

Write a function that reverses the bits in an integer.

For example== the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

You can assume that the number is not negative.

docker:
docker run -it --name reversebits -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.8-slim python ReverseBits.py

"""
def reverse_bits(n):
   return int( bin(n)[2:][::-1] ,2)


assert(reverse_bits(417)== 267)
assert(reverse_bits(267)== 417)
assert(reverse_bits(0)== 0)
assert(reverse_bits(2017)== 1087)
assert(reverse_bits(1023)== 1023)
assert(reverse_bits(1024)== 1)
print("done")