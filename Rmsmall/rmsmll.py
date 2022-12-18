"""

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
"""



def remove_smallest(numbers):
    if (numbers==[]): return []
    m=numbers.index(min(numbers))
    res=numbers[0:m]+numbers[m+1:]
    return res

def remove_smallest2(numbers):
    found=False
    res=[]
    for i in numbers:
        if(i==min(numbers) and found == False ):found =True
        else:res.append(i)
    return res
            


assert(remove_smallest([1, 2, 3, 4, 5])== [2, 3, 4, 5])
assert(remove_smallest([5, 3, 2, 1, 4])== [5, 3, 2, 4])
assert(remove_smallest([1, 2, 3, 1, 1])== [2, 3, 1, 1])
assert(remove_smallest([]), [])

print("done")