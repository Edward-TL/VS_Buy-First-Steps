from scrape_funcs import search_boxes
import re

def get_names(boxes_array, Page, test_all=False, test_len=False, position=None):
    names = [None]*len(boxes_array)
    name = Page.names_get

    if test_all == True:
            print(f'Boxes array len: {len(boxes_array)}')

    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position != None:
        searcher = search_boxes(boxes_array[position], Page.name_and_images)
        if searcher:
            if Page.name == 'Best Buy':
                image_name = searcher[0].img.get(name)
                name_split = image_name.split(' - ')
                names = name_split[1]
            else:
                names = searcher[0].img.get(name)
    else:
        '''For Testing the functions and Xpaths'''
        b=0
        if test_all == True:
            print('For Loop')
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, Page.name_and_images)
            if searcher:
                try:
                    if Page.name == 'Best Buy':
                        image_name = searcher[0].img.get(name)
                        name_split = image_name.split(' - ')
                        names[b] = name_split[1]
                    else:
                        names[b] = searcher[0].img.get(name)
                except:
                    name_message_error = f'''Value info:
                    box: {box}
                    Searcher: {searcher}
                    Searcher[0].img = {searcher[0].img}'''

                    raise ValueError(name_message_error)
                
            b +=1
    if test_all == True:
        print(names)
    
    elif test_len == True:
        print(len(names))

    return names


def get_images(boxes_array, Page, test_all=False, test_len=False, position=None):
    images = [None]*len(boxes_array)
    image = Page.images_get
    
    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], Page.name_and_images)

        if searcher:
            images = searcher[0].img.get(image)
    else:
        '''For Testing the functions and Xpaths'''
        b=0
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, Page.name_and_images)
            if searcher:
                images[b] = searcher[0].img.get(image)
            b +=1

    if test_all == True:
        print(images)
    
    elif test_len == True:
        print('images:', len(images))

    return images

def get_products_urls(boxes_array, Page, test_all=False, test_len=False, position=None):
    urls = [None]*len(boxes_array)
    url = Page.url_get
    if test_all == True:
        print('Urls:')
    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], Page.product_urls)
        if searcher:
            try:
                if Page.name == 'Amazon':
                    source_url = searcher[0].get(url)
                    position_url = 'https://www.amazon.com.mx' + source_url
                    
                else:
                    position_url = searcher[0].a.get(url)
                
                urls = position_url
            except:
                error_message = f'''Value info:
                Searcher: {searcher}
                searcher[0]: {searcher}
                searcher[0].a: searcher[0].a
                url: {Page.url_get}
                position: {position}
                '''

                raise ValueError(error_message)
    else:
        '''For Testing the functions and Xpaths'''
        b=0
        for box in boxes_array:
            if test_all == True:
                print('For loop:')
            #Remember that boxes are arrays
            searcher = search_boxes(box, Page.product_urls)
            if searcher:
                if test_all == True:
                    print(searcher[0].a)
                if Page.name == 'Amazon':
                    source_url = searcher[0].get(url)
                    urls[b] = 'https://www.amazon.com.mx' + source_url
                    
                else:
                    urls[b] = searcher[0].a.get(url)
            b +=1

    if test_all == True:
        print(urls)
    
    elif test_len == True:
        print('urls:', len(urls))
    return urls

def get_price(country, boxes_array, Page, test_all=False, test_len=False, position=None):
    price = [None]*len(boxes_array)
    coin_symbol = Page.money_dict[country]['coin']
    k_sep = Page.money_dict[country]['thousands']
    d_sep = Page.money_dict[country]['decimal']
    tps = Page.money_dict[country]['two_prices_sep']
    price_string = 'start'

    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], Page.price)
        if searcher:
            try:
                price_string = searcher[0].get_text().split(tps)
                price_string = price_string[0].replace(coin_symbol,'').replace(k_sep,'').replace(d_sep,'.')
                #Special case
                price_string = re.findall(r'(\d+\.\d+)', price_string)
                price = float(price_string[0])
            except:
                error_message = f'''String index out of range. 
                Money dictionary: {Page.money_dict}
                Original String: {searcher[0].get_text()}
                Box #{position}'''
                raise ValueError(error_message)     
        
    #For Testing the functions and Xpaths
    else:
        b=0
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, Page.price)
            if test_all == True:
                print(searcher)
            if searcher:
                if country == 'mx':
                    try:
                        price_string = searcher[0].get_text().split(tps)
                        if test_all == True:
                            print(price_string)
                        price_string_bfre = price_string[0].replace(coin_symbol,'').replace(k_sep,'').replace(d_sep,'.')
                        if test_all == True:
                            print(price_string) 
                        #Ebays Special case
                        price_string_bfre = price_string_bfre.replace('\xa0','')
                        #Just in case
                        price_string_check = re.findall(rf"(\d+\.?\d+)", price_string_bfre)
                        price[b] = float(price_string_check[0])                        

                    except:
                        error_message = f'''Info about the Value. 
                        Money dictionary: {Page.money_dict}
                        Original String: {searcher[0].get_text()}
                        Before RegEx: {price_string_bfre}
                        Type Before RegEx: {type(price_string)}
                        Price string: {price_string}
                        Box #{b}'''
                        raise ValueError(error_message)                        
            b +=1

    if test_all == True:
        print('prices:', len(price), price)
    
    elif test_len == True:
        print('prices:', len(price))

    return price

def get_stars(boxes_array, Page, country='mx', test_all=False, test_len=False, position=None):
    stars = [None]*len(boxes_array)
    decimal_sep = Page.money_dict[country]['decimal']

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, Page.stars)

        if searcher:
            if decimal_sep == '.':
                stars[b] = float(searcher[0].get_text()[:3])
            else:
                stars[b] = float(searcher[0].get_text()[:3].replace(decimal_sep,''))

        b +=1
    if test_all == True:
        print(stars)
    
    elif test_len == True:
        print('stars:', len(stars))
    return stars

def get_reviews(boxes_array, Page, country='mx', test_all=False, test_len=False, position=None):
    reviews = [None]*len(boxes_array)
    comma_sep = Page.money_dict[country]['thousands']

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, Page.reviews)

        if searcher:
            if len(searcher) > 1:
                searcher = [searcher[0]]

            try:
                reviews[b] = int(searcher[0].get_text().replace(comma_sep,''))
            except:
                pass
        
        b +=1
    if test_all == True:
        print(reviews)
    
    elif test_len == True:
        print('reviews:', len(reviews))
    return reviews

def amazon_products_id(boxes_array, test=False):
    ids = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        if box:
            product_id = box.get('data-asin')
            ids[b] = 'www.amazon.com.mx/dp/' + product_id
            
        b +=1
    if test == True:
        print(ids)
    return ids

