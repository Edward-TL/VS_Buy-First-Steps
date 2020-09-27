from bs4 import BeautifulSoup
import re

#All Selenium stuff 
#https://openwebinars.net/blog/como-hacer-web-scraping-con-selenium/
import zipfile
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium import WebElement

#VS_Buy Package
from data import headers
from scrape_funcs import extract_soup


if __name__ == '__main__':
    wallmart_url = 'https://www.walmart.com.mx/productos?Ntt=xbox%20one%20consola'
    # driver = webdriver.PhantomJS(executable_path = "/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs")
    driver = webdriver.Chrome("chromedriver.exe")
    
    # driver = webdriver.PhantomJS()
    driver.get(wallmart_url)

    selenium_html = driver.page_source
    selenium_soup = BeautifulSoup(selenium_html)
    print(selenium_soup.prettify())

    driver.close()