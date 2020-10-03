from bs4 import BeautifulSoup
import requests

# with open("index.html") as html_file:
#     soup = BeautifulSoup(html_file, "lxml")


source = requests.get("https://www.flightradar24.com/data/airports/bom")

print(source.text)
# soup = BeautifulSoup(source, "lxml")
# print("gggg")

# for match in soup.find_all("div", class_="row cnt-schedule-table"):
#     print("jello")
#     print(match.text)
