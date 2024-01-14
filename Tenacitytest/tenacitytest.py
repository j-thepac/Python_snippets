
import requests
from  requests.exceptions import HTTPError
from tenacity import retry , retry_if_exception_type ,stop_after_attempt,stop_after_delay


@retry(retry= retry_if_exception_type(HTTPError), stop=(stop_after_attempt(5)| stop_after_delay(1)) )
def fn():
    import time
    time.sleep(2)
    print("test")
    response = requests.get("https://example.com/nonexistent")
    response.raise_for_status()  

fn()
