from data import Amazon, Ebay, Mercado_Libre
from scrape_funcs import extract_soup, search_boxes
from page_getters import get_price
from cheapest_funcs import cheapest, get_cheapest

def scrap_cheapest(user_request, Page, country='mx'):
    #Adapt the url
    request_url = Page.adapt_url(Page, user_request, country)
    #All the HTML of the page
    soup_request = extract_soup(request_url, 1, just_soup=True)
    # #HTML divided by products, and stored as elements of an array
    page_boxes = search_boxes(soup_request, Page.boxes)
    # From this part, could get better AFTER the 4 scrapers are made
    #From the Boxes, obtain the prices
    price_boxes = get_price(country, page_boxes, Page)
    #Obtain the cheapest from prices and then, you obtain the cheapest product as a dictionary
    cheapest_idx, cheapest_price = cheapest(price_boxes, position_and_price=True)
    cheapest_product_dictionary = get_cheapest(cheapest_idx, page_boxes, cheapest_price, country, Page)

    return cheapest_product_dictionary

if __name__ == '__main__':
    user_request = 'audifonos marshall bluetooth major'
    pages = [Amazon, Ebay, Mercado_Libre]
    for page in pages:
        print(f'Searching {user_request} in -> {page.__name__}')
        cheapest_dict = scrap_cheapest(user_request, page)
        for key in cheapest_dict:
            print(key,':', cheapest_dict[key])
        print('\n')
