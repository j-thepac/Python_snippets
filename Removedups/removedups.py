"""
Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]

More examples can be found in the test cases.

Docker :

docker run -it --name removedups -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python removedups.py

docker build -t removedups:v1 .

docker-compose up
docker compose down
"""

def solve(arr:list): 

    for i in range(0,len(arr),1):
        if (arr.count(arr[i])>1):
            arr[i]="replaced"

    return list(filter(lambda x:x!="replaced",arr))



assert(solve([3,4,4,3,6,3])==[4,6,3])
assert(solve([1,2,1,2,1,2,3])==[1,2,3])
assert(solve([1,2,3,4])==[1,2,3,4])
assert(solve([1,1,4,5,1,2,1])==[4,5,2,1])

print("done")