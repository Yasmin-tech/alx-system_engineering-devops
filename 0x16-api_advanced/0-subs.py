#!/usr/bin/python3
"""A module that retrieves the number of subscribers of a subreddit."""


import requests
# import pprint


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (total subscribers)
        for a given subreddit. If an invalid subreddit is given,
        the function will return 0"""

    headers = {"User-Agent": "My User Agent 1.0"}
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0


# pprint.pprint(get_subreddit_subscribers("programming"))
