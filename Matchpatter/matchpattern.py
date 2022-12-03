"""
Example of use:

predicate = find_matched_by_pattern('acs')
predicate('access') # True
predicate('sacrifice') # False 
Examples of inputs/outputs:

Pattern:  Word:     Match:
acs       access    true
          ascces    false
          scares    false
vvl       veturvel  true
          velivel   false
bmb       bomb      true
          babyboom  false
"""

def find_matched_by_pattern(pattern):
    np='.*'.join(list(pattern))
    def fn(s:str):
        import re
        res= re.findall(np,s)
        return len(res)>0
    return fn

predicate = find_matched_by_pattern('acs')
assert(predicate('access')== True)
assert(predicate('sacrifice')== False)
print("done")

