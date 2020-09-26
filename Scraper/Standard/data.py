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


class Page:
    def __init__(self, __name__, url, url_replacers, space_replacer ,boxes, highlights,
    product_urls, url_get, name_and_images, names_get, images_get, reviews, stars, price, money_dict):
        self.__name__ = __name__
        '''Page URl with name of the format replacers'''
        self.url = url 

        '''Tuple with the name of the replacers'''
        self.url_replacers = url_replacers

        '''string that will replace the space of the users request on a search'''
        self.space_replacer = space_replacer

        '''All the next properties are tuples that contains:
        ("node: span", "attribute: class", "=predicate: text")'''
        self.boxes = boxes
        self.highlights = highlights

        #Products Info
        self.product_urls = product_urls
        self.url_get = url_get

        # self.product_id = product_id
        self.name_and_images = name_and_images
        self.names_get = names_get
        self.images_get = images_get
        
        self.reviews = reviews
        self.stars = stars
        self.price = price
        
        #dictionary
        self.money_dict = money_dict
        
    
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


class Products:
    def __init__(self, names, images_links, products_links, prices):
        self.names = names
        self.images = images_links
        self.products_links = products_links
        self.prices = prices

amazon_money_dict = {'mx' : {'coin' : '$',
                      'thousands': ',',
                      'decimal': '.',
                      'two_prices_sep' : ' - '}
}

Amazon = Page(__name__ = 'Amazon',
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

Ebay = Page(__name__='Ebay',
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
            
Mercado_Libre = Page(__name__='Mercado Libre',
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

if __name__ == '__main__':
    print(Amazon.__name__)