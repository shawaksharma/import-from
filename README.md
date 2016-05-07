# Import from Twitter

Host and import your python functions from Twitter!

(*Disclaimer: This is not a serious project, just a bit of fun.*)

## Installation:

### Option 1: pip

**Install using pip in order to get the latest stable release.**

`~ >> pip install importfromtwitter`

or

`~ >> python -m pip install importfromtwitter`

### Option 2: git clone

**Install using git to be at the bleeding edge. You'll receive the latest commit.**

```
~ >> git clone https://github.com/libeclipse/import-from-twitter.git
~ >> cd import-from-twitter
~ >> python setup.py install
```

## Usage:

```
# Import the module
import importfromtwitter

# Initialize `test` with the function.
test = importfromtwitter.pull('https://twitter.com/libeclipse/status/728907625648238594')

# Call the function.
print test()
```
