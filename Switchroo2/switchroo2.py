"""
encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'

docker run -it --name switchroo2 -v $PWD:/home/app/ -w /home/app/ -p 5000:5000 python:3.9-slim python switchroo2.py

docker build -t switchroo2:v1 .
docker run -it switchroo2:v1

docker-compose up

"""
def giveascii(char:str):
    num=ord(char.lower())
    if(num >=97 and num <= 122 ):return str(num-96)
    else: return char

def encode(string):
    l=list(map(lambda x: giveascii(x),string))
    return "".join(l)




assert(encode('abc')=='123')
assert(encode('ABCD')=='1234')
assert(encode('ZzzzZ')=='2626262626')
assert(encode('abc-#@5')=='123-#@5')
assert(encode('this is a long string!! Please [encode] @C0RrEctly')=='208919 919 1 1215147 1920189147!! 161251195 [51431545] @30181853201225')

print("done")