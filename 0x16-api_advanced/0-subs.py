#!/usr/bin/python3
"""How many subs?"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of the given subreddit"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        res = requests.get(url,
                           headers={'User-Agent': 'TanjereeN98'},
                           allow_redirects=False).json()
    except (Exception):
        return 0
    return res.get('data', {}).get('subscribers', 0)
