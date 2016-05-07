#!/usr/bin/python2

from bs4 import BeautifulSoup
import requests


def get_tweet(tweet_url):
    tweet_page = BeautifulSoup(requests.get(tweet_url).text, "html.parser")
    try:
        tweet_text = tweet_page.body.find('div', attrs={'class':'js-tweet-text-container'}).text
    except AttributeError:
        raise Exception('No tweet found at that URL.')
    return tweet_text.strip()


def pull(tweet_url):
    tweet = get_tweet(tweet_url) # Get string containing tweet text
    globals_ = {'__builtins__': None}  # no built-ins for safety
    locals_ = {}
    try:
        exec(tweet, globals_, locals_)
    except:
        raise Exception('Invalid code.')
    if len(locals_) != 1:
        raise Exception('Only a single function per tweet is supported.')
    return locals_.popitem()[1]  # return the function


# Run tests.
if __name__ == "__main__":
    test = pull('https://twitter.com/libeclipse/status/728907625648238594')
    print test()
