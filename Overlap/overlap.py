def merge_strings(first, second):
    for i in range(0,len(first)):
        if(first[i:] in second[0:len(first[i:])]):
            return (first[0:i]+second)
    return first+second


assert(merge_strings("abcde" ,"cdefgh" )== "abcdefgh")
assert(merge_strings("abaab" , "aabab" )== "abaabab")
assert(merge_strings("abc" , "def" )== "abcdef")
assert(merge_strings("abc" , "abc" )== "abc")
assert(merge_strings('abcd', 'dabcd')== 'abcdabcd')
print("done")