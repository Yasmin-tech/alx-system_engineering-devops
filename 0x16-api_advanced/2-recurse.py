#!/usr/bin/python3
"""A module that retrieves the tiltes of hot subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """a function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit."""

    headers = {"User-Agent": "Middle-Chipmunk-3601"}
    param = {"after": after}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers,
        allow_redirects=False, params=param
    )
    if response.status_code == 200:
        result = response.json()
        list_chlidren = result['data']['children']
        list_titles = [i['data']['title'] for i in list_chlidren]
        # print(list_titles)
        hot_list.extend(list_titles)
        if result['data']['after']:
            return recurse(subreddit, hot_list=hot_list,
                           after=result['data']['after'])
        else:
            return hot_list
    else:
        print(None)
