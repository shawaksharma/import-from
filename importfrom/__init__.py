#!/usr/bin/python2

from __future__ import print_function, unicode_literals

from bs4 import BeautifulSoup
import requests


def twitter(tweet_url):
    tweet_page = BeautifulSoup(requests.get(tweet_url).text, "html.parser")
    try:
        tweet_text = tweet_page.body.find('div', attrs={'class':'js-tweet-text-container'}).text
    except AttributeError:
        raise Exception('No tweet found at that URL.')
    tweet_text = tweet_text.strip()

    globals_ = {'__builtins__': None}  # no built-ins for safety
    locals_ = {}

    try:
        exec(tweet_text, globals_, locals_)
    except:
        raise Exception('Invalid code.')

    if len(locals_) != 1:
        raise Exception('Only a single function per tweet is supported.')

    return locals_.popitem()[1]  # return the function


# Run tests.
if __name__ == "__main__":
    test = twitter('https://twitter.com/libeclipse/status/728907625648238594')
    print('Twitter: ' + test())
