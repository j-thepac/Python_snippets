"""
two_oldest_ages([1, 3, 10, 0]) # should return [3, 10]

docker run -it --name twooldest -v $PWD:/home/app/ -w /home/app -p 5000:50000 python:3.9-slim python twooldest.py
"""
"""
docker build -t twooldest:v1 .
docker run -it twooldest:v1
"""

def two_oldest_ages(ages):
    return sorted(ages)[-2:]


assert(two_oldest_ages([1, 5, 87, 45, 8, 8])== [45, 87])
assert(two_oldest_ages([6, 5, 83, 5, 3, 18])== [18, 83])
assert(two_oldest_ages([10, 1])== [1, 10])
print("done")