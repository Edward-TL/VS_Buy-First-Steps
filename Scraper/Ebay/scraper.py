from data import Ebay
from cheapest_funcs import cheapest, get_cheapest
from scrape_funcs import extract_soup, search_boxes, get_brute_info

from page_getters import get_names, get_images, get_products_urls, get_price

def scraper(Page, user_request, country):
    #Adapt the url
    url = Page.adapt_url(Page, country, user_request)

    #All the HTML of the page
    soup = extract_soup(url, 1, just_soup=True)

    # #HTML divided by products, and stored as elements of an array
    boxes = search_boxes(soup, Page.boxes)

    # From this part, could get better AFTER the 4 scrapers are made
    #From the Boxes, obtain the prices
    prices= get_price(country, boxes, Page.price)

    #Obtain the cheapest from prices and then, you obtain the cheapest product as a dictionary
    cheapest_idx, cheapest_price = cheapest(prices, position_and_price=True)
    cheapest_product_dictionary = get_cheapest(cheapest_idx, boxes, cheapest_price, country, Page)

    return cheapest_product_dictionary

if __name__ == "__main__":
    user_request = 'audifonos inalambricos'
    country = 'mx'
    ebay_url = Ebay.adapt_url(Ebay, user_request, country)

    #All the HTML of the page
    ebay_soup = extract_soup(ebay_url, 1, just_soup=True)


    # #HTML divided by products, and stored as elements of an array
    ebay_boxes = search_boxes(ebay_soup, Ebay.boxes)
    # print(ebay_boxes)

    ebay_products = {}

    ebay_products['names'] = get_names(ebay_boxes, Ebay.name_and_images)
    # #Ebay's images source (link)
    ebay_products['images'] = get_images(ebay_boxes, Ebay)

    ebay_products['urls'] = get_products_urls(ebay_boxes, Ebay)
    ebay_products['prices'] = get_price(country, ebay_boxes, Ebay.price)

    cheapest_idx = cheapest(ebay_products['prices'])
    cheapest_ebay_product2 = get_cheapest(cheapest_idx, ebay_products)

    print(f'\nTest ONE:')
    for key in cheapest_ebay_product2:
        print(key, ':', cheapest_ebay_product2[key])