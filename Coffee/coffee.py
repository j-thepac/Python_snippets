"""
You love coffee and want to know what beans you can afford to buy it.

The first argument to your search function will be a number which represents your budget.

The second argument will be an array of coffee bean prices.

Your 'search' function should return the stores that sell coffee within your budget.

The search function should return a string of prices for the coffees beans you can afford. The prices in this string are to be sorted in ascending order.
"""




def search(budget, prices):
    result= sorted([p for p in prices if (p<=budget)])
    if (len(result)==0):return ""
    return ",".join(str(i) for i in result)


assert(search(3, [6, 1, 2, 9, 2])== "1,2,2")
assert(search(14, [7, 3, 23, 9, 14, 20, 7])== "3,7,7,9,14")
assert(search(0, [6, 1, 2, 9, 2])== "")
assert(search(10, [])== "")
assert(search(10, [0, 0, 0])== "0,0,0")
assert(search(0, [0, 0, 0])== "0,0,0")
assert(search(24, [24, 0, 100, 2, 5])== "0,2,5,24")
assert(search(24, [2.7, 0, 100.9, 1, 5.5])== "0,1,2.7,5.5")
assert(search(14, [17, 33, 23, 19, 19, 20, 17])== "")
assert(search(14, [13, 15, 14, 14, 15, 13])== "13,13,14,14")
print("done")