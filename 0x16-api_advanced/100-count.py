#!/usr/bin/python3
"""A module that retrieves the tiltes of hot subreddit. and count words."""

import requests


def count_words(subreddit, word_list, hot_list=[], after="", flag=False):
    """a recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords"""
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

    if not flag:
        word_list = [[w.lower(), 0] for w in word_list]
        flag = True
    result = response.json()
    list_children = result['data']['children']
    for child in list_children:
        title = child['data']['title']
        for word in title.lower().split():
            for item in word_list:
                if item[0] == word:
                    item[1] += 1
                    print(word, item[0], item[1])

    if result['data']['after']:
        return count_words(subreddit, word_list=word_list,
                           after=result['data']['after'],
                           flag=flag)
    else:
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        unique_list = {}
        for word in word_list:
            if word[1] != 0:
                if word[0] not in unique_list:
                    unique_list[word[0]] = word[1]
                else:
                    unique_list[word[0]] += word[1]
        for k, v in unique_list.items():
            print("{}: {}".format(k, v))
