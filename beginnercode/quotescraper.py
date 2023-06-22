from bs4 import BeautifulSoup
import requests
import csv

url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

#finding quotes here
divs = soup.find_all("div", class_= "quote")

#saving quotes here
quotes_by_author = []

#finding quotes and saving them to previous dictionary
for div in divs:
    quote_block = div.find("span", class_= "text")
    if quote_block is not None:
        quote = quote_block.text.strip()
    else:
        quote = ''

    author_block = div.find("small", class_= "author")
    if author_block is not None:
        author = author_block.text.strip()
    else:
        author = ''

    quotes_by_author.append({
        "quote": quote,
        "author": author,
    })

#ordering purposes
fields = ['quote', 'author']

#new csv file generation
outputfile_name = "quotes.csv"

#opening the previous file and writing the dictionary to it in a certian encoding
with open (outputfile_name, 'w', newline='', encoding="cp1252") as f_output:
    writer = csv.DictWriter(f_output, fieldnames = fields)
    writer.writeheader()
    writer.writerows(quotes_by_author)


