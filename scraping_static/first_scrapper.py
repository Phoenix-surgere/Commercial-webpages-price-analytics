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
    '''Scrapes an example, static website; Used for prototyping tests. Shoul
    also add a check to ensure it timeouts within a reasonable time because
    apparanetly, as seen by plaisio attempted scrape, it may take foreever
    example url: url = "https://pythonscraping.com/pages/page1.html"
    '''
    responce = requests.get(url)
    if responce.status_code == 200:
        soup = BeautifulSoup(responce.content, parser)
        return soup
    return {}



"""
EXAMPLE WEBSITES TO SCRAPE:

#ELECTROINICS
https://www.mediamarkt.gr/shop/article/media-markt-flyer   #WORKS
https://www.kotsovolos.gr/  #FORBIDDEN LINK
https://www.plaisio.gr/  #ALSO USELESS, takes foever to get it going
https://www.sunelectronics.gr/  #works

#OPTIONAL, international office, could be fun
https://www.distrelec.biz/en/   #works


#SUPERMARKETS
#GERMAN LIDL and kaufland, aldi (which is english!!)
https://www.lidl.de/h/mode/h10005518?mktc=brandpaidsearch_shop&gclid=Cj0KCQjw_O2lBhCFARIsAB0E8B-JyhCuZ1rrG_RyAvii1l8ZgscuKZARkUTKxdntAT9jSlSYHe5wUGkaAn3VEALw_wcB&et_uk=41b6a1bd1f7e459f866afc6b717e83b1
https://www.kaufland.de/?gclid=Cj0KCQjw_O2lBhCFARIsAB0E8B9V-jsnwgixG-7H7ykOR3C18sqQA33byIwwqtDDtgrBOIcph_qwL1saAvv9EALw_wcB
https://www.aldi.us/?utm_source=google&utm_medium=sem&utm_campaign=brand&utm_term=aldi&gclid=Cj0KCQjw_O2lBhCFARIsAB0E8B_uSYL6fhAEATf4oDsgJMMeVHdzRxrVbhw_N_gL9xFFl7oXNwAzm-0aAmA6EALw_wcB&gclsrc=aw.ds

https://eshop.masoutis.gr/

"""















#url = "https://pythonscraping.com/pages/page1.html"

#soup = scrape_example_website(url)

#TODO: Add a function that automatically calls the websites that 
#we wish to scrape, retrieves responces and stores them to a .csv
#file or whatever to be used as test fixtures 

#First, code to get shit (requests raw is enough)
#Then, code to get shit into a dict
#then dict => pd.Df => csv

#Ultra line: gets a dict of a response, appends it to existing ccv
#pd.Series(responses_dict_NEW).to_frame(name="responces").to_csv("responces_fixed.csv", mode='a', header=False)

#line to read those motherfuckers
#df_loaded = pd.read_csv('responces_fixed.csv')

#NECESSARy line to convert those strings to bs4 objects:
#mock_data = pd.read_csv(r'fixtures\responces_fixed.csv', names=['type', 'responces'], 
#                                header=0)
#mock_responce = mock_data.responces.iloc[0]  #mock_data == df_loaded#
#BeautifulSoup(bytes(mock_responce[2:len(mock_responce)-1], encoding='utf-8'), "html.parser")
