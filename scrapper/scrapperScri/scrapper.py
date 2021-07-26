import requests
from bs4 import BeautifulSoup
import csv


URL = "https://global-asp.github.io/storybooks-uganda/stories/lg/0158/"

#URL = "http://www.values.com/inspirational-quotes"
response = requests.get(URL)

soup = BeautifulSoup(response.content,'html5lib')
soupResult = soup.prettify()
#print(soupResult)

table = soup.find('div', attrs = {'id':'text02'})
#print(table.prettify())
quote = []
cleanedQuote = []
#column col-6 col-lg-11 col-md-12 col-sm-12 level2-txt def
for row in table.find_all_next('div',attrs = {'class' : 'column col-6 col-lg-11 col-md-12 col-sm-12 level3-txt def'}):
    print(row)
    quote.append(row.h3.text.replace('\n', ' ').replace('\t', ''))

print(quote)

filename = "data.csv"

file = open(filename,"a",encoding="utf-8")
for i in quote:
    file.write(i.lstrip())
    file.write('\n')


        