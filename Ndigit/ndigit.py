"""
Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).

Note
If num is negative, ignore its sign and treat it as a positive value
If nth is not positive, return -1
Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0
Examples(num, nth --> output)
5673, 4 --> 5
129, 2 --> 2
-2825, 3 --> 8
-456, 4 --> 0
0, 20 --> 0
65, 0 --> -1
24, -8 --> -1

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python ndigit.py
docker build -t ndigit:v1 .

docker-compose up
"""
def find_digit(num, nth): 
    nth=nth-1
    num=abs(num)
    num=str(num)[::-1]
    if (nth < 0):return -1 
    elif(len(str(num)) <= nth): return 0 
    return int(num[nth])

assert(find_digit(5673, 4)== 5)
assert(find_digit(129, 2)== 2)
assert(find_digit(-2825, 3)== 8)
assert(find_digit(0, 20)== 0)
assert(find_digit(65, 0)== -1)
assert(find_digit(24, -8)== -1)

assert(find_digit(-456, 5)== 0)
assert(find_digit(-1234, 2)== 3)
assert(find_digit(-5540, 1)== 0)

assert(find_digit(678998, 0)== -1)
assert(find_digit(-67854, -57)== -1)
assert(find_digit(0, -3)== -1)

assert( find_digit(44790, 6)==0)
print("done")