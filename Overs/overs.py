def totalOvers(balls):
 if( balls//6 ==balls /6):return balls/6
 else: return (balls // 6+ (balls% 6)/10)

assert(totalOvers(2400)== 400)
assert(totalOvers(164)== 27.2)
assert(totalOvers(945)== 157.3)
assert(totalOvers(5)== 0.5)
assert(totalOvers(7)== 1.1)
assert(totalOvers(15)== 2.3)
assert(totalOvers(0)== 0)
print("done")