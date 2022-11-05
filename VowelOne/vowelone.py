"""
vowelOne
Write a function that takes a string and outputs a strings of 1's and 0's where vowels become 1's and non-vowels become 0's.

All non-vowels including non alpha characters (spaces,commas etc.) should be included.

Examples:

vowelOne "abceios" -- "1001110"

vowelOne "aeiou, abc" -- "1111100100"
"""

def vowel_one(s):
    return "".join(["1" if(i in "aeiou") else "0" for i in s.lower() ])


tests = [
    # [input, expected],
    ["vowelOne", "01010101"],
    ["123, arou", "000001011"],
    ["Codewars", "01010100"],
    ["Python", "000010"]
]

for inp, exp in tests:
    assert(vowel_one(inp), exp)

print("done")
