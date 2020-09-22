from bs4 import BeautifulSoup
import requests

from scrape_funcs import search_boxes
from scrape_data import coins_dict

def get_names(boxes_array, info_tuple, test=False):
    names = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)
        if searcher:
            names[b] = searcher[0].img.get('alt')
            
        b +=1
    if test == True:
        print(names)
    return names

def get_images(boxes_array, info_tuple, test=False):
    images = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)
        if searcher:
            images[b] = searcher[0].img.get('src')
            
        b +=1
    if test == True:
        print(images)
    return images

def get_price(country, boxes_array, info_tuple, test=False):
    price = [None]*len(boxes_array)

    coin_symbol = coins_dict[country]

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)
        
        if searcher:
            if country == 'mx':
                try:
                    price[b] = float(searcher[0].get_text()[coin_symbol:].replace(',',''))
                except:
                    pass
            elif country == 'br':
                try:
                    price[b] = float(searcher[0].get_text()[coin_symbol:].replace('.','').replace(',','.'))
                except:
                    pass
                
                
        b +=1
    if test == True:
        print(price)
    return price

def get_products_urls(boxes_array, info_tuple, test=False):
    urls = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)
        if searcher:
            source_url = searcher[0].get('href')
            urls[b] = 'https://www.amazon.com.mx' + source_url
            
        b +=1
    if test == True:
        print(urls)
    return urls

def get_stars(country, boxes_array, info_tuple, test=False):
    stars = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)

        if searcher:
            if country == 'mx':
                stars[b] = float(searcher[0].get_text()[:3])
            if country == 'br':
                stars[b] = float(searcher[0].get_text()[:3].replace(',','.'))

        b +=1
    if test == True:
        print(stars)
    return stars

def get_reviews(country, boxes_array, info_tuple, test=False):
    reviews = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)

        if searcher:
            if len(searcher) > 1:
                searcher = [searcher[0]]

            if country == 'mx':
                try:
                    reviews[b] = int(searcher[0].get_text().replace(',',''))
                except:
                    pass
            elif country == 'br':
                try:
                    reviews[b] = int(searcher[0].get_text().replace('.',''))
                except:
                    pass
        
        b +=1
    if test == True:
        print(reviews)
    return reviews

def amazon_products_id(boxes_array, test=False):
    ids = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        if box:
            product_id = box.get('data-asin')
            ids[b] = 'www.amazon.com.mx/dp/' + product_id
            
        b +=1
    if test == True:
        print(ids)
    return ids

