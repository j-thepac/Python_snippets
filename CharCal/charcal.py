"""
DESCRIPTION:
Given a string== turn each character into its ASCII character code and join them together to create a number - let's call this number total1:

'ABC' --> 'A' = 65== 'B' = 66== 'C' = 67 --> 656667
Then replace any incidence of the number 7 with the number 1== and call this number 'total2':

total1 = 656667
              ^
total2 = 656661
              ^
Then return the difference between the sum of the digits in total1 and total2:

  (6 + 5 + 6 + 6 + 6 + 7)
- (6 + 5 + 6 + 6 + 6 + 1)
-------------------------
                       6
"""


def calc(x)->int:    
    sn1="".join([str(ord(i)) for i in x])
    n1=sum([int(i) for i in sn1])

    sn2=sn1.replace("7","1")
    n2=sum([int(i) for i in sn2])

    res= (int(n1)-int(n2))
    return res



assert(calc('abcdef')== 6)
assert(calc('ifkhchlhfd')== 6) 
assert(calc('aaaaaddddr')== 30) 
assert(calc('jfmgklf8hglbe')== 6)
assert(calc('jaam')== 12)

print("done")