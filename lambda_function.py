# coding=utf-8

# Wohnung sucher
# By Danil Konovalov <gesundmeister@gmail.com>!
# Telegram bot to get the newest flat offers from Immobilienscout24.de

import os
import time
import logging
import json
import boto3

from tools import read_config_file
from immoscout24_scrapper import get_new_flats_info
from dynamodb_handler import scan_db, put_item
from telegram_bot_handler import bot_sendtext

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CONF_FILE = 'config.ini'
config = read_config_file(CONF_FILE) # read config file

immo24_search_url = config.get('URLS','SEARCH1')
immo24_base_url = config.get('URLS','BASEURL')

bot_token = os.environ['BOTTOKEN'] # get bot token from lambda env var
bot_chat_id = os.environ['CHATID']
bot_chat_id2 = os.environ['CHATID2']

def lambda_handler(event,context):

    start_time = time.time()
    new_flats_url_list = get_new_flats_info(immo24_search_url, immo24_base_url)
    #print(new_flats_url_list)

    db_flat_weblinks = [] # Links on already saved flats in db
    db_flats_dict = scan_db('source', 'immoscout24')
    for db_flat in db_flats_dict:
        db_flat_weblinks.append(db_flat['weblink'])

    fresh_deals = list(set(new_flats_url_list) - set(db_flat_weblinks))
    print(db_flat_weblinks)

    if not fresh_deals:

        bot_message = 'Nothing new'

    else:

        bot_message = '{} new offers:'.format(len(fresh_deals)) + '\n' + '\n'.join(fresh_deals)
        bot_sendtext(bot_message, bot_token, bot_chat_id)
        bot_sendtext(bot_message, bot_token, bot_chat_id2) # send 2nd Telegram msg

        for fresh_deal in fresh_deals:
            write_db = put_item(fresh_deal) # update DB
        

    print('Execution time is {}'.format(time.time() - start_time))
    return {
        'message' : bot_message
    }
