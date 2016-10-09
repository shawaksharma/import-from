# Import From (Anywhere)

 [![PyPI](https://img.shields.io/pypi/v/importfrom.svg)](https://pypi.python.org/pypi/importfrom) [![PyPI](https://img.shields.io/pypi/l/importfrom.svg)](https://pypi.python.org/pypi/importfrom)

This module allows you to import python functions from anywhere!

**It's early days. Help out by submitting a pull request.**

Currently supported hosts:

- Twitter
- Pastebin
- Gist
- DNS TXT Records

*(Disclaimer: This is not a serious project, just a bit of fun.)*

## Installation:

`~ >> pip install importfrom`

or

`~ >> python -m pip install importfrom`

## Usage:

First of all, you have to upload the code.

For example:

```
def hello(name):
    return 'Hello, %s!' % name

def bye(name):
    return 'Bye, %s!' % name
```

Then, you can import and use it as normal:

```
# Import the module
from importfrom import twitter

# Parse and exec functions
functions = twitter('https://twitter.com/libeclipse/status/732279611002912769')

# Assign functions to variables
hello = functions['hello']
bye = functions['bye']

# Call and use functions as normal
print('%s\n%s' % (hello('world'), bye('world')))
```

The DNS function has to be handled slightly differently. Create a TXT record for a distinct subdomain on your domain, and place your code in that. If there are multiple TXT records then there's no guarantee as to which one will be chosen.

Here's an example:

```
hello = dns('importfrom-hello.libeclipse.me')['hello']
bye = dns('importfrom-bye.libeclipse.me')['bye']
```

If the service you want isn't already implemented, you can add it yourself!

```
from importfrom import magic

# Code to grab a string containing the functio(n|ns).
string = """
def hello(name):
    return 'Hello, %s!' % name

def bye(name):
    return 'Bye, %s!' % name
"""

functions = magic(string)

hello = functions['hello']
bye = functions['bye']

print('%s\n%s' % (hello('world'), bye('world')))
```

If you do add another service, consider contributing by opening a pull request.
