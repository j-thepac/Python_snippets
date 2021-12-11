"""
ASC Week 1 Challenge 4 (Medium #1)

Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.

Examples
"Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
"Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"

docker:
docker run -it --name vapour -v $PWD:/home/app -w /home/app/ python:3.8-slim python VapourCode.py


docker build -t vapour:v1 .

docker-compose up
"""

def vaporcode(s:str):
    return "  ".join(s.replace(" ","").upper())
    

assert(vaporcode("Lets go to the movies")=="L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S")
assert(vaporcode("Why isn't my code working?")=="W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?")
print("done")