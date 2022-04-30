"""
"hello"     -->  "hll" 
"codewars"  -->  "cdwrs" 
"goodbye"   -->  "gdby" 
"HELLO"     -->  "HELLO"


docker run -it -v $PWD:/home/apps/ -w /home/apps -p 5000:5000 python:3.9-slim rmv.py

docker build -t rmv:v1 .

"""
def shortcut( s ):
    l = list(filter(lambda x : x not in ("a","e","i","o","u") ,s))
    return "".join(l)

assert(shortcut('hello')=='hll')
print("done")