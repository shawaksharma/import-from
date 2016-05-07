#!/usr/bin/python2

import requests

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup


def get_tweet(tweet_url):
    tweet_page = BeautifulSoup(requests.get(tweet_url).text, "html.parser")
    try:
        tweet_text = tweet_page.body.find('div', attrs={'class':'js-tweet-text-container'}).text
    except AttributeError:
        raise Exception('No tweet found at that URL.')
    return tweet_text.strip()


def pull(tweet_url):
    tweet = get_tweet(tweet_url)
    globals_ = {'__builtins__': None}  # no built-ins for safety
    locals_ = {}
    exec(tweet, globals_, locals_)
    return locals_.popitem()[1]  # return the function
