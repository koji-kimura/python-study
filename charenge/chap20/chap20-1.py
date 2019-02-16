import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        file = open('./test.txt','w+')
        response = urllib.request.urlopen(self.site)
        html= response.read
        soup = BeautifulSoup(response.read(), 'html.parser')

        for tag in soup.find_all('a'):
            url = tag.get('href')
            url = tag.get('href')
            if url and 'html' in url:
                print("\n" + url)
                file.write(url + "\n")


news = 'https://news.google.co.jp'
Scraper(news).scrape()
