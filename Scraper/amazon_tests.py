import unittest

from General.scrape_data import Amazon
from General.scrape_funcs import extract_soup, search_boxes, get_brute_info
from Amazon.data_filters import get_names, get_images, get_products_urls, get_price

#Amazon Only
from Amazon.data_filters import get_stars, get_reviews, amazon_products_id


class Test_Amazon_Properties_And_Functions(unittest.TestCase):
    #Replacers
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)

        self.assertEqual(amz_url, 'https://www.amazon.com.mx/s?k=audifonos+inalambricos')

    def test_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)

        amz_status = extract_soup(amz_url, 0, just_status=True)

        self.assertEqual(amz_status,200)

    def test_there_is_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)

        amz_soup = extract_soup(amz_url, 1, just_soup=True)

        self.assertIsNotNone(amz_soup)

    def test_get_brute_info_including_Nones(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amz_url = Amazon.adapt_url(Amazon, country, user_request)
        amz_soup = extract_soup(amz_url, 1, just_soup=True)
        
        #New test
        amz_boxes = search_boxes(amz_soup, Amazon.boxes)
        self.assertEqual(len(amz_boxes), 60)

    def test_get_brute_info_without_losses(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, country, user_request)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

        #New test
        amazon_string_stars = get_brute_info(amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_string_stars))

    def test_get_stars_without_losses(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, country, user_request)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)
        amazon_string_stars = get_brute_info(amazon_boxes, Amazon.stars)
        
        #New test
        amazon_stars = get_stars(country, amazon_boxes, Amazon.stars)
        self.assertEqual(len(amazon_boxes), len(amazon_string_stars), len(amazon_stars))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        amazon_url = Amazon.adapt_url(Amazon, country, user_request)
        amazon_soup = extract_soup(amazon_url, 1, just_soup=True)
        amazon_boxes = search_boxes(amazon_soup, Amazon.boxes)

        amazon_names = len(get_names(amazon_boxes, Amazon.name_and_images))
        amazon_images = len(get_images(amazon_boxes, Amazon.name_and_images))
        amazon_urls = len(get_products_urls(amazon_boxes, Amazon.product_urls))
        amazon_price = len(get_price(country, amazon_boxes, Amazon.price))
        amazon_ids = len(amazon_products_id(amazon_boxes))
        amazon_reviews = len(get_reviews(country, amazon_boxes, Amazon.reviews))
        amazon_stars = len(get_stars(country, amazon_boxes, Amazon.stars))

        trials = [amazon_names, amazon_images, amazon_urls, amazon_price, amazon_ids, amazon_reviews, amazon_stars]
        for test in trials:
            self.assertEquals(len(amazon_boxes), test)

unittest.main()

