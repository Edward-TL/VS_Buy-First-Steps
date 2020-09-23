import unittest

from data import Mercado_Libre
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from data_filters import get_names, get_images, get_products_urls, get_price


class Test_Mercado_Libre_Properties_And_Functions(unittest.TestCase):
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)

        self.assertEqual(ml_url, 'https://listado.mercadolibre.com.mx/audifonos-inalambricos#D[A:audifonos%20inalambricos]')

    def test_mercado_libre_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)

        ml_status = extract_soup(ml_url, 0, just_status=True)

        self.assertEqual(ml_status,200)

    def test_there_is_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)

        ml_soup = extract_soup(ml_url, 1, just_soup=True)

        self.assertIsNotNone(ml_soup)

    def test_get_brute_info_including_Nones(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)
        ml_soup = extract_soup(ml_url, 1, just_soup=True)
        
        #New test
        ml_boxes = search_boxes(ml_soup, Mercado_Libre.boxes)
        
        self.assertIsNotNone(len(ml_boxes))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)
        ml_soup = extract_soup(ml_url, 1, just_soup=True)
        ml_boxes = search_boxes(ml_soup, Mercado_Libre.boxes)

        getters = {'ml_names' : len(get_names(ml_boxes, Mercado_Libre.name_and_images)),
        'ml_images' : len(get_images(ml_boxes, Mercado_Libre.name_and_images)),
        # 'ml_urls' : len(get_products_urls(ml_boxes, Mercado_Libre.product_urls)),
        # 'ml_price' : len(get_price(country, ml_boxes, Mercado_Libre.price)),
        # 'ml_ids' : len(ml_products_id(ml_boxes)),
        # 'ml_reviews' : len(get_reviews(country, ml_boxes, Mercado_Libre.reviews)),
        # 'ml_stars' : len(get_stars(country, ml_boxes, Mercado_Libre.stars)),
        }
        
        for value in range(len(getters)):
            self.assertEquals(len(ml_boxes), getters[value])
unittest.main()