"""
Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a multiple of three.

Return n if the input is already a multiple of three, and return null/nil/None/-1 if no such number exists.

Examples
1      => null
25     => null
36     => 36
1244   => 12
952406 => 9

docker
docker run -it --name mulThree -v $PWD:/home/app/ -w /home/app/ -p 5000:5000 python:3.9-slim python mulThree.py


dockerfile
docker build -t mulThree:v1 .

docker-compose
docker-compose up

"""
def prev_mult_of_three(n):
    while (n>0):
        if (n%3==0 ):return n
        n=(n//10)
    return None

assert(prev_mult_of_three(1)== None)
assert(prev_mult_of_three(25)== None)
assert(prev_mult_of_three(36)== 36)
assert(prev_mult_of_three(1244)== 12)
assert(prev_mult_of_three(952406)== 9)

print("done")