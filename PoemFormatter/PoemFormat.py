"""
You have a collection of lovely poems. Unfortuantely they aren't formatted very well. They're all on one line, like this:

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
What you want is to present each sentence on a new line, so that it looks like this:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.


docker
docker run -it --name poem -v $PWD:/home/app/ -w /home/app -p 5000:5000 python:3.8-slim python PoemFormat.py

docker build -t poem:v1 .
"""

def format_poem(poem):
    return poem.replace(". ",".\n")


#Test
#
assert(format_poem('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.')== 'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.')
assert(format_poem("Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules.")== "Flat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.")
assert(format_poem("Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess.")== "Although practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.")

print("done")
