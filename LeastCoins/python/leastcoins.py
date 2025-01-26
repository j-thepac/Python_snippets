
def fn(amt,c):
    l=[]
    c.sort(reverse=True)
    for i in c:
        if(amt>=i):
            nos=amt//i
            amt=amt%i
            l.extend(nos*[i])
    return l

def fn2(amount, coins):
    coins.sort(reverse=True)
    coins_used = []
    for coin in coins:
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin
    return coins_used

print(fn(63, [1, 2, 5, 10, 20, 50]))
print(fn2(63, [1, 2, 5, 10, 20, 50]))