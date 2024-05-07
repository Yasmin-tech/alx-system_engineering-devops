#!/usr/bin/python3
"""A module that retrieves the tiltes of hot subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """A function that queries the Reddit API and returns the titles of
    all hot posts listed for a given subreddit."""
    if not hot_list:
        hot_list = []

    headers = {"User-Agent": "Middle-Chipmunk-3601"}
    param = {"after": after}
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers,
        allow_redirects=False, params=param
    )

    if response.status_code != 200:
        return None

    result = response.json()
    list_children = result['data']['children']
    list_titles = [i['data']['title'] for i in list_children]
    hot_list.extend(list_titles)

    if result['data']['after']:
        return recurse(subreddit, hot_list=hot_list,
                       after=result['data']['after'])
    else:
        return hot_list
