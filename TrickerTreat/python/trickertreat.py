"""
Task
Your job is to find out how much candy each child has, and give them each additional candy until they too have as much as the child(ren) with the most candy. You also want to keep a total of how much candy you've handed out because reasons."

Your job is to give all the kids the same amount of candies as the kid with the most candies and then return the total number candies that have been given out. If there are no kids, or only one, return -1.

In the first case (look below) the most candies are given to second kid (i.e second place in list/array), 8. Because of that we will give the first kid 3 so he can have 8 and the third kid 2 and the fourth kid 4, so all kids will have 8 candies.So we end up handing out 3 + 2 + 4 = 9.

"""

def candies(lst):
    if len(lst)<2: return -1
    return sum([max(lst)-i for i in lst])

assert(candies([5,8,6,4])==9)
assert(candies([1,2,4,6])==11)
assert(candies([1,2])==1)
assert(candies([4,2])==2)
assert(candies([1,3,3,7])==14)
assert(candies([7,7,7,7])==0)
assert(candies([17,20,50,61,42,44])==132)
assert(candies([0])==-1)
assert(candies([])==-1)
assert(candies([4])== -1)
