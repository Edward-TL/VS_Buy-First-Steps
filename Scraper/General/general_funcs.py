def ordered_dict(dictionary, reverse=True):
    import operator
    ordered_dict = dict(sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))

    return ordered_dict

def cheapest(array_prices, just_position=True, just_price=False, test=False):
    cheapest_position = 0
    cheapest_price = array_prices[0]

    for n in range(len(array_prices)):
        price = array_prices[n]
        if test == True:
            print(f'number = {n} cheapest_price is {cheapest_price} and price check is {price}')

        if price < cheapest_price:
            if test == True:
                print(f'price: {price} < {cheapest_price}')

            cheapest_price = price
            cheapest_position = n
        
    if just_position == True:
        return cheapest_position
    elif just_price == True:
        return cheapest_price
    else:
        return cheapest_position, cheapest_price

def get_cheapest(cheapest, products):
    if type(products) == list:
        pass
    elif type(products) == dict:
        cheapest_dict = {}
        products_dictionary = products
        for key in products_dictionary:
            cheapest_dict[key] = products_dictionary[key][cheapest]
    else:
        return "Products type must be a dict or a list with the boxes"
    
    return cheapest_dict
    
def get_info(func):
    info = None
    def wrapper(*args, **kwargs):
        return wrapper
    return info