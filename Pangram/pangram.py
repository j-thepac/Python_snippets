
"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(s):
    result=True
    for i in range(97,123,1):
        if(s.lower().find(chr(i))==-1):
            result=False
            break
    return result


assert(is_pangram("The quick, brown fox jumps over the lazy dog!")== True)
assert(is_pangram("1bcdefghijklmnopqrstuvwxyz")== False)
print("Done")