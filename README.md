# Import From (Anywhere)

This module allows you to import python functions from anywhere!

**It's early days. Help out by submitting a pull request.**

Currently supported hosts:

- Twitter
- Pastebin

*(Disclaimer: This is not a serious project, just a bit of fun.)*

## Installation:

`~ >> pip install importfrom`

or

`~ >> python -m pip install importfrom`

## Usage:

First of all, you have to upload the code. Each snippet must contain exactly one function.

For example:

```
def hello(name):
    return 'Hello, %s!' % name
```

Then, you can import and use it as normal:

```
# Import the module
import importfrom

# Twitter
hello = importfrom.twitter('https://twitter.com/libeclipse/status/729058974302089216')
print('Twitter: ' + hello('world'))

# Pastebin
hello = importfrom.pastebin('http://pastebin.com/hgw7mphJ')
print('Pastebin: ' + hello('world'))
```
