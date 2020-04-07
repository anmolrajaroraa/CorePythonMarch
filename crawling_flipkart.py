from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response = urlopen("https://www.flipkart.com/search?count=40&otracker=CLP_filters&p%5B%5D=facets.smart_tv%255B%255D%3DYes&p%5B%5D=facets.resolution%255B%255D%3DUltra%2BHD%2B%25284K%2529&sid=ckf%2Fczl&otracker=nmenu_sub_TVs%20and%20Appliances_0_Smart%20and%20Ultra%20HD&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Smart%20%26%20Ultra%20HD")

html = BS(response, "lxml")

print("Product name is", html.find('div', "_3wU53n").text)

ul_tag = html.find('ul', 'vFw0gD')
# print(ul_tag)
# li_tag = ul_tag.find('li')
# print(li_tag)
li_list = ul_tag.find_all('li')
# print(li_list)
for li in li_list:
    print(li.text)
