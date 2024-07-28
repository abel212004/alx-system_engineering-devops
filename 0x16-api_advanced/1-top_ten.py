#!/usr/bin/python3
"""
Retrieves the top 10 hot posts from a given subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    retrieves the top 10 posts from a subreddit
    @param subreddit - the name of the subreddit
    @return None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/binyammamo)"
    }

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        result = resp.json()
        result = result["data"]["children"]
        i = 0
        while i < 10 and i < len(result):
            print(result[i]["data"]["title"])
            i = i + 1
    else:
        print("None")
