"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string)

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
import re
def validate_pin(pin):
    if(re.findall("^\d{4}$|^\d{6}$",pin)):return True
    else: return False

#Method 2 and 3
# if(re.findall("^\d{4}$",pin) or re.findall("^\d{6}$",pin)):return True
# else: return False
# if(re.findall("^\d{4}$",pin)):return True
# if(re.findall("^\d{6}$",pin)):return True
# else: return False

   
   

assert(validate_pin("12")==False)
assert(validate_pin("123")==False)
assert(validate_pin("12345")==False)
assert(validate_pin("1234567")==False)
assert(validate_pin("-1234")==False)
assert(validate_pin("-12345")==False)
assert(validate_pin("1.234")==False)
assert(validate_pin("00000000")==False)
assert(validate_pin("a234")==False)
assert(validate_pin(".234")==False)
assert(validate_pin("1234")==True)
assert(validate_pin("0000")==True)
assert(validate_pin("1111")==True)
assert(validate_pin("123456")==True)
assert(validate_pin("098765")==True)
assert(validate_pin("000000")==True)
assert(validate_pin("123456")==True)
assert(validate_pin("090909")==True)
print("done")