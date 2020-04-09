from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

search = input("Enter search term : ")
search = search.replace("&", "%26").replace(" ", "%20")
# print(search)
url = f"https://www.imdb.com/find?q={search}&ref_=nv_sr_sm"
print(url)
response = urlopen(url)

html = BS(response, "lxml")
# title_name = html.find("td", "result_text")
# print(title_name.text)
table = html.find("table", "findList")
# print(table)
table_rows = table.find_all("tr")
for i in range(len(table_rows)):
    print(f"{i+1}. {table_rows[i].text}")

while True:
    choice = int(input("Which one : "))
    if choice < 1 and choice > len(table_rows):
        print("Invalid choice")
        continue
    selected_row = table_rows[choice - 1]
    # print(selected_row)
    link = selected_row.find("a")["href"]
    # print("Path to next page - ", link)
    url = "https://imdb.com" + link
    response = urlopen(url)
    html = BS(response, "lxml")
    print(html.find("h1").text)
    summary = html.find("div", "summary_text")
    summary = summary.text.strip() if summary != None else html.find(
        "div", "inline").text.strip()
    print(summary)
