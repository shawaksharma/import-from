#!/usr/bin/env python

from __future__ import print_function, unicode_literals

from bs4 import BeautifulSoup
import requests
import json


def request(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Could not reach that URL. [%d]' % response.status_code)
    return response.text


def magic(code):
    namespace = {}
    code = compile(code, '<string>', 'exec')
    exec(code, namespace)
    return namespace


def pastebin(url):
    if not 'raw' in url:
        url = 'http://pastebin.com/raw/%s' % url.split('/')[-1].strip()
    return magic(request(url))


def twitter(url):
    page = BeautifulSoup(request(url), "html.parser")
    text = page.body.find('div', attrs={'class':'js-tweet-text-container'}).text.strip()
    return magic(text)


def gist(url):
    if not '/raw' in url:
        url = url + '/raw'
    return magic(request(url))


def dns(domain):
    response = json.loads(request('https://dns.google.com/resolve?name=%s&type=TXT' % domain))
    return magic(response['Answer'][0]['data'][1:-1])


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

    # DNS
    hello = dns('importfrom-hello.libeclipse.me')['hello']
    bye = dns('importfrom-bye.libeclipse.me')['bye']
    print('DNS:\n    %s\n    %s\n' % (hello('world'), bye('world')))

    # Self-implementation
    string = """def hello(name):
    return 'Hello, %s!' % name
def bye(name):
    return 'Bye, %s!' % name"""
    functions = magic(string)
    hello = functions['hello']
    bye = functions['bye']
    print('Self Implementation:\n    %s\n    %s\n' % (hello('world'), bye('world')))
