#

from tools import get_header
import requests
from bs4 import BeautifulSoup



def get_page_content(url):
    '''
    Get page content
    '''
    headers = get_header()
    content = BeautifulSoup(requests.get(url,headers = headers).text, 'html5lib')

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




# exposeOnlineSince: "2020-07-31T11:01:50.000+02:00"