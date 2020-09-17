#

from tools import get_header
import re
import pprint
import requests
from bs4 import BeautifulSoup

#proxies = {'https': '51.75.160.176:9999'} proxies = proxies


def get_page_content(url):
    '''
    Get page content
    '''
    headers = get_header()
    content = BeautifulSoup(requests.get(url, headers = headers).text, 'html5lib')

    return content

def get_new_flats_info(immo24_search_url, immo24_base_url):
    '''
    Get list of new flats
    '''
    immo24_content = get_page_content(immo24_search_url)
    flats = immo24_content.find_all(class_='result-list__listing') # get all flats on 1st page

    new_flats_url_list = []
    for flat in flats:
        flat_id = flat.find(attrs={"data-id": True})['data-id'] # get flat ID
        flat_url = immo24_base_url + flat_id # make flat url
        new_flats_url_list.append(flat_url)
        #print(flat_url)

    return new_flats_url_list

def get_flat_full_details(immo_flat_url):

    flat_content = get_page_content(immo_flat_url)
    #pprint.pprint(flat_content)
    flat_full_info = {}
    flat_full_info['weblink'] = immo_flat_url
    print(immo_flat_url)
    flat_full_info['source'] = 'immoscout24'
    flat_full_info['phone'] = '' # not scraping
    flat_full_info['email'] = '' # not scraping
    try:
        flat_full_info['description'] = flat_content.find(class_= 'criteriagroup').h1.text.strip()
    except AttributeError:
        flat_full_info ['description'] = ''
        print('AttributeError - no descripttion')
    # This parameters are required:
    flat_full_info['address'] = flat_content.find(class_= 'address-block').text.strip()
    flat_full_info['price'] = flat_content.find(class_= 'is24qa-kaltmiete is24-value font-semibold is24-preis-value').text.strip()
    flat_full_info['rooms'] = flat_content.find(class_= 'is24qa-zi is24-value font-semibold').text.strip()
    flat_full_info['Area'] = flat_content.find(class_= 'is24qa-flaeche is24-value font-semibold').text.strip()

    try:
        flat_full_info['movinDate'] = flat_content.find(class_= 'is24qa-bezugsfrei-ab grid-item three-fifths').text.strip()
    except AttributeError:
        flat_full_info['movinDate'] = ''
        print('AttributeError - no move in date')

    #flat_full_info['onlineSince'] = 'no data' #! IF IT GOES WRONG AGAIN!
    try:
        flat_full_info['petsAllowed'] = flat_content.find(class_= 'is24qa-haustiere grid-item three-fifths').text.strip()
    except AttributeError:
        flat_full_info['petsAllowed'] = ''
        print('AttributeError - no pets info')

    try:
        online_since = flat_content.find(class_= 'criteriagroup flex flex--wrap criteria-group--spacing padding-top-s').find('script').text.strip()
        for online in online_since.splitlines():
            if "exposeOnlineSince" in online:
                online_date = re.findall(r'"([^"]*)"', online)
                flat_full_info['onlineSince'] = ''.join(online_date).split('.')[0].strip()
            else:
                flat_full_info['onlineSince'] = 'no data'
    except Exception as e:
        print(e)
        flat_full_info['onlineSince'] = 'no data'
        #! Adding a pic to it
        # # try:
        #     flat_full_info['imageLink'] = flat_content.find(class_= 'first-gallery-picture-container')
        # except:
        #     print('no picture provided')
        #     flat_full_info['imageLink'] = ''
        #print('cunt online since{}'.format(online_since))

    return flat_full_info
