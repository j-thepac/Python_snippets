"""
Happy Holidays fellow Code Warriors!

It's almost Christmas! That means Santa's making his list, and checking it twice. Unfortunately, elves accidentally mixed the Naughty and Nice list together! Santa needs your help to save Christmas!
Save Christmas!

Santa needs you to write two functions. Both of the functions accept a sequence of objects. The first one returns a sequence containing only the names of the nice people, and the other returns a sequence containing only the names of the naughty people. Return an empty sequence [] if the result from either of the functions contains no names.

The objects in the passed will represent people. Each object contains two properties: name and wasNice.
name - The name of the person
wasNice - True if the person was nice this year, false if they were naughty
Person Object Examples
Test Examples

get_nice_names( [
    { 'name': 'Warrior reading this kata', 'was_nice': True },
    { 'name': 'xDranik', 'was_nice': False },
    { 'name': 'Santa', 'was_nice': True }
] )
# =
"""


def get_nice_names(people):
    return [i["name"] for i in people if(i["was_nice"]==True)]


def get_naughty_names(people):
    return [i["name"] for i in people if(i["was_nice"]==False)]

def example_tests():
    naughty = [{'name': 'xDranik', 'was_nice': False}]
    nice = [{'name': 'Santa', 'was_nice': True}, {'name': 'Warrior reading this kata', 'was_nice': True}]

    assert(get_nice_names(naughty)== [])
    assert(get_nice_names(nice)== ['Santa', 'Warrior reading this kata'])
    assert(get_naughty_names(naughty)== ['xDranik'])
    assert(get_naughty_names(nice)== [])

example_tests()