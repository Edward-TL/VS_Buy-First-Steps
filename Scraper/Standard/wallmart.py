from bs4 import BeautifulSoup
import re

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#VS_Buy Package
from data import headers, Wallmart
from scrape_funcs import extract_soup, search_boxes
from page_getters import get_names, get_images, get_products_urls, get_price
from cheapest_funcs import cheapest, get_cheapest


if __name__ == '__main__':
    wallmart_url = 'https://www.walmart.com.mx/productos?Ntt=xbox%20one%20consola'
    country = 'mx'
    # driver = webdriver.PhantomJS(executable_path = "/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
    driver = webdriver.Chrome("chromedriver.exe")
    
    # driver = webdriver.PhantomJS()
    driver.get(wallmart_url)

    selenium_html = driver.page_source
    selenium_soup = BeautifulSoup(selenium_html, features='lxml')
    print(selenium_soup.prettify())
    wallmart_boxes = search_boxes(selenium_soup, Wallmart.boxes)
    for box in wallmart_boxes:
        print(box.prettify())

    # From this part, could get better AFTER the 4 scrapers are made
    #From the Boxes, obtain the prices
    wallmart_products={}

    wallmart_products['name'] = get_names(wallmart_boxes, Wallmart, test_all=True)

    '''Wallmart's images source (link)'''
    # wallmart_products['image'] = get_images(wallmart_boxes, Wallmart, test_all=True)

    # wallmart_products['url'] = get_products_urls(wallmart_boxes, Wallmart, test_all=True)

    '''Just Wallmart's products id. Is used as a url generator:
    wallmart's url + domain + "/dp/" + product_id'''
    # wallmart_products['id']= wallmart_products_id(wallmart_boxes)

    # wallmart_products['price'] = get_price(country, wallmart_boxes, Wallmart.price, test_all=True)
    # print(len(wallmart_reviews))
    # for key in wallmart_products:
    #     print(key, ':', wallmart_products[key])

    # cheapest = cheapest(wallmart_products['price'])
    # cheapest_wallmart_product = get_cheapest(cheapest, wallmart_products)
    # for key in cheapest_wallmart_product:
    #     print(key, ':', cheapest_wallmart_product[key])
    # for highlight in wallmart_highlightners:
    #     print(highlight)
    if len(wallmart_boxes) > 0:
        driver.close()