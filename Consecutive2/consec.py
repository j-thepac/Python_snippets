"""
You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.

docker run -it --name consec -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.10-slim python consec.py


touch dockerfile

"""

def consecutive(arr, a, b):
    try:
        r1=arr.index(a)
        r2=arr.index(b)
        if(abs(r1-r2)==1):return True
    except:
        return False
    return False



# def consecutive(arr, a, b):
#     try:
#         for i in range(0,len(arr)+1):
#             if (arr[i] == a and arr[i+1]==b):
#                 return True
#             elif(arr[i]==b and arr[i+1]==a):
#                 return True
#     except:
#         return False
#     return False
    # s="".join([str(i) for i in arr])
    # v=str(a)+str(b)
    # if (v in s or v[::-1] in s):
    #     return True
    # else:
    #     return False


# assert(consecutive([1, -4, -5, 3, -2, 11, 23, -76, 6, -7, 2], 2 ,3)== False)
assert(consecutive([1, 3, 5, 7], 3, 1)== True)
# assert(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4)== True)

print("done")