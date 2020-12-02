#

from tools import get_header
from datetime import datetime
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
    #pprint.pprint(headers)
    response = requests.get(url, headers = headers)
    pprint.pprint(response)
    content = BeautifulSoup(response.text, 'html5lib')

    return content, headers

def get_new_flats_info(immo24_search_url, immo24_base_url):
    '''
    Get list of new flats
    '''
    immo24_content, header = get_page_content(immo24_search_url)
    warning = 'To regain access, please make sure that cookies and JavaScript are enabled before reloading the page'
    if warning in immo24_content.text:
        print('----------------------BLOCKED')
        blocked = True
        new_flats_url_list = []
    else:
        flats = immo24_content.find_all(class_='result-list__listing') # get all flats on 1st page
        new_flats_url_list = []
        for flat in flats:
            flat_id = flat.find(attrs={"data-id": True})['data-id'] # get flat ID
            flat_url = immo24_base_url + flat_id # make flat url
            new_flats_url_list.append(flat_url)
        blocked = False

    return new_flats_url_list, blocked, header

def get_flat_full_details(immo_flat_url):

    flat_content, header = get_page_content(immo_flat_url)
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
    try:
        flat_full_info['address'] = flat_content.find(class_= 'address-block').text.strip()
    except AttributeError:
        flat_full_info ['address'] = ''
    try:
        flat_full_info['price'] = flat_content.find(class_= 'is24qa-kaltmiete-main is24-value font-semibold is24-preis-value').text.strip()
    except AttributeError:
        flat_full_info['price'] = ''
    #flat_full_info['price'] = flat_content.find(class_= 'is24qa-kaltmiete is24-value font-semibold is24-preis-value').text.strip()
    try:
        flat_full_info['rooms'] = flat_content.find(class_= 'is24qa-zi-main is24-value font-semibold').text.strip()
    except AttributeError:
        flat_full_info['rooms'] = ''
    try:
        flat_full_info['Area'] = flat_content.find(class_= 'is24qa-flaeche-main is24-value font-semibold').text.strip()
    except AttributeError:
        flat_full_info['Area'] = ''

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
                break
            else:
                flat_full_info['onlineSince'] = 'no data'
    except Exception as e:
        print(e)
        flat_full_info['onlineSince'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    #Adding a pic to it
    try:
        flat_full_info['imageLink'] = flat_content.find(class_= 'first-gallery-picture-container').find('img').get('src')
        #print(type(flat_full_info['imageLink']))

    except:
        print('no picture provided')
        flat_full_info['imageLink'] = ''


    return flat_full_info
