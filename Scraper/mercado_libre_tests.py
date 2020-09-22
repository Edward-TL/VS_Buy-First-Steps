import unittest

from General.scrape_data import Mercado_Libre
from General.scrape_funcs import extract_soup, search_boxes, get_brute_info
from Amazon.data_filters import get_names, get_images, get_products_urls, get_price


class Test_Mercado_Libre_Properties_And_Functions(unittest.TestCase):
    def test_adapt_url(self):
        user_request = 'audifonos inalambricos'
        country = 'mx'
        ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)

        self.assertEqual(ml_url, 'https://listado.mercadolibre.com.mx/audifonos-inalambricos#D[A:audifonos%20inalambricos]')

    # def test_mercado_libre_conection_status(self):
    #     user_request = 'audifonos inalambricos'
    #     ml_user_request_edited = user_request.replace(' ', Mercado_Libre.space_replacer)
    #     ml_url = Mercado_Libre.url.replace(Mercado_Libre.url_replacers[0], 'mx')
    #     ml_url = ml_url.replace(Mercado_Libre.url_replacers[1], ml_user_request_edited)

    #     ml_status = extract_soup(ml_url, 0, just_status=True)

    #     self.assertEqual(ml_status,200)

    # def test_there_is_soup(self):
    #     user_request = 'audifonos inalambricos'
    #     country = 'mx'
    #     ml_url = Mercado_Libre.adapt_url(Mercado_Libre, country, user_request)

    #     ml_soup = extract_soup(ml_url, 1, just_soup=True)

    #     self.assertIsNotNone(ml_soup)


unittest.main()

