import unittest

from data import Mercado_Libre
from scrape_funcs import extract_soup, search_boxes, get_brute_info
from page_getters import get_names, get_images, get_products_urls, get_price
from cheapest_funcs import cheapest, get_cheapest


class Test_Mercado_Libre_Properties_And_Functions(unittest.TestCase):
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, user_request, country)

        self.assertEqual(ml_url, 'https://listado.mercadolibre.com.mx/audifonos-inalambricos#D[A:audifonos%20inalambricos]')

    def test_mercado_libre_conection_status(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, user_request, country)

        ml_status = extract_soup(ml_url, 0, just_status=True)

        self.assertEqual(ml_status,200)

    def test_there_is_soup(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, user_request, country)

        ml_soup = extract_soup(ml_url, 1, just_soup=True)

        self.assertIsNotNone(ml_soup)

    def test_get_brute_info_including_Nones(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, user_request, country)
        ml_soup = extract_soup(ml_url, 1, just_soup=True)
        
        #New test
        ml_boxes = search_boxes(ml_soup, Mercado_Libre.boxes)
        
        self.assertIsNotNone(len(ml_boxes))

    def test_products_info_getters(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, user_request, country)
        ml_soup = extract_soup(ml_url, 1, just_soup=True)
        ml_boxes = search_boxes(ml_soup, Mercado_Libre.boxes)

        getters = {'ml_names' : len(get_names(ml_boxes, Mercado_Libre.name_and_images)),
        'ml_images' : len(get_images(ml_boxes, Mercado_Libre)),
        'ml_urls' : len(get_products_urls(ml_boxes, Mercado_Libre)),
        'ml_price' : len(get_price(country, ml_boxes, Mercado_Libre.price)),
        }
        
        for value in getters:
            self.assertEqual(len(ml_boxes), getters[value])
    
    

    def test_cheapest_gets_info(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'

        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, user_request, country)
        ml_soup = extract_soup(ml_url, 1, just_soup=True)
        ml_boxes = search_boxes(ml_soup, Mercado_Libre.boxes)
        meli_prices= get_price(country, ml_boxes, Mercado_Libre.price)

        meli_cheapest_idx, meli_cheapest_price = cheapest(meli_prices, position_and_price=True)
        cheapest_ml_product_1 = get_cheapest(meli_cheapest_idx, ml_boxes, meli_cheapest_price, country, Mercado_Libre)

        for value in cheapest_ml_product_1:
            self.assertIsNotNone(cheapest_ml_product_1[value])

unittest.main()