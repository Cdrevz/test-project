import httpx
from selectolax.parser import HTMLParser
from rich import print
import json

"""
not finished sweden hockey getting matches links
"""

def html_get(client: httpx.Client, url):
    resp = client.get(url)
    resp.raise_for_status()
    html = HTMLParser(resp.text)
    return html

def parse_page(html: HTMLParser):
    matches_links = []
    table = html.css("table.tblContent")
    for link in html.css("td.tdOdd.standardPaddingTop a"):
        matches_links.append(link.attributes["href"].strip())
    return matches_links

def main():
    client = httpx.Client()
    client.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
        })
    url = "https://stats.swehockey.se/ScheduleAndResults/Schedule/15977"
    html = html_get(client, url)
    matches_links = parse_page(html)
    print(matches_links)
    print(len(matches_links))
    
    
if __name__ == "__main__":
    main()