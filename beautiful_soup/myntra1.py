from selenium import webdriver
import time

PATH = "/Users/aushakanuz/Downloads/chromedriver"
URL = (
    "https://in.pinterest.com/search/pins/?q=bollywood%20celebrity%20clothing&rs=typed"
)

driver = webdriver.Chrome(PATH)
driver.get(URL)
search = driver.find_elements_by_tag_name("img")
links = []
print(len(search))
for img in search:
    links.append(img.get_attribute("src"))

print(len(links))

print(links)
