# coding=utf-8

# Wohnung sucher
# By Danil Konovalov <gesundmeister@gmail.com>!
# Immoscout Crawler & Telegram bot to get the newest flat offers from Immobilienscout24.de

from random import randrange, random
import time
import os
import time
import logging
import pprint
import json
import boto3

from tools import read_config_file, download_img, upload_file_s3
from immoscout24_scrapper import get_new_flats_info, get_flat_full_details
from dynamodb_handler import scan_db, put_item
from telegram_bot_handler import bot_sendtext

logger = logging.getLogger()
logger.setLevel(logging.INFO)
#! Add referral
CONF_FILE = 'config.ini'
config = read_config_file(CONF_FILE) # read config file
#immo24_search_url = config.get('URLS','SEARCH1') #! Instead search link is in env variable
immo24_base_url = config.get('URLS','BASEURL')
#immo24_search_url = os.environ['SEARCHLINK']

bot_token = os.environ['BOTTOKEN'] # get bot token from lambda env var
bot_chat_id = os.environ['CHATID'] #! For personal use
bot_chat_id2 = os.environ['CHATID2']

def lambda_handler(event,context):

    start_time = time.time()
    time.sleep(random()) # little random delay
    immo24_search_url = os.environ['SEARCHLINK']
    immo24_search_url = immo24_search_url.replace('price=10', 'price=' + str(randrange(0, 15)))
    immo24_search_url = immo24_search_url.replace('-950', '-' + str(randrange(950, 962)))
    if randrange(1,5) > 3:
        immo24_search_url += '&enteredFrom=result_list'
    print(immo24_search_url)
    new_flats_url_list, blocked, header = get_new_flats_info(immo24_search_url, immo24_base_url)
    if blocked:
        bot_message = immo24_search_url#.split('price=')[1]
        bot_sendtext(bot_message, bot_token, bot_chat_id)
        bot_sendtext(str(header), bot_token, bot_chat_id)
    # temp_json_debug_path = '/tmp/' + 'json_log' + '.json'
    # with open(temp_json_debug_path, 'w', encoding='utf-8') as f:
    #     json.dump(json_debug, f, ensure_ascii=False, indent=4)
    # file_uploaded = upload_file_s3(temp_json_debug_path, 'wohnungsuchers3', 'log.json')
    # print(file_uploaded)
    pprint.pprint(new_flats_url_list)
    if not new_flats_url_list:
        logger.info('Couldnt scrape the listing page with results')

    # Links on already saved flats in db
    db_flats_dict = scan_db('source', 'immoscout24')
    db_flat_weblinks = [db_flat['weblink'] for db_flat in db_flats_dict[]]
    fresh_deals_urls = list(set(new_flats_url_list) - set(db_flat_weblinks))
    print('Fresh deals')
    print(fresh_deals_urls)

    if not fresh_deals_urls:
        bot_message = 'Nothing new'
        #bot_sendtext(bot_message, bot_token, bot_chat_id) #! DELETE
    else:
        for fresh_deal_url in fresh_deals_urls:
            flat_info = get_flat_full_details(fresh_deal_url)
            put_item(flat_info) # update DB
            bot_message = ' <b>Description:</b>{} \n <b>Address</b>:{} \n <b>Price</b>:{} \n <b>Area</b>:{} \n \
            <b>Move in date</b>:{} \n {}'.format(flat_info['description'], flat_info['address'], flat_info['price'], flat_info['Area'], flat_info['movinDate'],flat_info['weblink'])
            bot_sendtext(bot_message, bot_token, bot_chat_id2) # send msg to group

            #! Save img to S3
            if flat_info['imageLink'] != '':
                img_name = make_img_name(flat_info['weblink'])
                temp_img_path = '/tmp/' + img_name + '.jpg'
                download_img(flat_info['imageLink'], temp_img_path)
                file_uploaded = upload_file_s3(temp_img_path, 'wohnungsuchers3', 'wohnungSucherImages/' + img_name + '.jpg')
                print(file_uploaded)

            else:
                print('no picture was uploaded')

        #! TESTING
        # flat_info = get_flat_full_details(fresh_deals_urls[0])
        # put_item(flat_info) # update DB
        # bot_message = ' <b>Description:</b>{} \n <b>Address</b>:{} \n <b>Price</b>:{} \n <b>Area</b>:{} \n \
        # <b>Move in date</b>:{} \n {}'.format(flat_info['description'], flat_info['address'], flat_info['price'], flat_info['Area'], flat_info['movinDate'],flat_info['weblink'])
        # bot_sendtext(bot_message, bot_token, bot_chat_id2) # send msg to group


    print('Execution time is {}'.format(time.time() - start_time))
    return {
        'message' : bot_message
    }

