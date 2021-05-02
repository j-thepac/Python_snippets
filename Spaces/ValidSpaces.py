def valid_spacing(s:str):
    if(s.strip()!=s):return False
    elif((len(s.split())-1) !=s.count(" ")):return False
    else:return True
    
    


assert(valid_spacing('Hello world')==True)
assert(valid_spacing(' Hello world')==False)
assert(valid_spacing('Hello  world ')==False)
assert(valid_spacing('Hello')==True)
assert(valid_spacing('Helloworld')==True)
print("done")