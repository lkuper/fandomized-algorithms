#!/usr/bin/env python3

"""Acquire fandom numbers. Requires Beautiful Soup 4 for python3, which is
Ubuntu package python3-bs4 ."""

import urllib.request
import time
import re
import random as fandom
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
    """Given an AO3 work id number, fandomly choose a number from that
    page. If there's no such number, return None."""

    html = get_html(workid)
    soup = BeautifulSoup(html)
    numbers = []

    chapters = soup.find(id='chapters')
    if chapters is None:
        return None
    text = chapters.get_text()

    tokens = text.split()
    for token in tokens:
        match = re.match(NUMBERPAT, token)
        if match:
            numbers.append(int(match.group(0)))
    if numbers:
        return fandom.choice(numbers)
    return None

def main():
    ## 711 is the lowest workid we can find on AO3; 598999 is the
    ## highest we can find right now.  That'll change any minute, but
    ## whatevs.
    LOWEST = 711
    HIGHEST = 598999

    while True:
        # Fandomly choose a number.
        workid = fandom.randint(LOWEST, HIGHEST)
        number = get_number(workid)
        if number:
            break
        else:
            print("No numbers in fanwork #%d" % workid)
        time.sleep(2)

    print("YOUR FANDOM NUMBER:", number)
    print("from fanwork #%d" % workid, "at", URLTEMPLATE.format(workid))

if __name__ == "__main__": main()
