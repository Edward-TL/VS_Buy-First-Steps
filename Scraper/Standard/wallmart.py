from bs4 import BeautifulSoup
import re

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#VS_Buy Package
from data import headers, Wallmart
from scrape_funcs import extract_soup, search_boxes


if __name__ == '__main__':
    wallmart_url = 'https://www.walmart.com.mx/productos?Ntt=xbox%20one%20consola'
    # driver = webdriver.PhantomJS(executable_path = "/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
    driver = webdriver.Chrome("chromedriver.exe")
    
    # driver = webdriver.PhantomJS()
    driver.get(wallmart_url)

    selenium_html = driver.page_source
    selenium_soup = BeautifulSoup(selenium_html)
    

    page_boxes = search_boxes(selenium_soup, Wallmart.boxes)
    # From this part, could get better AFTER the 4 scrapers are made
    #From the Boxes, obtain the prices
    price_boxes = get_price(country, page_boxes, Page, test_len=True)
    #Obtain the cheapest from prices and then, you obtain the cheapest product as a dictionary
    cheapest_idx, cheapest_price = cheapest(price_boxes, position_and_price=True)
    cheapest_product_dictionary = get_cheapest(cheapest_idx, page_boxes, cheapest_price, country, Page)


    driver.close()