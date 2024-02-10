"""
ntroduction
There is a war...between alphabets!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war': dashes and dots are spread throughout the battlefield. Who will win?

Task
Write a function that accepts a fight string which consists of only small letters and * which represents a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, and when the right side wins return Right side wins!. In other cases, return Let's fight again!.

The left side letters and their power:

 w': 4
 p': 3 
 b': 2
 s': 1
The right side letters and their power:

 m': 4
 q': 3 
 d': 2
 z': 1
The other letters don't have power and are only victims.
The * bombs kill the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );

Example
AlphabetWar("s*zz");           //=> Right side wins!
AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
AlphabetWar("zzzz*s*");       //=> Right side wins!
AlphabetWar("www*www****z");  //=> Left side wins!
Alphabet war Collection
"""

import re
def alphabet_war(fight):
   res=re.sub(".\*+.|\*.|.\*","",fight) 
   l1,l2=[],[]
   d1={ 'w': 4,'p': 3 ,'b': 2,'s': 1}
   d2={ 'm': 4,'q': 3 ,'d': 2,'z': 1}
   for i in res:
    if (i in d1): l1.append(d1[i])
    elif (i in d2): l2.append(d2[i])
   if(sum(l1)>sum(l2)):return "Left side wins!"
   elif(sum(l1)<sum(l2)):return "Right side wins!"
   else: return "Let's fight again!"





assert(alphabet_war("z")=="Right side wins!")
assert(alphabet_war("****")== "Let's fight again!")
assert(alphabet_war("z*dq*mw*pb*s")== "Let's fight again!")
assert(alphabet_war("zdqmwpbs")== "Let's fight again!")
assert(alphabet_war("zz*zzs")== "Right side wins!")
assert(alphabet_war("sz**z**zs")== "Left side wins!")
assert(alphabet_war("z*z*z*zs")== "Left side wins!")
assert(alphabet_war("*wwwwww*z*")== "Left side wins!")
assert(alphabet_war("w****z")== "Let's fight again!")
assert(alphabet_war("mb**qwwp**dm")== "Let's fight again!")
print("Done")