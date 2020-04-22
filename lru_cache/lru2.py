"""Reading about LRU

I discovered you can create an LRU cache using python's own functools. This is the implementation of that.

"""
# Create an expensive function
import time
import urllib
import urllib.request
from functools import lru_cache


@lru_cache(maxsize=4)
def get_url(resource):
    try:
        with urllib.request.urlopen(resource) as s:
            return True
    except Exception as e:
        return False


start = time.time()
get_url("https://cloud.google.com/")

get_url("https://aws.amazon.com/es/")  # url 2
print(get_url.cache_info())
get_url("https://azure.microsoft.com/es-es/")  # url 3
get_url("https://www.digitalocean.com/")  # url 4
print(get_url.cache_info())
get_url("https://cloud.google.com/")  # url 1
print(get_url.cache_info())
get_url("https://www.ovh.com/")  # url 5
print(get_url.cache_info())

print(f"Duration: {time.time() - start}s")
# Output example: Duration: 0.1427597999572754s
