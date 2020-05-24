"""
Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

Example:

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"
"""

def greet(name):
    return "Hello {}!".format(name.title())


def example_tests():
    assert(greet('riley')== 'Hello Riley!')
    assert(greet('molly')=="Hello Molly!")
    assert(greet('BILLY')== "Hello Billy!")


if (__name__=="__main__"):
    example_tests()