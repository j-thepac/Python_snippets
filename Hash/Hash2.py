import base64
import hashlib
hashed = hashlib.sha256("hi".encode())
encod=base64.b64encode("hi".encode()) 
decod=base64.b64decode(encod) 
print(encod,decod)
