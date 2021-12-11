def converter(c:chr):
    post_add_asc=ord(c)+10
    if (post_add_asc > 122):
        return chr(post_add_asc-123+97)
    else:return chr(post_add_asc)
    

def move_ten(v:str):
    return "".join(list(map(lambda x:converter(x),v)))


assert (move_ten("testcase")== "docdmkco")
assert (move_ten("weneedanofficedog")== "goxoonkxyppsmonyq")