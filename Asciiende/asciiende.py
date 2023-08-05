"""
The goal of this kata is to create a very simple ASCII encryption and decryption. The encryption algorithm should shift each character's charcode by the character's current index in the string (0-based).

The input strings will never require to go outside of the ASCII range.

Example:
  p | a | s | s | w | o | r | d # Plaintext
+ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 # Shift (add)
  p | b | u | v | { | t | x | k # Ciphertext
The decryption should reverse this:

  p | b | u | v | { | t | x | k # Ciphertext
- 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 # Shift (subtract)
  p | a | s | s | w | o | r | d # Plaintext
"""


# #Can use enumerate  
# def ascii_encrypt(plaintext):
#     encrypt=[ chr(ord(plaintext[i])+i) for i in range(0,len(plaintext))]
#     return "".join(encrypt)

# #Can use enumerate     
# def ascii_decrypt(encrypted):
#     decrypt=[ chr(ord(encrypted[i])-i) for i in range(0,len(encrypted))]
#     return "".join(decrypt)

#Can use enumerate  
def ascii_encrypt(plaintext):
    en=[ chr(ord(j)+i) for i,j in enumerate(plaintext)]
    return "".join(en)
    

# Can use decrypt     
def ascii_decrypt(encrypted):
    de=[ chr(ord(j)-i) for i,j in enumerate(encrypted)]
    return "".join(de)


assert(ascii_encrypt("PASSWORD")== "PBUV[TXK")
assert(ascii_encrypt("password")== "pbuv{txk")
assert(ascii_encrypt("")== "")
assert(ascii_encrypt("zzzzz")== "z{|}~")
assert(ascii_encrypt("ZZZZZ")== "Z[\\]^")
assert(ascii_encrypt("aaaa")== "abcd")
assert(ascii_encrypt("AAAA")== "ABCD")
assert(ascii_encrypt("0123456789")== "02468:<>@B")
print("done")