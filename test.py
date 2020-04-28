#!/usr/bin/python

import urllib.request
#
response = urllib.request.Request("http://placekitten.com/400/600")
req = urllib.request.urlopen(response)
# catimg = response.read()
#
# with open('cat_500_600.jpg', 'wb') as f:
#     f.write(catimg)

print(req.info())

print(req.getcode())


