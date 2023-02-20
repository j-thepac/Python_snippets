def threeSum(nums: list[int]) -> list[list[int]]:
    res=[]
    from itertools import combinations
    res=list(filter(lambda x: sum(x)==0,sorted(list(combinations(nums , 3)))))
    print(res)
    return(res)

    # [for i in list(combinations(nums , 3)):
    #     if sum(i)==0:
    #         res.append(i)
    # print(res)
    # return res

nums = [-1,0,1,2,-1,-4]
op= [[-1,-1,2],[-1,0,1]]

assert(threeSum(nums)==op)