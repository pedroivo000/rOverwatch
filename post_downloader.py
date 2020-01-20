from psaw import PushshiftAPI
import json
from itertools import count
import logging
import sys

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
api = PushshiftAPI()

gen = api.search_submissions(subreddit="Overwatch")
max_response_cache = 10000
cache = []
filename = ("posts_%04i.json" % i for i in count(1))
counter = (i for i in count(1))

for c in gen:
    logging.debug(f"Record num {next(counter)}")
    cache.append(c.d_)

    if len(cache) == max_response_cache:
        name = next(filename)

        logging.info(f"Writing file: {name}")
        with open(name, "w") as f:
            json.dump(cache, f, indent=4)

        logging.info(f"Emptying record cache, size = {sys.getsizeof(cache)}")
        del cache[:]
        # break