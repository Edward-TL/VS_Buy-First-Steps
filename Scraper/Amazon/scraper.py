
from data import Amazon
from cheapest_funcs import cheapest, get_cheapest
from scrape_funcs import extract_soup, search_boxes, get_brute_info

from page_getters import get_names, get_images, get_products_urls, get_price
from page_getters import get_stars, get_reviews

def scraper(user_request, country):
    #Adapt the url
    amazon_url = Amazon.adapt_url(Amazon, user_request, country)

    #All the HTML of the page
    amazon_soup = extract_soup(amazon_url, 1, just_soup=True)

    # #HTML divided by products, and stored as elements of an array
    amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

    # From this part, could get better AFTER the 4 scrapers are made
    #From the Boxes, obtain the prices
    amazon_prices = get_price(country, amazon_boxes, Amazon.price)

    #Obtain the cheapest from prices and then, you obtain the cheapest product as a dictionary
    amazon_cheapest_idx, amazon_cheapest_price = cheapest(amazon_prices, position_and_price=True)
    cheapest_amazon_product_dictionary = get_cheapest(amazon_cheapest_idx, amazon_boxes, amazon_cheapest_price, country, Amazon)

    return cheapest_amazon_product_dictionary

if __name__ == "__main__":

    user_request = 'audifonos inalambricos'
    country = 'mx'
    amazon_url = Amazon.adapt_url(Amazon, user_request, country)

    #All the HTML of the page
    amazon_soup = extract_soup(amazon_url, 1, just_soup=True)

    #HTML divided by products, and stored as elements of an array
    amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)
    amazon_products = {}

    amazon_products['name'] = get_names(amazon_boxes, Amazon.name_and_images)

    '''Amazon's images source (link)'''
    amazon_products['image'] = get_images(amazon_boxes, Amazon)

    amazon_products['url'] = get_products_urls(amazon_boxes, Amazon)

    '''Just Amazon's products id. Is used as a url generator:
    amazon's url + domain + "/dp/" + product_id'''
    # amazon_products['id']= amazon_products_id(amazon_boxes)

    '''Just stars as float'''
    amazon_products['star'] = get_stars(country, amazon_boxes, Amazon.stars)

    '''Just number of reviews as int'''
    amazon_products['review'] = get_reviews(country, amazon_boxes, Amazon.reviews)

    amazon_products['price'] = get_price(country, amazon_boxes, Amazon.price)
    # print(len(amazon_reviews))
    # for key in amazon_products:
    #     print(key, ':', amazon_products[key])

    cheapest = cheapest(amazon_products['price'])
    cheapest_amazon_product = get_cheapest(cheapest, amazon_products)
    for key in cheapest_amazon_product:
        print(key, ':', cheapest_amazon_product[key])
    # for highlight in amazon_highlightners:
    #     print(highlight)