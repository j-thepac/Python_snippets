"""
Overview
Many people know that Apple uses the letter "i" in almost all of its devices to emphasize its personality.

And so John, a programmer at Apple, was given the task of making a program that would add that letter to every word. Let's help him do it, too.

Task:
Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the word. For example we get the word "Phone", so we must return "iPhone". But we have a few rules:

The word should not begin with the letter "I", for example Inspire.
The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace. ("y" is considered a consonant)
The first letter should not be lowercase, for example road.
If the word does not meet the rules, we return "Invalid word".

docker:
docker run -it --name iword -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.8-slim python imeverywhere.py

dockerfile:
    docker build -t iword:v1 .
    docker run -it image_id
"""
import re

def i(word):
    invalid='Invalid word'
    if(word=="" or word[0].islower() or word[0]=="I"): return invalid


    vcount=len(re.findall("[aeiou]",word.lower()))
    ccount=len(re.findall(r"[^aeiou]",word.lower()))
    if(vcount>=ccount): return invalid
    return ("i"+word)



assert(i('')== 'Invalid word')
assert(i('Inspire')== 'Invalid word')
assert(i('East')== 'Invalid word')
assert(i('Peace')== 'Invalid word')
assert(i('Phone')== 'iPhone')
assert(i('road')== 'Invalid word')
print("done")