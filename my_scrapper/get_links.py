from scrape_linkedin import ProfileScraper
import json
from os import environ
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

mylist = []
base_url = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22tn%3A0%22%5D&facetNetwork=%5B%22S%22%2C%22O%22%5D&origin=FACETED_SEARCH&page='
if 'LI_AT' not in environ:
    raise ValueError(
        'Must either define LI_AT environment variable, or pass a cookie string to the Scraper')
cookie = environ['LI_AT']

chromedriver = os.path.dirname(os.path.realpath(__file__)) + "/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get('http://www.linkedin.com')
driver.set_window_size(1200, 1000)
driver.add_cookie({
    'name': 'li_at',
    'value': cookie,
    'domain': '.linkedin.com'
})

for x in range(5,300):
    driver.get(base_url+str(x))
    divs= driver.find_elements_by_class_name("search-result__info")
    len(divs)
    for div in divs:
        mystr = div.find_element_by_css_selector('a').get_attribute('href')
        if("https://www.linkedin.com/in/" in mystr):
            mystr = mystr[28: (len(mystr)-1)]
            print(mystr)
            with open('profile_names.txt', 'a') as fd:
                if (os.stat("profile_names.txt").st_size == 0):
                    fd.write(f'{mystr}')
                else:
                    fd.write(f'\n{mystr}')
driver.quit()
os.system('python my_scrapper.py')





# sign in and perform all your scraping