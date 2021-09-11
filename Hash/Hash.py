import hashlib
path="/home/rdx/python/Python_snippets/Hash/sample.txt"
with open(path) as f:
    data=f.read()
print(data)
# print("Encode={}".format(data.encode("ascii")))
hashed=hashlib.sha256(data.encode())
print(hashed.hexdigest())

print(len(hashed.hexdigest()))