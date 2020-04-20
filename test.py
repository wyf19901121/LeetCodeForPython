#!/usr/bin/python

import urllib.request

baidu = urllib.request.urlopen("http://www.baidu.com")
print(baidu.read())



