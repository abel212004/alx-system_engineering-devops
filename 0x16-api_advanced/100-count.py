#!/usr/bin/python3
"""
counts the occurrences of each word in the titles ofthe top posts
in the subreddit. It then prints the words and their respective
counts in descending order.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    prints the occurrences of each word in the titles of
    the top posts in the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {"limit": 100, "after": after}

    response = requests.get(url, params=params,
                            headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code != 200:
        return

    data = response.json()
    articles = data["data"]["children"]

    for article in articles:
        title = article["data"]["title"].lower()
        words = title.split()

        for word in word_list:
            count = words.count(word.lower())
            if count > 0:
                word_count[word] = word_count.get(word, 0) + count

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, word_count)

    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(f"{word}: {count}")
