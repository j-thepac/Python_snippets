"""
Task:
You need to write a function grid that returns an alphabetical grid of size NxN, where a = 0, b = 1, c = 2....

Examples:
grid(4)

a b c d
b c d e
c d e f
d e f g
grid(10)

a b c d e f g h i j
b c d e f g h i j k
c d e f g h i j k l
d e f g h i j k l m
e f g h i j k l m n
f g h i j k l m n o
g h i j k l m n o p
h i j k l m n o p q
i j k l m n o p q r
j k l m n o p q r s
Notes:
After "z" comes "a"
If function receive N < 0 should return:
None


docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python grid.py
docker-compose up
"""

#a=97 , z=122
def grid(N):
    if (N<0): return None
    res=""
    d={i-97:chr(i) for i in range(97,123)}

    for i in range(0,N):
        for j in range(0,N):
            res=res+d[(i+j)%26]+" "
        res=res.strip()+"\n"
    print(res)
    return res.strip()



assert(grid(0)== '')
assert(grid(1)== 'a')
assert(grid(2)== 'a b\nb c')
assert(grid(4)== 'a b c d\nb c d e\nc d e f\nd e f g')
assert(grid(6)== 'a b c d e f\nb c d e f g\nc d e f g h\nd e f g h i\ne f g h i j\nf g h i j k')

assert(grid(-1)== None)
assert(grid(-5)== None)
print("done")
# grid(28)