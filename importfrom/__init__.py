#!/usr/bin/python2

from __future__ import print_function, unicode_literals

from bs4 import BeautifulSoup
import requests


# Fix the supplied url so requests doesn't complain.
def fix_url(url):
    if ((not url.startswith("http://")) and (not url.startswith("https://"))):
        url = "http://" + url
    if (url.endswith("/")):
        url = url[:-1]
    return url


def request(url):
    return requests.get(fix_url(url)).text


def magic(code):
    locals_ = {}
    exec(code, {'__builtins__': None}, locals_)
    if len(locals_) != 1:
        raise Exception('Only a single function per tweet is supported.')
    return locals_.popitem()[1]  # return the function


def pastebin(url):
    if not 'raw' in url:
        url = 'http://pastebin.com/raw/%s' % url.split('/')[-1].strip()
    return magic(request(url))


def twitter(url):
    page = BeautifulSoup(request(url), "html.parser")
    try:
        text = page.body.find('div', attrs={'class':'js-tweet-text-container'}).text.strip()
    except AttributeError:
        raise Exception('No tweet found at that URL.')
    return magic(text)


def gist(url):
    if not '/raw' in url:
        url = url + '/raw'
    return magic(request(url))


# Run tests.
if __name__ == "__main__":
    # Twitter
    hello = twitter('https://twitter.com/libeclipse/status/729058974302089216')
    print('Twitter: ' + hello('world'))

    # Pastebin
    hello = pastebin('http://pastebin.com/hgw7mphJ')
    print('Pastebin: ' + hello('world'))

    # Gist
    hello = gist('https://gist.github.com/libeclipse/b240d9b0fff2a65233a30457aad99f12')
    print('Gist: ' + hello('world'))

    # Self-implementation
    string = """def hello(name):
        return 'Hello, %s!' % name"""
    hello = magic(string)
    print('Self-implementation: ' + hello('world'))
