#For the system
import os

#Manage of time
from datetime import datetime, timedelta
from pytz import timezone
import time
import re

#Manage Files
import csv

#scrap
from bs4 import BeautifulSoup
import requests


#Personal
from scrape_tools import header
from general_tools import ordered_dict





if __name__ == "__main__":
    stars = {'Mercado Libre': 4.1,
            'Amazon': 4.3,
            'Wallmart': 4.5,
            'ebay': 3.9}

    reviews = {'Mercado Libre': 200,
            'Amazon': 300,
            'Wallmart': 500,
            'ebay': 150}

    price = {'Mercado Libre': 2000,
            'Amazon': 4000,
            'Wallmart': 3900,
            'ebay': 1500}

    data = {'stars':stars,
            'reviews':reviews,
            'price':price}

    print(ordered_dict(stars))
    print(header.wallmart)

