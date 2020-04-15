from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response = urlopen("https://www.flipkart.com/realme-5i-forest-green-128-gb/p/itmdac0da867a9fa?pid=MOBFP6W53WMJVX7G&lid=LSTMOBFP6W53WMJVX7G3CHKF8&marketplace=FLIPKART&srno=s_1_1&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&fm=SEARCH&iid=22da977e-dace-45d9-bba6-55e189812d99.MOBFP6W53WMJVX7G.SEARCH&ppt=sp&ppn=sp&ssid=9n7wckp1xc0000001586765901982&qH=eb4af0bf07c16429")
html = BS(response, "lxml")
div_tag = html.find("div", "_3WHvuP")
li_list = div_tag.find_all("li")
for li in li_list:
    print(" -> ", li.text)
choice = input("Do you want to see reviews ?")
if choice == "yes":
    div_tag = html.find("div", "col _39LH-M")
    # print(div_tag)
    a_tag = div_tag.find("a")
    link = a_tag["href"]
    print(link)
    link = "https://flipkart.com" + link + "&page=2"
    response = urlopen(link)
    html = BS(response, "lxml")
    reviews_list = html.find_all("div", "qwjRop")
    for i in range(len(reviews_list)):
        print(f"{reviews_list[i].text}")
