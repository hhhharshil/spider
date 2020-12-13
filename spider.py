#!/usr/bin/python3

import requests
import re
import urllib.parse as urlparse

target_url = input("Please enter the target URL: ")
extracted_links = []
def extraction(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
    href_links = extraction(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in extracted_links:
            extracted_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)

