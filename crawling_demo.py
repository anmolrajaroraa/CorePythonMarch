# import urllib.request as req
from urllib.request import urlopen
# import bs4
from bs4 import BeautifulSoup as BS

# 1. Make a http request to amazon.in
# 2. When response comes in, we have to get the html page source code
url = "https://www.imdb.com/"

response = urlopen(url)
print(response)
htmlPage = BS(response, "lxml")
print(type(htmlPage))
h3_tag = htmlPage.find("h3", "ipc-title__text")
print(h3_tag.text)
