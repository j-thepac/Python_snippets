"""
The following was a question that I received during a technical interview for an entry level software developer position. I thought I'd post it here so that everyone could give it a go:

You are given an unsorted array containing all the integers from 0 to 100 inclusively. However, one number is missing. Write a function to find and return this number. What are the time and space complexities of your solution?

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.10-slim python missing.py

"""
def missing_no(nums):
    return (set(range(0,100+1)) ^ set(nums)).pop()


nums = list(range(0,101))
nums.remove(5)
assert(missing_no(nums)== 5)

print("done")