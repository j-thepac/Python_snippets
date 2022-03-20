"""
NOTE: All input strings will contain only two words. Spoonerisms can be more complex. 
For example, three-word phrases in which the first letters of the first and last words are swapped: "pack of lies" --> "lack of pies" or more than one letter from a word is swapped: "flat battery --> "bat flattery" You are NOT expected to


docker
docker run -it --name spoon -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python spoonerism.py

docker build -t spoon:v1 .

docker-compose up
"""


def spoonerize(words:str):
    l=words.split(" ")
    newword= (l[1][0]+l[0][1:]+" "+l[0][0]+l[1][1:])
    return newword

assert(spoonerize("nit picking")== "pit nicking")
assert(spoonerize("wedding bells")== "bedding wells")
assert(spoonerize("jelly beans")== "belly jeans")
assert(spoonerize("pop corn")== "cop porn")
print("done")