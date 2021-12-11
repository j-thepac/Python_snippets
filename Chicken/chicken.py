"""e

Bob is a chicken sexer. His job is to sort baby chicks into a Male(M) and Female(F) piles. When bob can't guess can throw his hands up and declare it with a '?'.

Bob's bosses don't trust Bob's ability just yet, so they have paired him with an expert sexer. All of Bob's decisions will be checked against the experts choices to generate a correctness score.

Scoring Rules
When they agree, he gets 1 point.
When they disagree but one has said '?', he gets 0.5 points.
When they disagree completely, he gets 0 points.

docker:
docker run --name chicken -it -v $PWD:/home/app/ -w /home/app -p 5000:5000 python:3.8-slim python chicken.py

dockerfile:
docker build -t chick:v1 .

"""


def correctness(bobs_decisions, expert_decisions):
    result=0
    for bob,expert in zip(bobs_decisions,expert_decisions):
        if (bob==expert):result+=1
        elif(bob=="?" or expert=="?"):result+=0.5
    return result

assert(correctness(('M', 'F', '?'), ('M', 'F', '?'))== 3)
assert(correctness(('M', '?', 'M'), ('M', 'F', '?'))== 2)
assert(correctness(('F', 'M', 'F'), ('M', 'F', 'M'))== 0)
print("done")