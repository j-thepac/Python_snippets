from tenacity import retry,stop_after_attempt


def fn():
    print("Stopping after 3 attempts")
    raise Exception

xcvcxvcxv



fn()