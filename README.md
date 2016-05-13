# Import From (Anywhere)

This module allows you to import python functions from anywhere!

**It's early days. Help out by submitting a pull request.**

Currently supported hosts:

- Twitter
- Pastebin
- Gist

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

# Gist
hello = importfrom.gist('https://gist.github.com/libeclipse/b240d9b0fff2a65233a30457aad99f12')
print('Gist: ' + hello('world'))
```

If the service you want isn't already implemented, you add it yourself!

```
import importfrom

# Code to get string containing function
...

hello = importfrom.magic(string)
print(hello('world'))
```

If you do add another service, consider contributing by opening a pull request.
