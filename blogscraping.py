from csv import writer
import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com/')

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all(class_='quote')

with open('quotes.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Quotes', 'Author', 'Tags']
    csv_writer.writerow(headers)
    taglist = []
    for quote in quotes:
        quot = quote.find(class_='text').get_text()
        author = quote.find(class_='author').get_text()
        tags = quote.find_all(class_='tag')
        for tag in tags:
            taglist.append(tag.get_text())
        csv_writer.writerow([quot, author, *taglist])
        taglist = []
