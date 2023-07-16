import pandas
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import  BeautifulSoup
#from urllib.request import urlopen
from urllib.error import HTTPError

#-------------------
# this is definitely not the optimal way to ogranize, I need to figure out how to make python package
#import sys
#sys.path.insert(1, r'C:\Users\black\OneDrive\Documents\GitHub\Commercial-webpages-price-analytics\code')
#from some import add
#-------------------

#Creating a package, even a rudimentary one via __init__ IS THE WAY
from scraping_static.first_scrapper import multipleMe



#url = "https://www.kdnuggets.com/2022/07/12-essential-vscode-extensions-data-science.html"
#url  = 'http://www.pythonscraping.com/pages/page1.html'
#html = "https://pythonscraping.com/pages/page1.html"
#responce = requests.get(html)
#print(responce)


#soup = BeautifulSoup(responce.content, "html.parser")
#print(soup.h1)

def scrape_example_website(url: str ) -> BeautifulSoup:
    try: 
        responce = requests.get(url)
    except HTTPError as e:
        #print(e)
        return e
    else:
        soup = BeautifulSoup(responce.content, "html.parser")
        #print(soup.h1)
        return soup

#scrape_example_website("https://pythonscraping.com/pages/page1.html")

#add(5,7)