import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

source = requests.get("https://coreyms.com/").text

soup = BeautifulSoup(source, "lxml")

article = soup.find("article")

print(article.prettify())

