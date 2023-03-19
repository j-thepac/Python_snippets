def valid_parentheses(paren_str):
    if(len(paren_str)%2!=0):return False
    if(paren_str.count("(")!=paren_str.count(")")):return False

    try:
        while(len(paren_str)>0):
            if(paren_str[0]=='('):
                f=paren_str.find(")")
                paren_str=paren_str[1:f]+paren_str[f+1:]
            else:return False
    except:return False
    return True

assert(valid_parentheses("()") ==True)
assert(valid_parentheses(")(()))") ==False)
assert(valid_parentheses("(" ) ==False)
assert(valid_parentheses("(())((()())())") ==True)
assert(valid_parentheses("())(()")==False)
print("done")