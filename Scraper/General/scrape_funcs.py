
#Web Manage
from bs4 import BeautifulSoup
import requests
import re

#Personal
from .scrape_data import headers

def extract_soup(url, header=0, just_status=False, just_soup=False):
    header = headers.all_saved[header]
    response = requests.get(url, headers=header)
    status = response.status_code

    soup = BeautifulSoup(response.text, 'lxml')

    if just_status==True:
        return status
    elif just_soup==True:
        return soup
    else:
        return soup, status

def search_boxes(soup, box_tuple):
    boxes = soup.find_all(box_tuple[0], attrs={box_tuple[1] : box_tuple[2]})

    return boxes

def get_brute_info(boxes_array, info_tuple):
    '''Returns the brute text from the html depending of the info you asked'''
    info = [None]*len(boxes_array)
    searcher = None
    i=0
    for box in boxes_array:
        searcher = search_boxes(box, info_tuple)
        info[i] = searcher
        searcher = None
        i += 1
    
    return info
