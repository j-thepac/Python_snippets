
"""
calculator("..... + ...............") => "...................."
calculator("..... - ...") => ".."
calculator("..... - .") => "...."
calculator("..... * ...") => "..............."
calculator("..... * ..") => ".........."
calculator("..... // ..") => ".."
calculator("..... // .") => "....."
calculator(". // ..") => ""
calculator(".. - ..") => ""

docker run -it -v $PWD:/home/apps -w /home/apps -p 5000:5000 python:3.9-slim python dotcal.py
docker build -t dotcal:v1 .
docker-compose up
docker-compose down
"""
def calculator(txt): 
    l1,sign,l2=txt.split(" ") 
    v="{}{}{}".format(len(l1),sign,len(l2)) 
    return (eval(v)*".")

def calc(txt):
    l1,sign,l2=txt.split(" ")
    v=str(len(l1))+sign+str(len(l2))
    print(eval(v)*".")
    return (eval(v)*".")


assert(calc("..... + ...............")== "....................")
assert(calc("..... - ...")== "..")
assert(calc("..... - .")== "....")
assert(calc("..... * ...")== "...............")
assert(calc("..... * ..")== "..........")
assert(calc("..... // ..")== "..")
assert(calc("..... // ."), ".....")
assert(calc(". // .."), "")
assert(calc(". - ."), "")
