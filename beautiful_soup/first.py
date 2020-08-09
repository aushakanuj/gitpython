from bs4 import BeautifulSoup
import requests

with open("index.html") as html_file:
    soup = BeautifulSoup(html_file, "lxml")

for match in soup.find_all("div", class_="article"):

    print(match.h2.a.text)
    print(match.p.text)
