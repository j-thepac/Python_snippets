"""
docker run -it --name test  -v ${PWD}:/home/app  -w /home/app python:rc-alpine3.13 python english.py
"""

def sp_eng(sentence):
    return True if("english" in sentence.lower()) else False


assert(sp_eng("1234egn lis;h")== False);
assert(sp_eng("1234english ;k")==True);
assert(sp_eng("English")== True);

print("bye")
