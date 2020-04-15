from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
search = input("Enter Search term: ")
search = search.replace("&", "%26").replace(" ", "%20")
response = urlopen(
    f"https://www.flipkart.com/search?q={search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
html = BS(response)
productList = html.find_all('div', "_1UoZlX")
for i in range(len(productList)):
    productName = productList[i].find('div', "_3wU53n")
    productPrice = productList[i].find('div', "_1vC4OE _2rQ-NK")
    productRating = productList[i].find('div', "hGSR34")
    print(f'''
  Product Number->{i+1}
  Name->{productName.text}
  Price->{productPrice.text}
  Ratings->{productRating.text}''')
while True:
    choice = int(input("Which Product: "))
    if choice < 1 and choice > len(productList):
        print("Invalid choice")
        continue
    else:
        selectedProduct = productList[choice-1]
        link = selectedProduct.find("a")["href"]
        response = urlopen("https://flipkart.com"+link)
        html = BS(response)
        selectName = html.find("h1", "_9E25nV")
        selectMRP = selectName.find('div', "_3auQ3N _1POkHg")
        selectMRP = selectMRP.text if selectMRP != None else "Not Available"
        selectDiscount = selectedProduct.find('div', "VGWI6T _1iCvwn")
        selectDiscount = selectDiscount.text if selectDiscount != None else "Not available"
        selectPrice = selectedProduct.find('div', "_1vC4OE _3qQ9m1")
        selectPrice = selectPrice.text if selectPrice != None else "Not Available"
        selectRating = selectName.find('div', "hGSR34")
        selectRating = selectRating if selectRating != None else "Not available"
        featureList = html.find('ul', "_2-riNZ")
        selectReviews = selectName.find('div', "row")
        print(f'''
    Name-> {selectName.text}
    MRP-> {selectMRP}
    Discount-> {selectDiscount}
    Final Price-> {selectPrice}
    Features->''')
        for li in range(len(featureList)):
            print(li.text)
        moreReviews = input("Do you want to see more reviews(yes/no): ")
        if moreReviews == "no":
            break
        else:
            reviewTag = html.find("div", "_2aFisS")
            reviewLink = html.find("a")["href"]
            response = urlopen("https://flipkart.com", reviewLink)
            html = BS(response)
            reviewRating = html.find("div", "row")
            print("More Review->")
            for i in range(len(reviewRating)):
                print(i.text)
