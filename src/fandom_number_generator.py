#!/usr/bin/env python3

"""Acquire Fandom Numbers. Requires Beautiful Soup 4 for python3, which is
Ubuntu package python3-bs4 ."""

import urllib.request
import time
import re
from bs4 import BeautifulSoup

URLTEMPLATE = "http://archiveofourown.org/works/{0}?view_adult=true"

NUMBERPAT = re.compile(r"[1-9]\d*")

def get_html(workid):
    """Given an AO3 work id number, return the HTML text from the corresponding
    page."""
    url = URLTEMPLATE.format(workid)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    text = data.decode('utf-8')
    return text

def get_number(workid):
    """Given an AO3 work id number, maybe return the first number we find in
    that page. If there's no such number, return None."""

    html = get_html(workid)
    soup = BeautifulSoup(html)

    chapters = soup.find(id='chapters')
    text = chapters.get_text()

    tokens = text.split()
    for token in tokens:
        match = re.match(NUMBERPAT, token)
        if match:
            return int(match.group(0))
    return None

def main():
    workid = 598203

    while True:
        number = get_number(workid)
        if number:
            break
        else:
            print("No numbers in workid", workid)
        workid += 1
        time.sleep(1)

    print(number)
    print("from workid", workid, "at", URLTEMPLATE.format(workid))

if __name__ == "__main__": main()
