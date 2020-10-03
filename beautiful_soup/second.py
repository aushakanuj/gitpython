import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

source = requests.get("https://coreyms.com/").text

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(source, "lxml")
articles = soup.find_all("article")

for article in articles[:2]:

    print(article.h2.a["rel"])
