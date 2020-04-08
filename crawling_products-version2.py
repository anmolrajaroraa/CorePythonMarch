from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

response = urlopen("https://www.flipkart.com/search?q=watches&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_2_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_2_0_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=watches&requestId=403378b9-ed67-466b-b64a-bb79995da765")

html = BS(response, "lxml")

products_list = html.find_all("div", "IIdQZO _1SSAGr")
# print(len(products_list))
for i in range(len(products_list)):
    brand_name = products_list[i].find("div", "_2B_pmu").text
    product_name = products_list[i].find("a", "_2mylT6").text
    current_price = products_list[i].find("div", "_1vC4OE").text
    mrp = products_list[i].find("div", "_3auQ3N")
    mrp = mrp.text if mrp != None else current_price
    discount = products_list[i].find("div", "VGWI6T")

    # if discount != None:
    #     discount = discount.text
    # else:
    #     discount = "Discount not available"

    discount = discount.text if discount != None else "Discount not available"

    # variable_name = condition ? true_action : false_action //ternary operator

    print(f'''
    Product No. {i + 1}
    Product name - {brand_name} {product_name}
    Price - {current_price}
    MRP - {mrp}
    Discount - {discount}
    ''')
