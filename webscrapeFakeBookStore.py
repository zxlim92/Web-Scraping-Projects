from bs4 import BeautifulSoup
import requests
page = "http://books.toscrape.com/"
textPage = requests.get(page).text
soup = BeautifulSoup(textPage , "lxml")
numberConversion=["Zero", "One", "Two", "Three", "Four", "Five"]
print("NAME", " "*35,"Rating Out of 5","     Price   ")
for scrape in soup.find('ol'):
    x=[]
    y=[]
    try:
        name = scrape.h3.text
        rating = scrape.find("article")
        for p in rating:
            x.append(str(p))
        ratingText = x[3]
        counter = 22
        while ratingText[counter] != "\"":
            y.append(ratingText[counter])
            counter = counter+1
        ratingAlpha = "".join(y)
        ratingNumerical = numberConversion.index(ratingAlpha)
        priceFinder = scrape.find("div",class_="product_price")
        price = (priceFinder.find("p",class_="price_color")).text
        price = price[1:]
        print(name," "*(37-len(name)),"| ",ratingNumerical, " "*len("Rating Out of 5"),"|",price," "*(len(price)-8))
    except AttributeError:
        pass
    