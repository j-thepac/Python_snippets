"""
Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.


"""



def consonant_count(s):
    import re
    return len((re.findall("[^aeiou0-9\s_\^\$\&\#\\\]",s.lower())))


if __name__ == "__main__":

    assert(consonant_count('')== 0);
    assert(consonant_count('aaaaa')== 0);
    assert(consonant_count('XaeiouX')== 2);
    assert(consonant_count('Bbbbb')== 5);
    assert(consonant_count('helLo world')== 7);
    assert(consonant_count('h^$&^#$&^elLo world')== 7);
    assert(consonant_count('0123456789')== 0)
    assert(consonant_count('012345_Cb')== 2)
    print("Done")