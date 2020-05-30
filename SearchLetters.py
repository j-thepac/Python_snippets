import unittest
def change(st):
    res = ["0"] * 26
    for i in st.lower():
        if (122 >= ord(i) >= 97):
            res[ord(i) - 97] = "1"
    print(res)
    return "".join(res)


#@test.describe('Example Tests')
def example_tests():
    assert(change("a **&  bZ")== "11000000000000000000000001")
    assert(change('Abc e  $$  z')=="11101000000000000000000001")
    assert(change("!!a$%&RgTT")=="10000010000000000101000000")
    assert(change("")=="00000000000000000000000000")
    assert(change("abcdefghijklmnopqrstuvwxyz")=="11111111111111111111111111")
    assert(change("aaaaaaaaaaa")=="10000000000000000000000000")
    assert(change("&%&%/$%$%$%$%GYtf67fg34678hgfdyd")=="00010111000000000001000010")
