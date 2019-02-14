import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        soup = BeautifulSoup(r.read(), 'html.parser')

        for tag in soup.find_all('a'):
            print(tag.get('href'))

news = 'https://news.google.co.jp'
Scraper(news).scrape()
