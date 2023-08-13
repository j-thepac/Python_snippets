"""
Create a function that checks if the first argument n is divisible by all other arguments (return true if no other arguments)

Example:

(6,1,3)--> true because 6 is divisible by 1 and 3
(12,2)--> true because 12 is divisible by 2
(100,5,4,10,25,20)--> true
(12,7)--> false because 12 is not divisible by 7
This kata is following kata: http://www.codewars.com/kata/is-n-divisible-by-x-and-y


"""


def is_divisible(x,*y):
#     return all([  1 if x%i ==0 else 0 for i in y] )   #Method 1

#     for i in y:                                       #Method 2
#         if x%i !=0 : return 0
#     return 1
    return len(list( filter(lambda i: x%i!=0,y))) ==0


assert(is_divisible(3,3,4)==False);
assert(is_divisible(12,3,4)==True);
assert(is_divisible(8,3,4,2,5)==False);
assert(is_divisible(48,3,4,2)==True);
assert(is_divisible(100,5,10,20,25)==True);
assert(is_divisible(100,5)==True);
assert(is_divisible(4,4,2,4,4,4,4,4,4)==True);
assert(is_divisible(5,2)==False);
assert(is_divisible(17,17,17,17)==True);
assert(is_divisible(17,1)==True);

print("Done")