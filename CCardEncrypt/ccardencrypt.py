def maskify(cc):
    if(len(cc)>4):return "#"*(len(cc[-4::-1])-1)+cc[-4::]
    else:return cc

assert(maskify('')== '')
assert(maskify('123')== '123')
assert(maskify('SF$SDfgsd2eA')== '########d2eA')
print("Done")