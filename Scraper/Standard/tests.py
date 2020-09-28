import unittest

from data import Best_Buy
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from page_getters import get_names, get_images, get_products_urls, get_price

#Best_Buy Only
from page_getters import get_stars, get_reviews


class Test_Best_Buy_Properties_And_Functions(unittest.TestCase):
    #Replacers
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        best_buy_url = Best_Buy.adapt_url(Best_Buy, user_request, country)

        self.assertEqual(best_buy_url, Best_Buy.page_test)

    def test_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        best_buy_url = Best_Buy.adapt_url(Best_Buy, user_request, country)

        best_buy_status = extract_soup(best_buy_url, 0, just_status=True)

        self.assertEqual(best_buy_status,200)

    def test_extract_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        best_buy_url = Best_Buy.adapt_url(Best_Buy, user_request, country)

        best_buy_soup = extract_soup(best_buy_url, 1, just_soup=True)

        self.assertIsNotNone(best_buy_soup)

    def test_get_product_boxes(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        best_buy_url = Best_Buy.adapt_url(Best_Buy, user_request, country)
        best_buy_soup = extract_soup(best_buy_url, 1, just_soup=True)
        
        #New test
        best_buy_boxes = search_boxes(best_buy_soup, Best_Buy.boxes)
        self.assertIsNotNone(len(best_buy_boxes))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        best_buy_url = Best_Buy.adapt_url(Best_Buy, user_request, country)
        best_buy_soup = extract_soup(best_buy_url, 1, just_soup=True)
        best_buy_boxes = search_boxes(best_buy_soup, Best_Buy.boxes)

        best_buy_names = len(get_names(best_buy_boxes, Best_Buy))
        best_buy_images = len(get_images(best_buy_boxes, Best_Buy))
        best_buy_urls = len(get_products_urls(best_buy_boxes, Best_Buy))
        best_buy_price = len(get_price(country, best_buy_boxes, Best_Buy))
        
        trials = [best_buy_names, best_buy_images, best_buy_urls, best_buy_price]
        for test in trials:
            self.assertEqual(len(best_buy_boxes), test)

unittest.main()

