"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighbouring numbers is equal (note that 0 and n - 1 are neighbouring, too).

Given n and firstNumber/first_number/first-number, find the number which is written in the radially opposite position to firstNumber.

Example
For n = 10 and firstNumber = 2, the output should be 7


"""
def circle_of_numbers(n, fst):
    l=list(range(0,n))
    m=len(l)//2
    l1=l[0:m]
    l2=l[m:]
    d=dict(zip(l1,l2))
    d2=dict(zip(d.values(),d.keys()))
    d.update(d2)
    return d[fst]





assert(circle_of_numbers(10,2) == 7)
assert(circle_of_numbers(10,7) == 2)
assert(circle_of_numbers(4,1) == 3)
assert(circle_of_numbers(6,3) == 0)
print("DOne")