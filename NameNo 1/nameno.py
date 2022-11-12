"""
In this kata, you'll be given an integer of range 0 <= x <= 99 and have to return that number spelt out in English. A few examples:

name_that_number(4)   # returns "four"
name_that_number(19)  # returns "nineteen"
name_that_number(99)  # returns "ninety nine"
Words should be separated by only spaces and not hyphens. No need to validate parameters, they will always be in the range [0, 99]. Make sure that the returned String has no leading of trailing spaces. Good luck!
"""
def name_that_number(x):
    n1={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
    n2={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen"}
    n3={20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty"}
    if(x<=10):return n1[x]


assert(name_that_number(0)== 'zero')
assert(name_that_number(4)== 'four')
assert(name_that_number(9)== 'nine')
assert(name_that_number(23)== 'twenty three')