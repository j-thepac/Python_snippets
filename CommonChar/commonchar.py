# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:
#
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]


def commonChars(words: list[str]) -> list[str]:
    from collections import Counter
    res=[]
    res2=[]
    for word in words:
        res.append(Counter(word))

    for




assert(commonChars(["bella","label","roller"])==["e","l","l"])
