"""
In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.

"""

def solve(s):
    uppercase,lowercase,numbers,special=0,0,0,0
    for i in s:
        if(i.isdigit()):numbers=numbers+1
        elif( i.isupper()):uppercase=uppercase+1
        elif( i.islower()):lowercase=lowercase+1
        else :special=special+1
    return ([uppercase,lowercase,numbers,special])




assert(solve("Codewars@codewars123.com")==[1,18,3,2])
assert(solve("bgA5<1d-tOwUZTS8yQ")==[7,6,3,2])
assert(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H")==[9,9,6,9])
assert(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD")==[15,8,6,9])
assert(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe")== [10,7,3,6])
assert(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft")== [7,13,4,10])
print("done")