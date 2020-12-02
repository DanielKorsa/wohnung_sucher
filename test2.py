

# flat_info = {'Area': '50 m²',
#  'address': 'Johann-Clanze-Straße 29, 81369 München, Mittersendling',
#  'description': 'Vollständig renovierte, möblierte 2-Zimmer-Wohnung mit Balkon '
#                 'und EBK in Sendling-Westpark',
#  'email': '',
#  'movinDate': '15.10.2020',
#  'petsAllowed': '',
#  'phone': '',
#  'price': '1.200 €',
#  'rooms': '2',
#  'source': 'immoscout24',
#  'weblink': 'https://www.immobilienscout24.de/expose/114676849'}





# from immoscout24_scrapper import get_flat_full_details
# import pprint

# # url = 'https://www.immobilienscout24.de/expose/122863597#/'

# # full_info = get_flat_full_details(url)
# # img_link_dirty = full_info['imageLink']

# # pprint.pprint(img_link_dirty)

# img_weblink = 'https://pictures.immobilienscout24.de/listings/622c9c55-231f-4483-861b-1f1fca5517a5-1398300448.png/ORIG/legacy_thumbnail/1024x768/format/jpg/quality/80'

# weblink = 'https://www.immobilienscout24.de/expose/114676849'


from random import randrange, random
import time
immo24_search_url = 'https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?numberofrooms=1.5-&price=10-950.0&pricetype=rentpermonth&geocodes=110000000801,110000000201,110000000202,110000000301&sorting=2'


immo24_search_url = immo24_search_url.replace('price=10', 'price=' + str(randrange(0, 13)))
immo24_search_url = immo24_search_url.replace('-950', '-' + str(randrange(950, 962)))
if randrange(1,5) > 3:
    immo24_search_url += '&enteredFrom=result_list'

print(immo24_search_url.split('1.5')[1])