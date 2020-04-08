from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response = urlopen("https://www.flipkart.com/search?count=40&otracker=CLP_filters&p%5B%5D=facets.smart_tv%255B%255D%3DYes&p%5B%5D=facets.resolution%255B%255D%3DUltra%2BHD%2B%25284K%2529&sid=ckf%2Fczl&otracker=nmenu_sub_TVs%20and%20Appliances_0_Smart%20and%20Ultra%20HD&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Smart%20%26%20Ultra%20HD")

html = BS(response, "lxml")
products_list = html.find_all('a', "_31qSD5")
print(len(products_list))

for i in range(len(products_list)):
    product_name = products_list[i].find('div', '_3wU53n')
    features = products_list[i].find('ul', 'vFw0gD')
    print(f'''
    Product no. {i+1}
    Product name - {product_name.text}
    Current Price -
    MRP - 
    Discount - 
    Rating - 
    Features : ''')
    for feature in features:
        print(" -> ", feature.text)
