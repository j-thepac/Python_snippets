"""
Kate likes to count words in text blocks. By words she means continuous sequences of English alphabetic characters (from a to z ). Here are examples:

Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp. contains "words" ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd', 'or', 'K', 'mp']

Kate doesn't like some of words and doesn't count them. Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.

Today Kate's too lazy and have decided to teach her computer to count "words" for her.

Example Input 1
Hello there, little user5453 374 ())$.

Example Output 1
4

docker 
docker run -it --name katecount -v $PWD:/home/app/ -w /home/app/ -p 5000:5000 python:3.8-slim python katewords.py

docker build -t katewords:v1 .

docker-compose up

"""
import re
def word_count(s:str):
    neg =[ "a", "the", "on", "at", "of", "upon", "in", "as", " ",""]
    res=re.sub("[^a-zA-Z ]"," ",s)
    count =sum([1 for i in res.lower().split(" ") if i not in neg ])
    return count

assert(word_count("hello there")== 2)
assert(word_count("hello there and a hi")== 4)
assert(word_count("I'd like to say goodbye")== 6)
assert(word_count("Slow-moving user6463 has been here")== 6)
assert(word_count("%^&abc!@# wer45tre")== 3)
print("done")