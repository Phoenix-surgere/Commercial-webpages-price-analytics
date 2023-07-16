import pandas
import matplotlib.pyplot as plt
import numpy as np
import requests
from bs4 import  BeautifulSoup
from urllib.error import HTTPError


def multipleMe(f1: float, f2:float ) -> float:
    if type(f1) not in [int, float]:
        raise TypeError("f1 must be a number")
    if type(f2) not in [int, float]:
        raise TypeError("f2 must be a number")
    return f1*f2

#https://stackoverflow.com/questions/38727520/how-do-i-add-default-parameters-to-functions-when-using-type-hinting
def scrape_example_website(url: str, parser: str = "html.parser") -> BeautifulSoup:
    '''Scrapes an example, static website; Used for prototyping tests '''
    responce = requests.get(url)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.content, parser)
        return soup
    return {}
    
#url = "https://pythonscraping.com/pages/page1.html"

#soup = scrape_example_website(url)