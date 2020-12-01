#

import random

'https://www.immobilienscout24.de/Suche/de/berlin//wohnung-mieten?numberofrooms=1.5-&price=-950.0&pricetype=rentpermonth&geocodes=110000000801,110000000201,110000000202,110000000301&sorting=2'

user_search_criteria = {
    "city": "berlin",
    "numberofrooms": "",
    "price_from": "1000",
    "price_to": "",
    "livingspace_form": "",
    "livingspace_to": "100"
}

cities = [
    'berlin',
    'hamburg',
    'stuttgart',
    'munich',
    'frankfurt',
    'duesseldorf',
    'cologne'
        ]

def make_search_url(user_search_criteria):

    #! city must be specified

    user_search_url = 'https://www.immobilienscout24.de/Suche/de/{}/wohnung-mieten?'.format(user_search_criteria['city'])

    if user_search_criteria['numberofrooms']:
        user_search_url += 'numberofrooms=' + user_search_criteria['numberofrooms']
    # Price range set
    if user_search_criteria['price_from'] and user_search_criteria['price_to']:
        print('both there')
        user_search_url += 'price=' + user_search_criteria['price_from'] + '-' + user_search_criteria['price_to']
    # Only from price set
    elif user_search_criteria['price_from']:
        user_search_url += 'price=' + user_search_criteria['price_from'] + '-'
    # Only to price set
    elif user_search_criteria['price_to']:
        user_search_url += 'price=-' + user_search_criteria['price_to']

    # Livingspace range set
    if user_search_criteria['livingspace_form'] and user_search_criteria['livingspace_to']:
        print('both there')
        user_search_url += '&livingspace=' + user_search_criteria['livingspace_form'] + '-' + user_search_criteria['livingspace_to']
    # Only from Livingspace set
    elif user_search_criteria['livingspace_form']:
        user_search_url += '&livingspace=' + user_search_criteria['livingspace_form'] + '-'
    # Only to Livingspace set
    elif user_search_criteria['livingspace_to']:
        user_search_url += '&livingspace=-' + user_search_criteria['livingspace_to']

    user_search_url += '&sorting=2'


    return user_search_url


search_url = make_search_url(user_search_criteria)

print(search_url)