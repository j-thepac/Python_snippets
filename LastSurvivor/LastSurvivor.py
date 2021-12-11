"""
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.

Example:

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'
Notes
The given string will never be empty.
The length of the array is always one less than the length of the string.
All numbers are valid.
There can be duplicate letters and numbers.
If you like this kata, check out the next one: Last Survivors Ep.2

docker run --name lastsurvivor -it -v $PWD:/home/app/ -w /home/app/ -p 5000:5000 python:3.8-slim python LastSurvivor.py

docker build -t lastsurvivor:v1 .
docker run -it 620c021bd5b0


docker-compose up
"""
def last_survivor(input:str, l:list)->str:
    temp_data=list(input)
    for i in l:temp_data.pop(i)
    return "".join(temp_data)


assert(last_survivor('abc', [1, 1])== 'a')
assert(last_survivor('kbc', [0, 1])== 'b')
assert(last_survivor('zbk', [2, 1])=='z')
assert(last_survivor('c', [])== 'c')
print("done")