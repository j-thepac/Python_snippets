"""
How many urinals are free?
In men's public toilets with urinals, there is this unwritten rule that you leave at least one urinal free between you and the next person peeing. For example if there are 3 urinals and one person is already peeing in the left one, you will choose the urinal on the right and not the one in the middle. That means that a maximum of 3 people can pee at the same time on public toilets with 5 urinals when following this rule (Only 2 if the first person pees into urinal 2 or 4).

"""




def get_free_urinals(urinals):
    if urinals.count('11'): return -1
    temp=urinals
    c=0
    if urinals=="0":return 1
    elif urinals =="1": return 0

    if temp[0]=="0" and temp[1]=="0":
        temp="1"+temp[1:]
        c+=1
    for i in range(1,len(temp)-1):
        if temp[i-1]=="0" and temp[i]=="0" and temp[i+1]=="0":
            temp=temp[0:i]+"1"+temp[i+1:]  
            c+=1 
    if temp[-2]=="0" and temp[-1]=="0":
        temp=temp[0:-1]+"1"
        c+=1
    return c




    # t1=re.sub("^10|01$","",urinals)

    # # return urinals.replace('10', '1').replace('01', '1').replace('00','0').count('0')
    # l=[t1[i:i+2] for i in range(0,len(t1),2)]
    # count=0
    # for i in l:
    #     if(i=="00"):count+=1
    # return count
    # tot=urinals.count("1")
    # first=urinals.index("1")
    # if(first==0):


if(__name__=="__main__"):

    test_cases = [

            ('10001', 1),
            ('1001', 0),
            ('00000', 3),
            ('0000', 2),
            ('01000', 1),
            ('00010', 1),
            ('10000', 2),
            ('1', 0),
            ('0', 1),
            ('10', 0),
        
    ]


    for urinals, expected in test_cases:
        assert(get_free_urinals(urinals)==expected)


    print("done")