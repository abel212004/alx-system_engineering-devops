#!/usr/bin/python3
"""
retrieves the titles of hot posts from a given
subreddit using the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list of titles of hot posts from a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {"limit": 100, "after": after}

    response = requests.get(url, params=params,
                            headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code != 200:
        return None

    data = response.json()
    articles = data["data"]["children"]

    for article in articles:
        hot_list.append(article["data"]["title"])

    after = data["data"]["after"]
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
