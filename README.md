# Import From (Anywhere)

This module allows you to import python modules from anywhere!

**It's early days. Help out by submitting a pull request.**

### Currently supported hosts:

- Twitter

(*Disclaimer: This is not a serious project, just a bit of fun.*)

## Installation:

### Option 1: pip

**Install using pip in order to get the latest stable release.**

`~ >> pip install importfrom`

or

`~ >> python -m pip install importfrom`

### Option 2: git clone

**Install using git to be at the bleeding edge. You'll receive the latest commit.**

```
~ >> git clone https://github.com/libeclipse/import-from.git
~ >> cd import-from
~ >> python setup.py install
```

## Usage:

```
# Import the module
import importfrom

# Twitter
test = importfrom.twitter('https://twitter.com/libeclipse/status/728907625648238594')
print test()
```
