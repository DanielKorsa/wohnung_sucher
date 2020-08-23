#

import random
import configparser

def get_header():
    '''
    Get headers
    '''
    USER_AGENTS = [
        # Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        # Edge
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
        # Firefox
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        # Safari
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
    ]

    HEADERS = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': f'{random.choice(USER_AGENTS)}',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                    'application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    return HEADERS


def read_config_file(conf_filename):
    '''
    Read local file `config.ini`
    '''
    config = configparser.ConfigParser()                                     
    config.read(conf_filename)
    
    return config




# def get_old_flats():
#     old_flats = ['https://www.immobilienscout24.de/expose/122104655', 
#     'https://www.immobilienscout24.de/expose/122103422', 
#     'https://www.immobilienscout24.de/expose/122100453', 
#     'https://www.immobilienscout24.de/expose/122100254', 
#     'https://www.immobilienscout24.de/expose/83329790', 
#     'https://www.immobilienscout24.de/expose/122015149', 
#     'https://www.immobilienscout24.de/expose/122042075', 
#     'https://www.immobilienscout24.de/expose/122076460', 
#     'https://www.immobilienscout24.de/expose/122075160', 
#     'https://www.immobilienscout24.de/expose/122075009', 
#     'https://www.immobilienscout24.de/expose/122074277', 
#     'https://www.immobilienscout24.de/expose/122069734', 
#     'https://www.immobilienscout24.de/expose/122070608', 
#     'https://www.immobilienscout24.de/expose/121610143', 
#     'https://www.immobilienscout24.de/expose/122062917', 
#     'https://www.immobilienscout24.de/expose/122055487', 
#     'https://www.immobilienscout24.de/expose/122055072', 
#     'https://www.immobilienscout24.de/expose/122053450', 
#     'https://www.immobilienscout24.de/expose/121728396']

#     return old_flats
