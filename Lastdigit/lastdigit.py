"""
N = 1
D = 1
result = [1]

N = 1234
D = 2
result = [3, 4]

N = 637547
D = 6
result = [6, 3, 7, 5, 4, 7]

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python lastdigit.py
docker build -t lastdigit:v1 .
"""


def solution(n,d):
    if (d<=0):return []
    l=[int(i) for i in str(n)]
    if(d >= len(l)):return l
    else:return l[len(l)-d:len(l)]


assert(solution(1,1)==[1])
assert(solution(123767,4)==[3,7,6,7])
assert(solution(0,1)==[0])
assert(solution(34625647867585,10)==[5,6,4,7,8,6,7,5,8,5])

#test.describe('d <= 0')
assert(solution(1234,0)==[])
assert(solution(24134,-4)==[])

#test.describe('d > number of digits in n')
assert(solution(1343,5)==[1,3,4,3])
print("done")