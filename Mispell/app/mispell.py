"""
Create a function mispelled(word1, word2):

mispelled('versed', 'xersed') # returns True
mispelled('versed', 'applb') # returns False
mispelled('versed', 'v5rsed') # returns True
mispelled('1versed', 'versed') # returns True
mispelled('versed', 'versed') #returns True 
It checks if the word2 differs from word1 by at most one character.

This can include an extra char at the end or the beginning of either of words.

In the tests that expect true, the mispelled word will always differ mostly by one character. If the two words are the same, return True.
"""


def mispelled(word1,word2):
    c=0
    if( abs(len(word1)-len(word2)) > 1):return False
    elif word1 in word2 or word2 in word1: return True 
    
    for i in zip(word1,word2):
        if(i[0]!=i[-1]):c=c+1
        if c>1:return False
    return True


assert(mispelled('versed','xersed')==True)
assert(mispelled('versed','applb')==False)
assert(mispelled('versed','v5rsed')==True)
assert(mispelled('1versed','versed')==True)
assert(mispelled('versed','versed')==True)
print("Done")