

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



bot_message = ' Description:{} \n Address:{} \n Price:{} \n Area:{} \n \
Move in date:{}'.format(flat_info['description'], flat_info['address'], flat_info['price'], flat_info['Area'], flat_info['movinDate'])

print(bot_message)