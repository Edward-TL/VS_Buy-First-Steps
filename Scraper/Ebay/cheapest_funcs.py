
from page_getters import get_names, get_images, get_products_urls, get_price

def ordered_dict(dictionary, reverse=True):
    import operator
    ordered_dict = dict(sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))

    return ordered_dict

def cheapest(array_prices, just_position=True, just_price=False, position_and_price=False, test=False):
    cheapest_position = 0
    cheapest_price = None
    
    for n in range(len(array_prices)):
        price = array_prices[n]
        if price:
            if cheapest_price == None:
                cheapest_price = price
            if test == True:
                print(f'number = {n} cheapest_price is {cheapest_price} and price check is {price}')

            if price < cheapest_price:
                if test == True:
                    print(f'price: {price} < {cheapest_price}')

                cheapest_price = price
                cheapest_position = n
        
    if position_and_price == True:
        just_position = False
        return cheapest_position, cheapest_price
    elif just_position == True:
        return cheapest_position
    elif just_price == True:
        return cheapest_price


def get_cheapest(cheapest_idx, products, cheapest_price=None, country=None, Page=None):
    products_type = str(type(products))
    if products_type == "<class 'bs4.element.ResultSet'>":
        if country and Page:
            cheapest_dict = {}
            cheapest_dict['name'] = get_names(products, Page.name_and_images, position=cheapest_idx)
            cheapest_dict['image'] = get_images(products, Page.name_and_images, position=cheapest_idx)
            cheapest_dict['url'] = get_products_urls(products, Page.product_urls, position=cheapest_idx)
            cheapest_dict['price'] = cheapest_price
        else:
            if not country:
                raise ValueError("Missing country value")
            elif not Page:
                raise ValueError("Missing Page object")
            elif not cheapest_price:
                raise ValueError("Missing cheapest_price value (int)")
            else:
                raise ValueError(f'''Missing Page and country values.
            You can use this function with a dictionary with all the data preloaded as well''')
    elif products_type == "<class 'dict'>":
        cheapest_dict = {}
        products_dictionary = products
        for key in products_dictionary:
            cheapest_dict[key] = products_dictionary[key][cheapest_idx]
    else:
        error_in_product_type =  f"Products type must be a dict or a bs4.element.ResultSet with the boxes. Recived {type(products)}"
        raise ValueError(error_in_product_type)
    
    return cheapest_dict