from pprint import pprint

import requests


# Structure payload.
payload = {
    "source": "amazon_reviews",
    "domain": "nl",
    "query": "B08238V32L",
    "parse": True,
}


# Get response.
response = requests.request(
    "POST",
    "https://realtime.oxylabs.io/v1/queries",
    auth=("user", "pass1"),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
