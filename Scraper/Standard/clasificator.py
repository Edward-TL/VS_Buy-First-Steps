# Statistics methods adapted to work with None values
from statistics import mean, std, max_and_min, max_with_none, min_with_none

def params(products_dict, method_x, method_y, x_adjustment=0.85, y_adjustment=1):
    x = products_dict['prices']
    y = products_dict['hit points']

    if method_x == 'Stads':
        price_std_less = mean(x) - 1*std(x)
        # For some products, the standard desviation turns to be huge,
        # making a rest of ONE standar desviation negative. Preventing
        # that case, the max method is forced.
        if price_std_less < 0:
            max_x, min_x = max_and_min(x)
            price_std_plus = max_x
            price_mean = max_x/2
            price_std_less = min_x

        # Is not, the other variables are stimaded
        else:
            price_std_plus =  mean(x) + 1*std(x)
            price_mean = mean(x)

    if method_y == 'Stads':
        hit_emergency = False
        hits_std_plus = mean(y) + 1*std(y)
        hits_mean = mean(y)
        hits_std_less = mean(y) - 5*std(y)
        
        # The emergency in hits means that there's no relevant product in the
        # search. In that case, the emergency is activaded and the price turns
        # to be the only axis of reference.
        if hits_std_plus == 0 and hits_mean == 0 and hits_std_less == 0:
            hit_emergency = True
        else:
            hit_emergency = False
    
    if method_x == 'Max':
        max_x, min_x = max_and_min(x)
        price_std_plus = max_x * x_adjustment
        price_mean = (max_x + min_x)/2
        price_std_less = min_x + (max_x * (1-x_adjustment))

    if method_y == 'Max':
        hit_emergency = False

        max_y, min_y = max_and_min(y)
        hits_std_plus = max_y
        hits_std_less = min_y

        hits_mean = (max_y + min_y)/2
        
    # Params are not added to the product_dict in this function,
    # because they're not someting to storage in DB. Are only saved
    # in case of graphing
    params = {'price_std_plus' : price_std_plus,
                'price_mean' : price_mean,
                'price_std_less' : price_std_less,
                'hits_std_plus' : hits_std_plus,
                'hits_mean' : hits_mean,
                'hits_std_less' : hits_std_less,
                'hit_emergency' : hit_emergency,
                }
    return params

def categories(products_dict, params, method_y, colors_dict=None):
    colors = ['None'] * len(products_dict['names'])
    clasification = ['None'] * len(products_dict['names'])
    sizes = [15] * len(products_dict['names'])

    if colors_dict == None:
        colors_dict = {'Ignored' : 'Black',
               'areas_choose':'LawnGreen',
                'Desireable': 'Blue',
                "Expensive but Requested": 'Green',
                "Couldn't find better": 'Gold',
                "Emergency Case": 'Crimson'
                }

    # Establish the cheapest storage info in the stangard categories
    cheapest_stock = {'Desireable': [None, None],
                      'Expensive but Requested': [None, None],
                      "Couldn't find better": [None, None],
                      'Emergency Case': [None, None],
                      'Ignored': [None, None],
                      }

    # Etablish the y's params for the clasification, by methods and relevance risk
    hit_emergency = params['hit_emergency']
    if method_y == 'Max':
        hit_param_top = hit_param_low = params['hits_mean']
    elif method_y == 'Stads':
        hit_param_top, hit_param_low = params['hits_std_plus'], params['hits_std_less']

    price_std_plus = params['price_std_plus']
    price_mean = params['price_mean']
    price_std_less = params['price_std_less']


    # Loop that returns the category of every product
    for product in range(len(products_dict['names'])):
        price = products_dict['prices'][product]
        hit = products_dict['hit points'][product]

        if price != None :
            # Right side of price
            if price >= price_mean and price <= price_std_plus:
                if hit > hit_param_top or hit_emergency == True:
                    category = 'Expensive but Requested'
                elif (hit <= hit_param_top) or (method_y == 'Stads' and hit >= hit_param_low and hit <= hit_param_top):
                    category = 'Emergency Case'
                    # Expensive and not relevant
                else:
                    category = "Ignored"

            # Left side of price
            elif price <= price_mean and price >= price_std_less:
                if hit >= hit_param_top or hit_emergency == True:
                    category = 'Desireable'
                elif (hit <= hit_param_top) or (method_y == 'Stads' and hit >= hit_param_low and hit <= hit_param_top):
                    category = "Couldn't find better"
                else:
                    # Cheap but not relevant
                    category = "Ignored"
            # Extreamly cheap or expensive for the page parameters.
            # Understanding that if you search for a console, this case is like an spare part 
            else:
                category = "Ignored"
        # There's no price (None) but there's product. Primortly, issue of Amazon
        else:
            category = "Ignored"
        

        if price != None: # If there's price, it would be stored and compared
            stock_price = cheapest_stock[category][0]

            # First time that the category recieves info
            if stock_price == None:
                cheapest_stock[category][0] = price
                cheapest_stock[category][1] = product

            # There was a price before, and needs a comparation
            else:
                if price < stock_price:
                    cheapest_stock[category][0] = price
                    cheapest_stock[category][1] = product

        clasification[product] = category
        colors[product] = colors_dict[category]

    return clasification, cheapest_stock, colors, sizes


# Search in the stock wich one is the must relevant (by category),
# and the cheapest (previusly compared at the moment of storage).
def category_loop(cheapest_stock):
    areas = iter(cheapest_stock.items())
    while True:
        try: 
            area = next(areas)
            if area[1][0] != None:
                category_given = area[0]
                raise StopIteration
        except StopIteration:
            break
    return category_given

def add_clasification_info(products_dict, method_x='Max', method_y='Max', x_adjustment=None,
 y_adjustment=None, cheapest_dict=True, graph=False, colors_dict=None, category_given=None):
    '''Methods for the clasification of products, using "x" and "y" values:
    - 'Max' use the max values from x and y; Middle is obtained dividing them by 2.
    - 'Stads' use the mean and standar desviation; Middle is the average of values.

    category_given is used when the user wants to force to obtain a value from an specific
    category:
    Price = x, Relevance = y
    1) "Desireable" (Min price, and Max relevance)
    2) "Expensive but requested" (price avobe middle point, but high relevance)
    3) "Couldn't find better" (low relevance, but low price)
    4) "Emergency case" (low relevance and high price)
    5) "Ignored" (would take the cheapest of the ignored data by the x_adjustment)

    x_adjustment is stablished in 0.85 (check notebook) and reduces the values
    of min and max prices considered. Meanwhile, y_adjustment is set in 1 because
    the relevance searching is the max possible.
    
    colors_dict works with the same categories as category_given, with the exception
    of areas_choose.
    '''
    # Here is were it's used all above
    param = params(products_dict, method_x, method_y)
    clasification, cheapest_stock, colors, sizes = categories(products_dict, param, method_y)

    # Colors can change, categories don't
    if colors_dict == None:
        colors_dict = {'Ignored' : 'Black',
                'areas_choose':'LawnGreen',
                    'Desireable': 'Blue',
                    "Expensive but Requested": 'Green',
                    "Couldn't find better": 'Gold',
                    "Emergency Case": 'Crimson'
                    }

    if category_given != None:
        chosen_area = category_given
    else:
        chosen_area = category_loop(cheapest_stock)

    areas_choose_product = cheapest_stock[chosen_area][1]
    # Sometimes the pages return diferent results and the category
    # that works one time, now is completly empty
    if areas_choose_product == None:
        chosen_area = category_loop(cheapest_stock)
        print("Change of area. not it's:", chosen_area)
        areas_choose_product = cheapest_stock[chosen_area][1]
    
    if cheapest_dict == True:
        page_request_dict = {}
        page_request_dict['name'] = products_dict['names'][areas_choose_product]
        page_request_dict['picture'] = products_dict['images'][areas_choose_product]
        page_request_dict['url'] = products_dict['urls'][areas_choose_product]
        page_request_dict['price'] = products_dict['prices'][areas_choose_product]

    #Code for Notebook.
    if graph == True:
        clasification[areas_choose_product] = 'areas_choose'
        colors[areas_choose_product] = colors_dict['areas_choose']
        sizes[areas_choose_product] = 30

        products_dict['price_std_plus'] = param['price_std_plus']
        products_dict['price_mean'] = param['price_mean']
        products_dict['price_std_less'] = param['price_std_less']
        products_dict['hits_std_plus'] = param['hits_std_plus']
        products_dict['hits_mean'] = param['hits_mean']
        products_dict['hits_std_less'] = param['hits_std_less']
        products_dict['colors'] = colors
        products_dict['clasification'] = clasification
        products_dict['sizes'] = sizes
        products_dict['cheapest_stock'] = cheapest_stock

    # This is left for the Notebooks test
    if cheapest_dict == True and graph == False:
        return page_request_dict
    elif graph == True and cheapest_dict == False:
        return products_dict
    elif cheapest_dict == True and graph == True:
        return page_request_dict, products_dict
    else:
        raise AttributeError('None value to give, page_request and graph are "False". Select one')
