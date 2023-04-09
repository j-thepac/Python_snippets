"""

Vanya gets bored one day and decides to enumerate a large pile of rocks. He first counts the rocks and finds out that he has n rocks in the pile, then he goes to the store to buy labels for enumeration.

Each of the labels is a digit from 0 to 9 and each of the n rocks should be assigned a unique number from 1 to n.

If each label costs $1, how much money will Vanya spend on this project?

Input/Output
[input] integer n
The number of rocks in the pile.

1  ≤  n  ≤  10^9

[output] an integer
the cost of the enumeration.

Example
For n = 13, the result should be 17.

the numbers from 1 to n are:
1 2 3 4 5 6 7 8 9 10 11 12 13
we need 17 single digit labels:
1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3
"""





import math
def rocks(n):
    lessthan = 10**len(str(n))
    loop=math.log10(lessthan)-1
    res=0
    while loop:
        res=res+9*(10**(loop-1))*(loop)
        loop=loop-1

    lastPart=(n-(lessthan/10-1))*math.log10(lessthan)
    finalres=res+lastPart
    return finalres

assert(rocks(1)==1)
assert(rocks(10)==11)
assert(rocks(13)==17)
assert(rocks(100)==192)
assert(rocks(36123011)==277872985)
print("Done")

# if(n<10): return n
# if(n<100): return (9)+(n-9)*2
# if(n<1000):return (9)+(90*2) +(n-99)*3 
# if(n<10000):return (9)+(90*2)+(900*3) +(n-999)*4
# if(n<100000):return (9)+(90*2) +(900*3) + (9000*4) +(n-9999)*5
# if(n<1000000):return (9+90*2+900*3+9000*4+90000*5) +(n-99999)*6
# if(n<10000000):return (9+90*2+900*3+9000*4+90000*5+900000*6) +(n-999999)*7
# if(n<100000000):return (9+90*2+900*3+9000*4+90000*5+900000*6+9000000*7) +(n-9999999)*8
