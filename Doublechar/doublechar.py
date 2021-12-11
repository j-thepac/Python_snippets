"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

double_char("String") ==> "SSttrriinngg"

double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"

double_char("1234!_ ") ==> "11223344!!__  "

docker :
docker run -it --name doublechar -v $PWD:/home/app -w /home/app -p 8000:8000 python:3.9-slim python doublechar.py

"""
def double_char(s):
    return "".join([i*2 for i in s])


assert(double_char("String")=="SSttrriinngg")
assert(double_char("Hello World")=="HHeelllloo  WWoorrlldd")
assert(double_char("1234!_ ")=="11223344!!__  ")
print("done")