"""
Description:
Complete function findSequences. It accepts a positive integer n. Your task is to find such integer sequences:

Continuous positive integer and their sum value equals to n

For example, n = 15 
valid integer sequences:
[1,2,3,4,5]  (1+2+3+4+5==15)
[4,5,6]          (4+5+6==15)
[7,8]              (7+8==15)
The result should be an array [sequence 1,sequence 2...sequence n], sorted by ascending order of the length of sequences; If no result found, return [].

Some examples:

findSequences(3) === [[1,2]]
findSequences(15) === [[7,8],[4,5,6],[1,2,3,4,5]]
findSequences(20) === [[2, 3, 4, 5, 6]]
findSequences(100) === [[18, 19, 20, 21, 22], [9, 10, 11, 12, 13, 14, 15, 16]]
findSequences(1) === []
"""

def find_sequences(n):
    n1=n//2
    res=[]
    for i in range(0,n1):
        tempRes=[]
        while True:
            i=i+1
            tempRes.append(i)
            if(sum(tempRes)==n):
                res.append(tempRes)
                break
            elif (sum(tempRes)>n):break
    return res[::-1]

def find_sequences2(n):
    n1=n//2
    res=[]
    for i in range(1,n1+1):
        tempRes=[]
        for j in range(i,n-1):
            tempRes.append(j)
            if(sum(tempRes)>n):break
            elif(sum(tempRes)==n):
                res.append(tempRes)
                break
    print(n,res)
    return res[::-1]

test_cases = [
    # (  3, [[1,2]]),
    ( 15, [[7,8], [4,5,6], [1,2,3,4,5]]),
    ( 20, [[2,3,4,5,6]]),
    (100, [[18,19,20,21,22], [9,10,11,12,13,14,15,16]]),
    (  1, []),
]   


for n, expected in test_cases:
    assert(find_sequences(n)== expected)

print("Done")