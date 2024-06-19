#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """Recurse it!"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {
        'after': after,
        'limit': 100
    }
    res = requests.get(url, headers={'User-Agent': 'TanjereeN98'},
                       params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None
    results = res.json().get('data')
    after = results.get('after')
    for post in results.get('children'):
        hot_list.append(post.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
