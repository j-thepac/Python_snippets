"""
Write a method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings

The method should return an array of sentences declaring the state or country and its capital.

Examples

[{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
[{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
[{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]


"""

def capital(capitals):
    res =list(map(lambda x:cap_dict(x),capitals))
    return (res)


def cap_dict(cap_map):
    state=cap_map.get("country","state")
    if state=="state":state=cap_map[state]
    cap=cap_map.get("capital")
    return "The capital of {} is {}".format(state,cap)

def example_tests():
    state_capitals = [{'state': 'Maine', 'capital': 'Augusta'}]
    assert(capital(state_capitals) == ["The capital of Maine is Augusta"])

    country_capitals = [{'country': 'Spain', 'capital': 'Madrid'}]
    assert(capital(country_capitals)== ["The capital of Spain is Madrid"])

    mixed_capitals = [{"state": 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital": "Madrid"}]
    assert(capital(mixed_capitals)== ["The capital of Maine is Augusta", "The capital of Spain is Madrid"])


if __name__=="__main__":
    example_tests()