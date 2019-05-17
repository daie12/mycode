#!/usr/bin/env python3
import urllib.request as ulib
import re
print(f"where search?")
url=input()
print(f"great we'll search {url} for the phrase:")
searchFor = input()
searchMe = ulib.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchMe):
    print("Found it!!")
else:
    print("not found and no match!")
