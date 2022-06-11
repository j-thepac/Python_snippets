"""
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
NOTES
Vowels in this context refers to: a e i o u y (including upper case)
This is indexed from [1..n] (not zero indexed!)

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.10-slim python findvowel.py
"""
def vowel_indices(word:str):
	return ([ i for i,j in enumerate((word.lower()),1) if j in "aeiouy"])

assert(vowel_indices("mmm")== [])
assert(vowel_indices("apple")== [1,5])
assert(vowel_indices("123456")== [])
assert(vowel_indices("UNDISARMED")== [1,4,6,9])
print("done")