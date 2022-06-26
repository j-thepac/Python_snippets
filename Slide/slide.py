"""
Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:

each_cons([1,2,3,4], 2)
  #=> [[1,2], [2,3], [3,4]]

each_cons([1,2,3,4], 3)
  #=> [[1,2,3],[2,3,4]]
  
As you can see, the lists are cascading; ie, they overlap, but never out of order.

"""

def each_cons(lst, n):
    res= [ lst[i:i+n] for i in range(0,len(lst)) if ( len( lst[i:i+n])==n )         ]
    return res


lst1 = [3, 5, 8, 13]
assert(each_cons(lst1, 1)== [[3], [5], [8], [13]])

lst2 = [3, 5, 8, 13]
assert(each_cons(lst2, 2)==[[3,5], [5,8], [8,13]])


lst3 = [3, 5, 8, 13]
assert(each_cons(lst3, 3)== [[3,5,8], [5,8,13]])


assert(each_cons([], 3)== [])
