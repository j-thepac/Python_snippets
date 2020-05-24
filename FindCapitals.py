

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