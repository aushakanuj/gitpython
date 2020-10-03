from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlopen
import re

url = (
    "https://in.pinterest.com/search/pins/?q=bollywood%20celebrity%20clothing&rs=typed"
)
resp = requests.get(url).text
matches = re.findall(r'src="(https:\/\/i.pinimg\.com\/236x.+.jpg)"', resp)
print(re)
print(len(matches))
