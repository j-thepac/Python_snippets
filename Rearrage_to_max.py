def max_redigit(num): 
    if(num<=0):return None
    l_res=sorted(str(num),reverse=True)
    if (len(l_res)!=3):return None
    res=int("".join(l_res))
    return res


assert (max_redigit(99)==None)