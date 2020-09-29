import unittest

from data import Amazon, Mercado_Libre, Ebay, Best_Buy
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from page_getters import get_names, get_images, get_products_urls, get_price

#Best_Buy Only
from page_getters import get_stars, get_reviews


class Test_Pages_Properties_And_Functions(unittest.TestCase):

    def setUp(self):
        self.Pages = [Amazon, Mercado_Libre, Ebay, Best_Buy]

    #Replacers
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'

        for Page in self.Pages:
            page_url = Page.adapt_url(Page, user_request, country)

            self.assertEqual(page_url, Page.page_test)

    def test_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        for Page in self.Pages:
            page_url = Page.adapt_url(Page, user_request, country)
            #New test:
            conection_status = extract_soup(page_url, 0, just_status=True)

            self.assertEqual(conection_status,200)

    def test_extract_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        for Page in self.Pages:
            page_url = Page.adapt_url(Page, user_request, country)
            #New test:
            page_soup = extract_soup(page_url, 1, just_soup=True)

            self.assertIsNotNone(page_soup)

    def test_get_product_boxes(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        for Page in self.Pages:
            page_url = Page.adapt_url(Page, user_request, country)
            page_soup = extract_soup(page_url, 1, just_soup=True)
        
            #New test
            page_boxes = search_boxes(page_soup, Page.boxes)
            self.assertIsNotNone(len(page_boxes))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        for Page in self.Pages:
            page_url = Page.adapt_url(Page, user_request, country)
            page_soup = extract_soup(page_url, 1, just_soup=True)
            page_boxes = search_boxes(page_soup, Page.boxes)
            #New test
            page_names = len(get_names(page_boxes, Page))
            page_images = len(get_images(page_boxes, Page))
            page_urls = len(get_products_urls(page_boxes, Page))
            page_price = len(get_price(country, page_boxes, Page))
            
            trials = [page_names, page_images, page_urls, page_price]
            for test in trials:
                self.assertEqual(len(page_boxes), test)

unittest.main()

