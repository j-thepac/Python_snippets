"""
Description:
Remove all exclamation marks from the end of sentence.

Examples
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"

docker run -it -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python rmex.py


docker build -t rmex:v1 .
docker
"""

def remove(inp):
    if(inp[-1] != "!"):return inp
    while True:
        if(inp[-1] == "!"):inp=inp[0:-1]
        else: return inp

tests = [
    #[input, expected],

    ["!Hi" , "!Hi"],
    ["!Hi!" , "!Hi"],
    ["Hi! Hi!" , "Hi! Hi"],
    ["Hi" , "Hi"],
]

print("done")

for inp, exp in tests:
    assert (remove(inp)== exp)

