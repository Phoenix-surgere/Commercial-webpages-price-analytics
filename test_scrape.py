from unittest import TestCase
#from hello import scrape_example_website
from bs4 import  BeautifulSoup
from scraping_static.first_scrapper import multipleMe, scrape_example_website
import numpy as np
from unittest.mock import patch, Mock
import json
from requests import Response
#Note: run with < python -m unittest > NOT <python3 .. >
#conda env export -n scraping  > environment.yml: RUN THIS TO GET .YML file of ALL
#  libraries installed with pip AND conda
#SOURCE: https://stackoverflow.com/questions/18640305/how-do-i-keep-track-of-pip-installed-packages-in-an-anaconda-conda-environment
"""
    conda create --name scraping python=3.9.12 pandas  beautifulsoup4 unittest2 
                 seaborn requests urllib3 tensorflow scikit-learn nose coverage
    conda install beautifulsoup4 urllib3 requests
    conda install pandas seaborn
    conda install nose
    conda install coverage
    conda install -c conda-forge scrapy

"""

mock_data = {}

class TestScrape(TestCase):
    """ Tests Cases for Static Webstie"""

    @classmethod
    def setUpClass(cls):
        """ Load basic responses needed by tests """
        global mock_data
        with open('fixtures/test_website.json') as json_data:
            mock_data = json.load(json_data)

    #Not actually a terribly good test because it depends on external factos
    #This should ideally be converted to use Mocks for consistencty
    def test_example_scrape(self):
        """Tests  if the basic scrape is Ok - good path"""
        url = "https://pythonscraping.com/pages/page1.html"
        self.assertIsInstance(scrape_example_website(url), BeautifulSoup)
        

    @patch('scraping_static.first_scrapper.requests.get')
    def test_example_scrape_mock(self, example_scrape_mock):
        """Uses Mock objects and patching to test the basic scrape w/out actually calling the website """
        example_scrape_mock.return_value = Mock(status_code=404)
        #note: url can be anything, it doesn't matter as I mock
        url = "https://pythonscraping.com/pages/page1.html"
        self.assertEqual(scrape_example_website(url), {})
        #re.findall("^<[a-z]+>"  , str(soup.title))

    @patch('scraping_static.first_scrapper.requests.get')
    def test_goodCall_example_scrape(self, good_mock):
        """Using mock to test a good call """
        good_mock.return_value = Mock(
            spec = Response,
            status_code=200,
            content = b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An Interesting Title</h1>\n<div>\nLorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n' )
       
        url = "whatever.html"
        mock_soup = scrape_example_website(url)
        self.assertIsInstance(mock_soup, BeautifulSoup)
        
        title = mock_soup.find('title').text 
        h1 = mock_soup.find('h1').text

        self.assertEqual(title ,'A Useful Page' )
        self.assertEqual( h1 , 'An Interesting Title')



    def test_multipleMe(self):
        """Tests if multipleMe works - good path (5 tests) """
        for k in range(5):
            f1 = np.random.randn(1).item()
            f2 = np.random.randn(1).item()
            self.assertAlmostEquals(multipleMe(f1,f2), f1*f2)

    def test_multipleMe_f1_bad(self):
        """Test bad argument for f1 """
        self.assertRaises(TypeError, multipleMe,  "andfom", 5)

    def test_multipleMe_f2_bad(self):
        """Test bad argument for f2 """
        self.assertRaises(TypeError, multipleMe,  3, True)








