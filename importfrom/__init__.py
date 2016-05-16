#!/usr/bin/python

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
    exec(code, {}, locals_)
    return locals_


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
    functions = twitter('https://twitter.com/libeclipse/status/732279611002912769')
    hello = functions['hello']
    bye = functions['bye']
    print('Twitter:\n    %s\n    %s\n' % (hello('world'), bye('world')))

    # Pastebin
    functions = pastebin('http://pastebin.com/qAjHYyrs')
    hello = functions['hello']
    bye = functions['bye']
    print('Pastebin:\n    %s\n    %s\n' % (hello('world'), bye('world')))

    # Gist
    functions = gist('https://gist.github.com/libeclipse/b240d9b0fff2a65233a30457aad99f12')
    hello = functions['hello']
    bye = functions['bye']
    print('Gist:\n    %s\n    %s\n' % (hello('world'), bye('world')))

    # Self-implementation
    string = """def hello(name):
    return 'Hello, %s!' % name
def bye(name):
    return 'Bye, %s!' % name"""
    functions = magic(string)
    hello = functions['hello']
    bye = functions['bye']
    print('Self Implementation:\n    %s\n    %s\n' % (hello('world'), bye('world')))
