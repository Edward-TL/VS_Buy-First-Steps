from scrape_data import Mercado_Libre, Products
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from data_filters import get_names, get_images, get_products_urls, get_price

from general_funcs import cheapest, get_cheapest

user_request = 'audifonos inalambricos'
country = 'mx'
ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)

#All the HTML of the page
ml_soup = extract_soup(ml_url, 1, just_soup=True)

#HTML divided by products, and stored as elements of an array
ml_boxes = search_boxes(ml_soup, Mercado_Libre.boxes)
ml_products = {}

ml_products['names'] = get_names(ml_boxes, Mercado_Libre.name_and_images)

#Mercado_Libre's images source (link)
ml_products['images'] = get_images(ml_boxes, Mercado_Libre.name_and_images)

ml_products['urls'] = get_products_urls(ml_boxes, Mercado_Libre.product_urls)

ml_products['prices'] = get_price(country, ml_boxes, Mercado_Libre.price)

cheapest = cheapest(ml_products['prices'])
cheapest_ml_product = get_cheapest(cheapest, ml_products)
for key in cheapest_ml_product:
    print(key, ':', cheapest_ml_product[key])