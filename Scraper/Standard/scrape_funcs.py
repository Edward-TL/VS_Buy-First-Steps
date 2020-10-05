# Web Manage
from bs4 import BeautifulSoup
import requests
import re

# Personal
from data import headers

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


# Search the kind of box specified by the touple
# Cents is a bug in some pages that returns the cents in another box.
# don't worry, if you fill all, this won't stop you
def search_boxes(soup, box_tuple, cents=False):
    if cents == True:
        boxes = soup.find(box_tuple[0], attrs={box_tuple[1] : box_tuple[2]})
    else:
        boxes = soup.find_all(box_tuple[0], attrs={box_tuple[1] : box_tuple[2]})

    return boxes

# Returns the brute text from the html depending of the info you asked
def get_brute_info(boxes_array, info_tuple):
    info = [None]*len(boxes_array)
    searcher = None
    i=0
    for box in boxes_array:
        searcher = search_boxes(box, info_tuple)
        info[i] = searcher
        searcher = None
        i += 1
    
    return info
