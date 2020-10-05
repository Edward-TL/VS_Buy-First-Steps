#principal functions
from data import Amazon, Ebay, Mercado_Libre, Best_Buy, headers
from scrape_funcs import extract_soup, search_boxes
from page_getters import get_names, get_images, get_products_urls, get_price

# Clasification info
from clasificator import add_clasification_info

# Corpus and Params
from statistics import min_with_none
from corpus import create_corpus_points, hit_points_info

# Basics
import requests
import time
import re


def request_products(user_request, Page, header, home=False, country='mx'):
    page_url = Page.adapt_url(Page, user_request, country)

    # All the HTML of the page
    page_soup, status = extract_soup(page_url, header)
    # Wait until receive the info or been denied
    if status == 503:
        while status == 503:
            time.sleep(1)
            page_soup, status = extract_soup(page_url)
    elif status == 200:
        # HTML divided by products, and stored as elements of an array
        page_boxes = search_boxes(page_soup, Page.boxes)
        page_products = {}

        # Obtain the info of the product
        page_products['names'] = get_names(page_boxes, Page)
        page_products['images'] = get_images(page_boxes, Page)
        page_products['urls'] = get_products_urls(page_boxes, Page)
        page_products['prices'] = get_price(country, page_boxes, Page, home)
        page_products['status'] = status

        return page_products

    else:
        page_products = {}
        # With the empty values, not None, the script knows that this won't be
        # uploaded. In case of one 'None', it thinks that there was a product box
        # without info. Somethings that occurs in Amazon
        page_products['store'] = Page.name
        page_products['idx'] = Page.index
        page_products['product'] = user_request
        page_products['names'] = []
        page_products['images'] = []
        page_products['urls'] = []
        page_products['prices'] = []
        page_products['status'] = status
        
        return page_products

def scrap_product_in_Pages(user_request, test=False, home=False):
    #header to be used
    h = 0
    products_from_pages = []
    url = 'https://vsbuy.xyz/scrap/'
    Pages = [Amazon, Mercado_Libre, Ebay, Best_Buy]
    products_from_pages = []
    for Page in Pages:
        products_from_pages.append(request_products(user_request, Page, header=h, home=home))
        if h < 3:
            h = 0
        else:
            h +=1

    page_names = []
    for page in products_from_pages:
        # The error 503 is considered at the moment of scraping the page. If status
        # turns to be a 400 type, it returns the status and breaks the code for that
        # page
        if page['status'] == 200:
            page_names.append(page['names'])
        else:
            print(f"Error: {page['status']} with {page['status']}")

    if len(page_names) > 0:
        # Creates a dictionary with point values of each word by:
        #  1) Aparition oreder: 1st = highest, last = lowest.
        #  2) Times that shows.
        # Needs to be improve in the tokenizer
        corpus = create_corpus_points(user_request, page_names, header=h)

        for p in range(len(Pages)):
            page_products = products_from_pages[p]
            Page = Pages[p]

            if str(type(page_products['prices'])) == "<class 'list'>":

                # Using the corpus info
                page_products['hit points'] = hit_points_info(user_request, page_products, corpus)

                # This makes more sense with the Jupyer/Colab Notebook
                recomended_product = add_clasification_info(page_products)
                if test == True:
                    print('Info of the cheapest product recomended')
                
                # Info that completes the DB requirements
                # Is added here because this is the last filter of knowing if
                # the page give something to add or not.
                recomended_product['store'] = Page.index
                recomended_product['product'] = user_request

                if test == True:
                    for key, value in recomended_product.items():
                        print(key, ':', value)


                # Posting data in Server
                r = requests.post(url=url, json=recomended_product)
                
                # In case de server returnsan error and needs to try de uploading again:
                request_answer = str(r.text)
                if  re.match(u"<code>DEBUG" , request_answer) is not None:
                    t=1
                    while re.match(u"<code> DEBUG" ,r.text) is not None and t < 10:
                        print('Server Error. Trying again...')
                        r = requests.post(url=url, json=recomended_product)
                        time.sleep(1)
                        t += 1
                else:
                    print(f'Succes uploading! {user_request}')
                    print('\n')

if __name__ == '__main__':
    user_request = input('Enter the product that you want to scrap: ')
    print('\n')
    scrap_product_in_Pages(user_request, test=False, home=False)
