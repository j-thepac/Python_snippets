"""
Task
Write a function which takes a input string s and return a string in the following way:

                  C|                          R|
                  |O                          n|
                  D|                          d|
   "Codewars" =>  |E       "Rnd Te5T"  =>      |
                  W|                          T|
                  |A                          |e
                  R|                          5|
                  S|                          T|


Notes:

List all the Vowels on the right side of |
List every character except Vowels on the left side of |
Case doesn't matter
Each line is seperated with \n
Invalid input ( undefined / null / integer ) should return an empty string


Docker :
docker run --name sorvowels -it -v $PWD:/home/app/ -w /home/app python:3.8-slim python sortvowels.py
"""


def sort_vowels(s):
    if(s =="" or s==None or isinstance(s,int)):return ''
    vowels=list("aeiouAEIOU")
    result=list(map(lambda x:  "|"+x if(x in vowels) else x+"|" ,str(s)))
    return "\n".join(result)

assert(sort_vowels('Codewars')== 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|')
assert(sort_vowels('Rnd Te5T')== 'R|\nn|\nd|\n |\nT|\n|e\n5|\nT|')
assert(sort_vowels(1337)== '')
assert(sort_vowels(None)== '')
print("done")