"""
This function should take two string parameters: a person's name (name) and a quote of theirs (quote), and return a string attributing the quote to the person in the following format:

'[name] said: "[quote]"'
For example, if name is 'Grae' and 'quote' is 'Practice makes perfect' then your function should return the string

'Grae said: "Practice makes perfect"'
Unfortunately, something is wrong with the instructions in the function body. Your job is to fix it so the function returns correctly formatted quotes.

docker:
#docker run -it --name quotable -v $PWD:/home/app/ -w /home/app/ python:3.8-slim python Quotable.py
docker build -t quotable:v1 .
docker-compose up
"""

def quotable(name, quote):
    return ('{} said: "{}"'.format(name,quote))


assert(quotable('Grae', 'Practice makes perfect')== 'Grae said: "Practice makes perfect"')
assert(quotable('Dan', 'Get back to work, Grae')== 'Dan said: "Get back to work, Grae"')
assert(quotable('Alex', 'Python is great fun')== 'Alex said: "Python is great fun"')
assert(quotable('Bethany', 'Yes, way more fun than R')== 'Bethany said: "Yes, way more fun than R"')
assert(quotable('Darrell', 'What the heck is this thing?')== 'Darrell said: "What the heck is this thing?"')
print("done")
