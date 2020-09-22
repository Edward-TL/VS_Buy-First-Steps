
from General.scrape_data import Amazon, Products
from General.general_funcs import cheapest, get_cheapest
from General.scrape_funcs import extract_soup, search_boxes, get_brute_info

# import sys
# sys.path.insert(1, '"web scraper"/Amazon')

from Amazon.data_filters import get_names, get_images, get_products_urls, get_price
from Amazon.data_filters import get_stars, get_reviews, amazon_products_id

from bs4 import BeautifulSoup

user_request = 'audifonos inalambricos'
country = 'mx'
amazon_url = Amazon.adapt_url(Amazon, country, user_request)

#All the HTML of the page
amazon_soup = extract_soup(amazon_url, 1, just_soup=True)

#HTML divided by products, and stored as elements of an array
amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)
amazon_products = {}

amazon_products['name'] = get_names(amazon_boxes, Amazon.name_and_images)

'''Amazon's images source (link)'''
amazon_products['image'] = get_images(amazon_boxes, Amazon.name_and_images)

amazon_products['url'] = get_products_urls(amazon_boxes, Amazon.product_urls)

'''Just Amazon's products id. Is used as a url generator:
amazon's url + domain + "/dp/" + product_id'''
amazon_products['id']= amazon_products_id(amazon_boxes)

'''Just stars as float'''
amazon_products['star'] = get_stars(country, amazon_boxes, Amazon.stars)

'''Just number of reviews as int'''
amazon_products['review'] = get_reviews(country, amazon_boxes, Amazon.reviews)

amazon_products['price'] = get_price(country, amazon_boxes, Amazon.price)
# print(len(amazon_reviews))

cheapest = cheapest(amazon_products['price'])
cheapest_amazon_product = get_cheapest(cheapest, amazon_products)
for key in cheapest_amazon_product:
    print(key, ':', cheapest_amazon_product[key])
# for highlight in amazon_highlightners:
#     print(highlight)