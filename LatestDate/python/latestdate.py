"""
Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59" (19:25 is also a valid time, but 21:59 is later)
Notes
Result should be a valid 24-hour time, between 00:00 and 23:59.
Only inputs which have valid answers are tested.

"""

from itertools import permutations
def latest_clock(a, b, c, d):
    a,b,c,d=str(a),str(b),str(c),str(d)
    l=[]
    for i in list(permutations([a,b,c,d])):
        hh,mm=i[0]+i[1],i[2]+i[3]
        if(hh<"24" and mm <"60"):l.append(hh+mm)
    l.sort(reverse=True)
    return f"{l[0][0:2]}:{l[0][2:]}"


assert(latest_clock(1, 9, 8, 3)== "19:38")
assert(latest_clock(9, 1, 2, 5)== '21:59')
print("Done")