# coding=utf-8

# Wohnung sucher
# By Danil Konovalov <gesundmeister@gmail.com>!
# Telegram bot to get the newest flat offers from Immobilienscout24.de

import os
import logging
import json
import boto3

from tools import read_config_file
from immoscout24_scrapper import get_new_flats_info
from dynamodb_handler import scan_db, put_item
from telegram_bot_handler import bot_sendtext

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# CONF_FILE = 'config.ini'
# config = read_config_file(CONF_FILE) # read config file

# immo24_search_url = config.get('URLS','SEARCH1')
# immo24_base_url = config.get('URLS','BASEURL')
immo24_search_url = 'https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?numberofrooms=2.0-&price=-1300.0&livingspace=45.0-&sorting=2'
immo24_base_url = 'https://www.immobilienscout24.de/expose/'

bot_token = os.environ['BOTTOKEN'] # get bot token from lambda env var
bot_chat_id = os.environ['CHATID']

def lambda_handler(event,context):

    new_flats_url_list = get_new_flats_info(immo24_search_url, immo24_base_url)
    #print(new_flats_list)

    db_flat_weblinks = [] # Links on already saved flats in db
    db_flats_dict = scan_db('source', 'immoscout24')
    for db_flat in db_flats_dict:
        db_flat_weblinks.append(db_flat['weblink'])

    fresh_deals = list(set(new_flats_url_list) - set(db_flat_weblinks))
    #print(fresh_deals)

    if not fresh_deals:

        print('Nothing new')

    else:

        bot_message = 'There are {} new offers:'.format(len(fresh_deals)) + '\n' + '\n'.join(fresh_deals)
        bot_sendtext(bot_message, bot_token, bot_chat_id)

        for fresh_deal in fresh_deals:
            write_db = put_item(fresh_deal) # update DB
        print(write_db)
