# coding=utf-8

# Wohnung sucher
# By Danil Konovalov <gesundmeister@gmail.com>!
# Telegram bot to get the newest flat offers from Immobilienscout24.de

import os
import time
import logging
import json
import boto3

from tools import read_config_file, make_img_name, download_img, upload_file_s3
from immoscout24_scrapper import get_new_flats_info, get_flat_full_details
from dynamodb_handler import scan_db, put_item
from telegram_bot_handler import bot_sendtext

logger = logging.getLogger()
logger.setLevel(logging.INFO)

CONF_FILE = 'config.ini'
config = read_config_file(CONF_FILE) # read config file

immo24_search_url = config.get('URLS','SEARCH1')
immo24_base_url = config.get('URLS','BASEURL')

bot_token = os.environ['BOTTOKEN'] # get bot token from lambda env var
#bot_chat_id = os.environ['CHATID'] #! For personal use 
bot_chat_id2 = os.environ['CHATID2']

def lambda_handler(event,context):

    start_time = time.time()
    new_flats_url_list = get_new_flats_info(immo24_search_url, immo24_base_url)
    #print(new_flats_url_list)

    db_flat_weblinks = [] # Links on already saved flats in db
    db_flats_dict = scan_db('source', 'immoscout24')
    for db_flat in db_flats_dict:
        db_flat_weblinks.append(db_flat['weblink'])

    fresh_deals_urls = list(set(new_flats_url_list) - set(db_flat_weblinks))
    #print(db_flat_weblinks)

    if not fresh_deals_urls:

        bot_message = 'Nothing new'

    else:

        #bot_message = '{} new offers:'.format(len(fresh_deals_urls)) + '\n' + '\n'.join(fresh_deals_urls)
        #bot_sendtext(bot_message, bot_token, bot_chat_id)
        #bot_sendtext(bot_message, bot_token, bot_chat_id2) # send msg to group

        for fresh_deal_url in fresh_deals_urls:
            flat_info = get_flat_full_details(fresh_deal_url)
            put_item(flat_info) # update DB
            bot_message = ' <b>Description:</b>{} \n <b>Address</b>:{} \n <b>Price</b>:{} \n <b>Area</b>:{} \n \
            <b>Move in date</b>:{} \n {}'.format(flat_info['description'], flat_info['address'], flat_info['price'], flat_info['Area'], flat_info['movinDate'],flat_info['weblink'])
            bot_sendtext(bot_message, bot_token, bot_chat_id2) # send msg to group

            # #! Save img to S3
            # if flat_info['imageLink'] != '':
            #     img_name = make_img_name(flat_info['weblink'])
            #     temp_img_path = '/tmp/' + img_name + '.jpg'
            #     download_img(flat_info['imageLink'], temp_img_path)
            #     file_uploaded = upload_file_s3(temp_img_path, 'wohnungsuchers3', 'wohnungSucherImages/' + img_name + '.jpg')
            #     print(file_uploaded)

            # else:
            #     print('no picture was uploaded')

    print('Execution time is {}'.format(time.time() - start_time))
    return {
        'message' : bot_message
    }

