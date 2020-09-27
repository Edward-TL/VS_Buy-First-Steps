from data import Best_Buy
from cheapest_funcs import cheapest, get_cheapest
from scrape_funcs import extract_soup, search_boxes, get_brute_info

from page_getters import get_names, get_images, get_products_urls, get_price


if __name__ == '__main__':
    user_request = 'lavadoras'
    country = 'mx'
    best_buy_url = Best_Buy.adapt_url(Best_Buy, user_request, country)

    #All the HTML of the page
    best_buy_soup = extract_soup(best_buy_url, 1, just_soup=True)


    # #HTML divided by products, and stored as elements of an array
    best_buy_boxes = search_boxes(best_buy_soup, Best_Buy.boxes)
    # print(best_buy_boxes)

    best_buy_products = {}

    best_buy_products['names'] = get_names(best_buy_boxes, Best_Buy)
    # #Best_Buy's images source (link)
    best_buy_products['images'] = get_images(best_buy_boxes, Best_Buy)

    best_buy_products['urls'] = get_products_urls(best_buy_boxes, Best_Buy)
    best_buy_products['prices'] = get_price(country, best_buy_boxes, Best_Buy)

    cheapest_idx = cheapest(best_buy_products['prices'])
    cheapest_best_buy_product2 = get_cheapest(cheapest_idx, best_buy_products)

    print(f'\nTest ONE:')
    for key in cheapest_best_buy_product2:
        print(key, ':', cheapest_best_buy_product2[key])