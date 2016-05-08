#!/usr/bin/python2

from __future__ import print_function, unicode_literals

from bs4 import BeautifulSoup
import requests


def pastebin(url):
    if not 'raw' in url:
        url = 'https://pastebin.com/raw/%s' % url.split('/')[-1].strip()
    page = requests.get(url).text

    globals_ = {'__builtins__': None}  # no built-ins for safety
    locals_ = {}

    try:
        exec(page, globals_, locals_)
    except:
        raise Exception('Invalid code.')

    if len(locals_) != 1:
        raise Exception('Only a single function per tweet is supported.')

    return locals_.popitem()[1]  # return the function


def twitter(url):
    page = BeautifulSoup(requests.get(url).text, "html.parser")
    try:
        text = page.body.find('div', attrs={'class':'js-tweet-text-container'}).text.strip()
    except AttributeError:
        raise Exception('No tweet found at that URL.')

    globals_ = {'__builtins__': None}  # no built-ins for safety
    locals_ = {}

    try:
        exec(text, globals_, locals_)
    except:
        raise Exception('Invalid code.')

    if len(locals_) != 1:
        raise Exception('Only a single function per tweet is supported.')

    return locals_.popitem()[1]  # return the function


# Run tests.
if __name__ == "__main__":
    # Twitter
    hello = twitter('https://twitter.com/libeclipse/status/729058974302089216')
    print('Twitter: ' + hello('world'))

    # Pastebin
    hello = pastebin('http://pastebin.com/hgw7mphJ')
    print('Pastebin: ' + hello('world'))
