

flat_info = {'Area': '50 m²',
 'address': 'Johann-Clanze-Straße 29, 81369 München, Mittersendling',
 'description': 'Vollständig renovierte, möblierte 2-Zimmer-Wohnung mit Balkon '
                'und EBK in Sendling-Westpark',
 'email': '',
 'movinDate': '15.10.2020',
 'petsAllowed': '',
 'phone': '',
 'price': '1.200 €',
 'rooms': '2',
 'source': 'immoscout24',
 'weblink': 'https://www.immobilienscout24.de/expose/114676849'}





from immoscout24_scrapper import get_flat_full_details
import pprint

# url = 'https://www.immobilienscout24.de/expose/122863597#/'

# full_info = get_flat_full_details(url)
# img_link_dirty = full_info['imageLink']

# pprint.pprint(img_link_dirty)

img_weblink = 'https://pictures.immobilienscout24.de/listings/622c9c55-231f-4483-861b-1f1fca5517a5-1398300448.png/ORIG/legacy_thumbnail/1024x768/format/jpg/quality/80'

weblink = 'https://www.immobilienscout24.de/expose/114676849'



