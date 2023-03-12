
def real_numbers(n):
    return len(list(filter(lambda x : x%2!=0 and x%3 !=0 and x%5!=0, range(1,n) )))

assert(real_numbers(5)== 1)
assert(real_numbers(10)== 2)
assert(real_numbers(20)== 6)
assert(real_numbers(30)== 8)
assert(real_numbers(40)== 10)
assert(real_numbers(55)== 15)
assert(real_numbers(66)== 17)
assert(real_numbers(75)== 20)
assert(real_numbers(100)== 26)
print("done")

