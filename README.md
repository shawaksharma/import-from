# Import From (Anywhere)

 [![PyPI](https://img.shields.io/pypi/v/importfrom.svg)](https://pypi.python.org/pypi/importfrom) [![PyPI](https://img.shields.io/pypi/l/importfrom.svg)](https://pypi.python.org/pypi/importfrom) [![Dependency Status](https://dependencyci.com/github/libeclipse/import-from/badge)](https://dependencyci.com/github/libeclipse/import-from)

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
import importfrom

# Parse and exec functions
functions = importfrom.twitter('https://twitter.com/libeclipse/status/732279611002912769')

# Assign functions to variables
hello = functions['hello']
bye = functions['bye']

# Call and use functions
print('%s\n%s' % (hello('world'), bye('world')))
```

If the service you want isn't already implemented, you can add it yourself!

```
import importfrom

# Code to grab a string containing the function.
string = """
def hello(name):
    return 'Hello, %s!' % name

def bye(name):
    return 'Bye, %s!' % name
"""

functions = importfrom.magic(string)

hello = functions['hello']
bye = functions['bye']

print('%s\n%s' % (hello('world'), bye('world')))
```

If you do add another service, consider contributing by opening a pull request.
