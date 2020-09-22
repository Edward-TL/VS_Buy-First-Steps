
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
    def __init__(self, url, url_replacers, space_replacer ,boxes, highlights,
    product_urls, name_and_images, reviews, stars, price):
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
        # self.product_id = product_id
        self.name_and_images = name_and_images
        self.reviews = reviews
        self.stars = stars
        self.price = price
        
    
    def adapt_url(self, Page, country_domain, user_request):
        if country_domain[0] != ".":
            country_domain = '.' + country_domain

        adapted_url = Page.url.replace(Page.url_replacers[0], country_domain)
        
        # for r in range(1, len(Page.url_replacers)):
        user_request_adapted = user_request.replace(' ', Page.space_replacer)
        adapted_url = adapted_url.replace(Page.url_replacers[1], user_request_adapted)
        

        return adapted_url

class Products:
    def __init__(self, names, images_links, products_links, prices):
        self.names = names
        self.images = images_links
        self.products_links = products_links
        self.prices = prices
        
Amazon = Page(url='https://www.amazon.com{country}/s?k={user_request}',
    url_replacers=('{country}', '{user_request}'),
    space_replacer='+',
    boxes=('div', 'data-component-type', 's-search-result'),
    highlights=('div', 'class', 'a-row a-badge-region'),
    product_urls=('a', 'class', 'a-link-normal a-text-normal'),
    name_and_images=('div', 'class', 'a-section aok-relative s-image-square-aspect'),
    reviews=('span', 'class', 'a-size-base'),
    stars=('span', 'class', 'a-icon-alt'),
    price=('span', 'class', 'a-offscreen'),
    #product_id('data-asin')
    )

coins_dict = {'mx':1,
                'br':2,}

Mercado_Libre = Page(url='https://listado.mercadolibre.com.{country}/{user_request}#D[A:{user_request}]',
    url_replacers=('{country}', '{user_request}'),
    space_replacer='%20',
    boxes=('div', 'class', 'ui-search-result__wrapper'),
    highlights=('span', 'class', 'ui-search-item__highlight-label__text'),
    product_urls=('a', 'class', 'a-link-normal a-text-normal'),
    name_and_images=('div', 'class', 'ui-search-result__image'),
    reviews=None,
    stars=None,
    price=('span', 'class', 'price-tag ui-search-price__part'),)

# Wallmart = Page(url='https://www.walmart.com{country}/productos?Ntt={request}',
#     url_replacers=('{country}', '{request}'),
#     space_replacer='%20')


if __name__ == '__main__':
    user_request = 'audifonos inalambricos'
    country = 'mx'
    amz_url = Amazon.adapt_url(Amazon, country, user_request)
    print(amz_url)
