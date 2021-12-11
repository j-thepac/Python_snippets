"""
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.

docker
docker run -it --name encrypt -v $PWD:/home/app -w /home/app -p 5000:5000 python:3.9-slim python encrypt.py

docker build -t encrypt:v1 .

docker-compose.yml
"""
def encrypt_this(text:str):
    l=text.split(" ")
    res=""
    for i in l:
        if(len(i)==1):res=res+str(ord(i))+" "
        elif(len(i)==2):res=res+str(ord(i[0]))+i[-1]+" "
        elif(len(i)==0):res=res+i
        else:res=res+str(ord(i[0]))+i[-1]+i[2:-1]+i[1]+" "
    return res.strip()


tests = [
    ("", ""),
    ("A wise old owl lived in an oak", "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"),
    ("The more he saw the less he spoke", "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"),
    ("The less he spoke the more he heard", "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"),
    ("Why can we not all be like that wise old bird", "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"),
    ("Thank you Piotr for all your help", "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"),
]

for t in tests:
    inp, exp = t
    assert(encrypt_this(inp)== exp)

print("done")