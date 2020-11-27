# importing classes and packages
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import time
import os

BASE_URL = "https://codeforces.com"


def getProblemUrls(contest_code):
    CONTEST_URL = BASE_URL + "/contest/" + contest_code

    html = urllib.request.urlopen(CONTEST_URL).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    problem_urls = set()
    for tag in tags: 
        link = tag.get('href', None)
        if ("contest/" + contest_code + "/problem/") in link:
            problem_urls.add( BASE_URL + link) 
    return problem_urls


def makeSetup():
    contest_code = input("Enter contest code : ").strip()
    for link in getProblemUrls(contest_code):
        print(link)