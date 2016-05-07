#!/usr/bin/python2

import importfromtwitter

test = importfromtwitter.pull('https://twitter.com/libeclipse/status/728907625648238594')

print test()
