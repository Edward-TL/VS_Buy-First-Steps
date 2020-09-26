from dataclasses import dataclass

@dataclass
class Page:
    name:str
    '''Page URl with name of the format replacers'''
    url : str
    '''Tuple with the name of the replacers'''
    url_replacers : tuple
    '''string that will replace the space of the users request on a search'''
    space_replacer : tuple
    '''All the next properties are tuples that contains:
    ("node: span", "attribute: class", "=predicate: text")'''
    boxes : tuple
    '''Products Info'''
    product_urls : tuple
    url_get : str
    # self.product_id = product_id
    name_and_images : tuple
    names_get : str
    images_get : str
    '''All the next properties are tuples that contains:
    ("node: span", "attribute: class", "=predicate: text")'''
    reviews : tuple
    stars : tuple
    price : tuple
    highlights : tuple
    '''dictionary'''
    money_dict : dict      
    
    def adapt_url(self, Page, user_request, country_domain):
        check = str(type(Page.url_replacers))
        if country_domain[0] != ".":
            country_domain = '.' + country_domain
        
        
        if check != "<class 'str'>":
            adapted_url = Page.url.replace(Page.url_replacers[0], country_domain)
            for r in range(1, len(Page.url_replacers)):
                user_request_adapted = user_request.replace(' ', Page.space_replacer[r-1])
                adapted_url = adapted_url.replace(Page.url_replacers[r], user_request_adapted)
        else:
            user_request_adapted = user_request.replace(' ', Page.space_replacer[0])
            adapted_url = Page.url.replace(Page.url_replacers, user_request_adapted)
        
        return adapted_url

amazon_money_dict = {'mx' : {'coin' : '$',
                      'thousands': ',',
                      'decimal': '.',
                      'two_prices_sep' : ' - '}
}

Amazon = Page(name = 'Amazon',
    url='https://www.amazon.com{country}/s?k={user_request}',
    url_replacers=('{country}', '{user_request}'),
    space_replacer=['+'],
    boxes=('div', 'data-component-type', 's-search-result'),
    highlights=('div', 'class', 'a-row a-badge-region'),
    url_get='href',
    product_urls=('a', 'class', 'a-link-normal a-text-normal'),
    name_and_images=('div', 'class', 'a-section aok-relative s-image-square-aspect'),
    names_get='alt',
    images_get='src',
    reviews=('span', 'class', 'a-size-base'),
    stars=('span', 'class', 'a-icon-alt'),
    price=('span', 'class', 'a-offscreen'),
    money_dict=amazon_money_dict,
    #product_id('data-asin')
    )

ebay_money_dict = {'mx' : {'coin' : 'MXN $',
                      'thousands': ' ',
                      'decimal': '.',
                      'two_prices_sep' : ' a '}
            }

Ebay = Page(name='Ebay',
    url='https://www.ebay.com/sch/i.html?_nkw={user_request}',
    url_replacers=('{user_request}'),
    space_replacer=['+'],
    boxes=('li', 'class', 's-item'),
    highlights=('span', 'class', 'ui-search-item__highlight-label__text'),
    product_urls=('div', 'class', 's-item__image'),
    url_get='href',
    name_and_images=('div', 'class', 's-item__image-wrapper'),
    names_get='alt',
    images_get='src',
    reviews=None,
    stars=None,
    price=('span', 'class', 's-item__price'),
    money_dict=ebay_money_dict,)

meli_money_dict = {'mx' : {'coin' : '$',
                      'thousands': ',',
                      'decimal': '.',
                      'two_prices_sep' : ' - '}
            }
            
Mercado_Libre = Page(name='Mercado Libre',
    url='https://listado.mercadolibre.com{country}/{user_request_1}#D[A:{user_request_2}]',
    url_replacers=('{country}', '{user_request_1}', '{user_request_2}'),
    space_replacer=['-','%20'],
    boxes=('div', 'class', 'ui-search-result__wrapper'),
    highlights=('span', 'class', 'ui-search-item__highlight-label__text'),
    product_urls=('div', 'class', 'ui-search-result__image'),
    url_get='href',
    name_and_images=('div', 'class', 'slick-slide slick-active'),
    names_get='alt',
    images_get='data-src',
    reviews=None,
    stars=None,
    price=('span', 'class', 'price-tag ui-search-price__part'),
    money_dict=meli_money_dict,)

wallmart_money_dict = {'mx' : {'coin' : '$',
                      'thousands': ',',
                      'decimal': '.',
                      'two_prices_sep' : ' - '}
}

Wallmart = Page(name = 'Wallmart',
    url='https://www.walmart.com{country}/productos?Ntt={user_request}',
    url_replacers=('{country}', '{user_request}'),
    space_replacer=['%20'],
    boxes=('div', 'data-automation-id', 'production-index-0'),
    highlights=None,
    product_urls=('a', 'class', 'nav-link_navLink__2oJ29 product_image__LcsAj'),
    url_get='href',
    name_and_images=('span', 'class', 'lazyload-wrapper'),
    names_get='alt',
    images_get='src',
    reviews=None,
    stars=None,
    price=('p', 'data-automation-id', 'sale-price'),
    money_dict=wallmart_money_dict,
    #product_id('data-asin')
    )

class headers:
    wallmart = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
                'cache-control':'max-age=0',
                'upgrade-insecure-requests':'1',
                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

    h0 = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding":"gzip, deflate",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT":"1",
            "Connection":"close",
            "Upgrade-Insecure-Requests":"1"}

    h1 = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)AppleWebKit/605.1.15 (KHTML, like Gecko)Version/12.1.1 Safari/605.1.15",
            "Accept-Encoding":"gzip, deflate",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT":"1",
            "Connection":"close",
            "Upgrade-Insecure-Requests":"1"}

    h2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Accept-Encoding":"gzip, deflate",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT":"1",
            "Connection":"close",
            "Upgrade-Insecure-Requests":"1"}

    common = (h0, h2, h2)
    h3 = wallmart
    all_saved = (h0, h2, h2, wallmart)

class Products:
    def __init__(self, names, images_links, products_links, prices):
        self.names = names
        self.images = images_links
        self.products_links = products_links
        self.prices = prices



if __name__ == '__main__':
    print(Amazon)