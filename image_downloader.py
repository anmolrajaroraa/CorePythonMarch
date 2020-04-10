# from urllib.request import urlretrieve

# urlretrieve("https://rukminim1.flixcart.com/image/390/468/jeka07k0/watch/4/p/y/38024pp25-fastrack-original-imaf37n5df3bn52n.jpeg?q=50", "watch.jpeg")

from urllib.request import *
from bs4 import BeautifulSoup as BS

response = urlopen("https://imdb.com")
html = BS(response, "lxml")
images_list = html.find_all("img")
# print(len(images_list))
# for image in images_list:
#     print(image)

for i in range(len(images_list)):
    image = images_list[i]
    url = image["src"]
    filename = f"downloads/{i+1}.jpg"
    urlretrieve(url, filename)
