

#3^4
def fn(i):
    print(i)
    if(i//10==0):return i
    else:
        return (i%10)*10+fn(i//10)


  
print(fn(123))