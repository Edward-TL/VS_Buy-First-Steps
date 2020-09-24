import unittest

from data import Ebay
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from page_getters import get_names, get_images, get_products_urls, get_price
from cheapest_funcs import cheapest, get_cheapest


class Test_Ebay_Properties_And_Functions(unittest.TestCase):
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ebay_url = Ebay.adapt_url(Ebay, user_request, country_domain=country)

        self.assertEqual(ebay_url, 'https://www.ebay.com/sch/i.html?_nkw=audifonos+inalambricos')

    def test_Ebay_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ebay_url = Ebay.adapt_url(Ebay, user_request, country)

        ebay_status = extract_soup(ebay_url, 0, just_status=True)

        self.assertEqual(ebay_status,200)

    def test_there_is_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ebay_url = Ebay.adapt_url(Ebay, user_request, country)

        ebay_soup = extract_soup(ebay_url, 1, just_soup=True)

        self.assertIsNotNone(ebay_soup)

    def test_get_brute_info_including_Nones(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ebay_url = Ebay.adapt_url(Ebay, user_request, country)
        ebay_soup = extract_soup(ebay_url, 1, just_soup=True)
        
        #New test
        ebay_boxes = search_boxes(ebay_soup, Ebay.boxes)
        
        self.assertIsNotNone(len(ebay_boxes))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ebay_url = Ebay.adapt_url(Ebay, user_request, country)
        ebay_soup = extract_soup(ebay_url, 1, just_soup=True)
        ebay_boxes = search_boxes(ebay_soup, Ebay.boxes)

        getters = {'ebay_names' : len(get_names(ebay_boxes, Ebay.name_and_images)),
        'ebay_images' : len(get_images(ebay_boxes, Ebay)),
        'ebay_urls' : len(get_products_urls(ebay_boxes, Ebay)),
        # 'ebay_price' : len(get_price(country, ebay_boxes, Ebay.price)),
        }
        
        for value in getters:
            self.assertEqual(len(ebay_boxes), getters[value])
    
    

    def test_cheapest_gets_info(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'

        ebay_url = Ebay.adapt_url(Ebay, user_request, country)
        ebay_soup = extract_soup(ebay_url, 1, just_soup=True)
        ebay_boxes = search_boxes(ebay_soup, Ebay.boxes)
        ebay_prices= get_price(country, ebay_boxes, Ebay.price)

        ebay_cheapest_idx, ebay_cheapest_price = cheapest(ebay_prices, position_and_price=True)
        cheapest_ebay_product_1 = get_cheapest(ebay_cheapest_idx, ebay_boxes, ebay_cheapest_price, country, Ebay)

        for value in cheapest_ebay_product_1:
            self.assertIsNotNone(cheapest_ebay_product_1[value])

unittest.main()