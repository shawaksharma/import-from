# Import From (Anywhere)

This module allows you to import python modules from anywhere!

**It's early days. Help out by submitting a pull request.**

Currently supported hosts:

- Twitter

*(Disclaimer: This is not a serious project, just a bit of fun.)*

## Installation:

`~ >> pip install importfrom`

or

`~ >> python -m pip install importfrom`

## Usage:

```
# Import the module
import importfrom

# Twitter
hello = twitter('https://twitter.com/libeclipse/status/729058974302089216')
print(hello('Eclipse'))

# Pastebin
hello = pastebin('http://pastebin.com/hgw7mphJ')
print('Pastebin: ' + hello('Eclipse'))
```
