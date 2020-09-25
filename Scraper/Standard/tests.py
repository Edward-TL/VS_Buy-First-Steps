import unittest

from data import Amazon
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from page_getters import get_names, get_images, get_products_urls, get_price

#Amazon Only
from page_getters import get_stars, get_reviews


class Test_Amazon_Properties_And_Functions(unittest.TestCase):
    #Replacers
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)

        self.assertEqual(amazon_url, 'https://www.amazon.com.mx/s?k=audifonos+inalambricos')

    def test_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)

        amz_status = extract_soup(amazon_url, 0, just_status=True)

        self.assertEqual(amz_status,200)

    def test_there_is_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)

        amz_soup = extract_soup(amazon_url, 1, just_soup=True)

        self.assertIsNotNone(amz_soup)

    def test_get_brute_info_including_Nones(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)
        amz_soup = extract_soup(amazon_url, 1, just_soup=True)
        
        #New test
        amz_boxes = search_boxes(amz_soup, Amazon.boxes)
        self.assertEqual(len(amz_boxes), 60)

    def test_get_brute_info_without_losses(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

        #New test
        amazon_string_stars = get_brute_info(amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_string_stars))

    def test_get_stars_without_losses(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)
        amazon_string_stars = get_brute_info(amazon_boxes, Amazon.stars)
        
        #New test
        amazon_stars = get_stars(country, amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_string_stars), len(amazon_stars))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, user_request, country)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

        amazon_names = len(get_names(amazon_boxes, Amazon.name_and_images))
        amazon_images = len(get_images(amazon_boxes, Amazon))
        amazon_urls = len(get_products_urls(amazon_boxes, Amazon))
        amazon_price = len(get_price(country, amazon_boxes, Amazon.price))
        amazon_reviews = len(get_reviews(country, amazon_boxes, Amazon.reviews))
        amazon_stars = len(get_stars(country, amazon_boxes, Amazon.stars))

        trials = [amazon_names, amazon_images, amazon_urls, amazon_price, amazon_reviews, amazon_stars]
        for test in trials:
            self.assertEqual(len(amazon_boxes), test)

unittest.main()

