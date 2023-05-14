"""
You have a list of integers. The task is to return the maximum sum of the elements located between two negative elements. No negative element should be present in the sum. If there is no such sum: -1 for Python, C++, JavaScript, Java, CoffeeScript and COBOL, Nothing for Haskell, None for Rust.

Example 1
[4, -1, 6, -2, 3, 5, -7, 7] -> 8
     ^      ^         ^
"""
def getSum(s:str):
    if(s==""):return ""
    elif(len(s)==1):return int(s)
    else:
        return sum(list(map(lambda x:int(x),list(s))))

def max_sum_between_two_negatives(arr):
    if len(list(filter(lambda x: x>0,arr)))<2:return -1

    temp=list(map((lambda x: str(x) if(x>=0) else "x"),arr))
    temp2="".join(temp).split("x")
    res= [getSum(i) for i in temp2]
    return max(res[1:])



assert(max_sum_between_two_negatives([-1,6,-2,3,5,-7])== 8)
# assert(max_sum_between_two_negatives([5,-1,-2])== 0)
# assert(max_sum_between_two_negatives([1,-2])== -1)