#This imports requests, that is used to get webpages
import requests#This is used to get webpages

#This goes to the webpage and gets it
page = requests.get("https://www.bbc.com/news")

#pRINTS THE HTML STATUS CODE , 200= GOOD 404== not found 500= error
print()
#Then we print the CONTENT of the page, that is , the HTML
print(page.content)

#Import requests
import requests

#Just import Beautiful soup from the bs4 library
from bs4 import BeautifulSoup

page =  requests.get("https://www.bbc.com/news")

#we make some soup:)
soup = BeautifulSoup(page.content,"html.parser")

#we can do many nice things with out our soup!!!
#print all the paragraphs one by one in the HTML
for item in soup.find_all("p"):
    print(item)

import requests
from bs4 import BeautifulSoup

def getNewsHeadline():
    page = requests.get("https://www.bbc.com/news")
    sou =  BeautifulSoup(page.content,"html.parser")
    for p in soup.find_all("p"):
        break#Get the first p and stop
    return p.text#get only the text and not the <> tags too

print("Hello Leo,here is the news today:")
print(getNewsHeadline())

import requests
from bs4 import BeautifulSoup

def getPrices(name):
    page = requests.get("https://www.books.ie/catalogsearch/result/?q="+name)
    soup =  BeautifulSoup(page.content,"html.parser")
    prices = []
    for s in soup.find_all("span",class_="price"):
        prices.append(float(s.text.replace("€","")))
        prices.sort()
    return(prices[0])

book = input("what is the name of your book?")
print("The cheapest price is :")
print(getPrices(book))