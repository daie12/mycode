#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():

    r = requests.get('https://cat-fact.herokuapp.com/facts')
    print(r.json()["all"])
#    for catfact in r.json()["all"]:
#       print(catfact.get("text"))

main()

