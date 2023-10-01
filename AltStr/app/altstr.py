"""

ask
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.

longest_substring("20") ➞ "2"

longest_substring("") ➞ ""
Input Constraints
0 <= len(digits) <= 10^5
"""

# def longest_substring(digits):
#     res,temp,flag=[],"",False
#     for i in range(0,len(digits)+1):
#         d1=int(digits[i])
#         d2=int(digits[i+1])
#         if(d1 ^ d2):
#             temp+=str(d1)
#             flag=True
#         else:
#             if(flag==True and d2 ^ int(digits[i-1])):temp+=str(int(digits[i-1]))
#             flag =False
#             res.append(temp)
#             temp =""
#     print(res)
#     return res
def longest_substring(digits):
    if(len(digits)==2):return digits[0]
    elif (len(digits)==0):return ""
    res,temp=[],""
    flag=False
    for i in range(0,len(digits)-1):
        if(int(digits[i])%2 ^ int(digits[i+1])%2):
            temp+=str(digits[i])
            flag=True
        else:
            if(flag==True and int(digits[i])%2 ^ int(digits[i-1])%2 ):
                temp+=str(digits[i])
                flag=False
            res.append(temp)
            temp=""
    
    if flag:temp+=str(digits[-1])
    res.append(temp)
    print(res)
    return sorted(res,key=lambda x:len(x),reverse=True)[0]


# longest_substring("225424272163254474441338664823")
# assert(longest_substring("225424272163254474441338664823")== "272163254")
# assert(longest_substring("594127169973391692147228678476")== "16921472")
# assert(longest_substring("721449827599186159274227324466")== "7214")
# assert(longest_substring("20")== "2")
# assert(longest_substring("")== "")
assert(longest_substring("1476474439981628014303")== "014303")

