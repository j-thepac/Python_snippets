"""

My 5th kata, and 1st in a planned series of rock climbing themed katas.

In rock climbing (bouldering specifically), the V/Vermin (USA) climbing grades start at 'VB' (the easiest grade), and then go 'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5' etc. up to 'V17' (the hardest grade). You will be given a list (lst) of climbing grades and you have to write a function (sort_grades) to return a list of the grades sorted easiest to hardest.

If the input is an empty list, return an empty list; otherwise the input will always be a valid list of one or more grades.

Please do vote, rank, and provide any feedback on the kata.
"""

def sort_grades(lst):
    bFlag,pFlag=0,0
    if("VB" in lst):
        lst.remove("VB")   
        bFlag=1
    if("V0+" in lst):
        lst.remove("V0+")   
        pFlag=1
    result=sorted(lst,key=lambda x:int(x[1:]))

    if pFlag==1:
        if result[0]=="V0":result=[result[0]]+["V0+"]+result[1:]
        else:result=["V0+"]+result
    if bFlag==1:
        result=["VB"]+result
    return result

tests = [
    [[], []],
    [['V1'], ['V1']],
    [['V7', 'V12', 'V1'], ['V1', 'V7', 'V12']],
    [['V13', 'V14', 'VB', 'V0'], ['VB', 'V0', 'V13', 'V14']],
    [['V0+', 'V0', 'V16', 'V2', 'VB', 'V6'], ['VB', 'V0', 'V0+', 'V2', 'V6', 'V16']]
    ] 

for inp,exp in tests:
    assert(sort_grades(inp)== exp)

print("Done")