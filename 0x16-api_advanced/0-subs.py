#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

CLIENT_ID = "giJNSgUJI9j600G1max3iA"
SECRET_KEY = "DDF9lor7MbKzT5TgqvRYqjHapJC66w"
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    data = {
        'grant_type': 'password',
        'username': 'Middle-Chipmunk-3601',
        'password': '123456poiuyt'
    }
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1 (by /u/Middle-Chipmunk-3601)"
    }
    response = requests.post('https://www.reddit.com/api/v1/access_token',
                             data=data, headers=headers, auth=auth)
    TOKEN = response.json().get('access_token')
    headers['Authorization'] = f"bearer {TOKEN}"
    # response2 = requests.get('https://oauth.reddit.com/api/v1/me',
    #                          headers=headers)
    # return response2.json()

    url = "https://oauth.reddit.com/r/{}/about.json".format(subreddit)

    response3 = requests.get(url, headers=headers, allow_redirects=False)
    if response3.status_code == 200:
        return response3.json().get("data").get("subscribers")
    return 0
