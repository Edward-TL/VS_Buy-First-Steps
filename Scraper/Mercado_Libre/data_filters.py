from scrape_funcs import search_boxes
from data import coins_dict

def get_names(boxes_array, info_tuple, test_all=False, test_len=False, position=None):
    names = [None]*len(boxes_array)

    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], info_tuple)
        if searcher:
            names = searcher[0].img.get('alt')
    else:
        '''For Testing the functions and Xpaths'''
        b=0
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, info_tuple)
            if searcher:
                names[b] = searcher[0].img.get('alt')
                
            b +=1
    if test_all == True:
        print(names)
    
    elif test_len == True:
        print(len(names))

    return names


def get_images(boxes_array, info_tuple, test_all=False, test_len=False, position=None):
    images = [None]*len(boxes_array)
    
    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], info_tuple)
        if searcher:
            images = searcher[0].img.get('data-src')
    else:
        '''For Testing the functions and Xpaths'''
        b=0
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, info_tuple)
            if searcher:
                images[b] = searcher[0].img.get('data-src')
            b +=1

    if test_all == True:
        print(searcher[0].img)
        print(images)
    
    elif test_len == True:
        print('images:', len(images))

    return images

def get_products_urls(boxes_array, info_tuple, test_all=False, test_len=False, position=None):
    urls = [None]*len(boxes_array)

    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], info_tuple)
        if searcher:
            urls = searcher[0].a.get('href')
            
    else:
        '''For Testing the functions and Xpaths'''
        b=0
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, info_tuple)
            if searcher:
                urls[b] = searcher[0].a.get('href')
            b +=1

    if test_all == True:
        print(urls)
    
    elif test_len == True:
        print('urls:', len(urls))
    return urls

def get_price(country, boxes_array, info_tuple, test_all=False, test_len=False, position=None):
    price = [None]*len(boxes_array)
    coin_symbol = coins_dict[country]

    '''If you know want to know some info of an specific product by its position on the page.
    Like you know the position of the cheapest'''
    if position:
        searcher = search_boxes(boxes_array[position], info_tuple)
        if searcher:
            if country == 'mx':
                    try:
                        price[b] = float(searcher[0].get_text()[coin_symbol:].replace(',',''))
                    except:
                        pass
            elif country == 'br':
                try:
                    price[b] = float(searcher[0].get_text()[coin_symbol:].replace('.','').replace(',','.'))
                except:
                    pass
            
    #For Testing the functions and Xpaths
    else:
        b=0
        for box in boxes_array:
            #Remember that boxes are arrays
            searcher = search_boxes(box, info_tuple)
            if searcher:
                if country == 'mx':
                    try:
                        price[b] = float(searcher[0].get_text()[coin_symbol:].replace(',',''))
                    except:
                        pass
                elif country == 'br':
                    try:
                        price[b] = float(searcher[0].get_text()[coin_symbol:].replace('.','').replace(',','.'))
                    except:
                        pass
            b +=1

    if test_all == True:
        print(price)
    
    elif test_len == True:
        print('prices:', len(price))

    return price

def get_stars(country, boxes_array, info_tuple, test_all=False, test_len=False, position=None):
    stars = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)

        if searcher:
            if country == 'mx':
                stars[b] = float(searcher[0].get_text()[:3])
            if country == 'br':
                stars[b] = float(searcher[0].get_text()[:3].replace(',','.'))

        b +=1
    if test_all == True:
        print(stars)
    
    elif test_len == True:
        print('stars:', len(stars))
    return stars

def get_reviews(country, boxes_array, info_tuple, test_all=False, test_len=False, position=None):
    reviews = [None]*len(boxes_array)

    b=0
    for box in boxes_array:
        #Remember that boxes are arrays
        searcher = search_boxes(box, info_tuple)

        if searcher:
            if len(searcher) > 1:
                searcher = [searcher[0]]

            if country == 'mx':
                try:
                    reviews[b] = int(searcher[0].get_text().replace(',',''))
                except:
                    pass
            elif country == 'br':
                try:
                    reviews[b] = int(searcher[0].get_text().replace('.',''))
                except:
                    pass
        
        b +=1
    if test_all == True:
        print(reviews)
    
    elif test_len == True:
        print('reviews:', len(reviews))
    return reviews

# def ml_products_id(boxes_array, test_all=False, test_len=False):
#     ids = [None]*len(boxes_array)

#     b=0
#     for box in boxes_array:
#         #Remember that boxes are arrays
#         if box:
#             product_id = box.get('data-asin')
#             ids[b] = 'www.amazon.com.mx/dp/' + product_id
            
#         b +=1
#     if test == True:
#         print(ids)
#     return ids
