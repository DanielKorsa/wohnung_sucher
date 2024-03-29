# Utils & Tools

import random
import configparser
import requests
import logging

import boto3
from botocore.exceptions import ClientError


def get_header():
    '''
    Get headers
    '''
    USER_AGENTS = [

        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.0; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Mozilla/5.0 (X11; Linux i686; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.400',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.400',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 Edg/87.0.664.52'
                ]


    HEADERS = [
        # {
        # 'Connection': 'keep-alive',
        # 'Pragma': 'no-cache',
        # 'Cache-Control': 'no-cache',
        # 'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': f'{random.choice(USER_AGENTS)}',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
        #             'application/signed-exchange;v=b3;q=0.9',
        # 'Sec-Fetch-Site': 'none',
        # 'Sec-Fetch-Mode': 'navigate',
        # 'Sec-Fetch-User': '?1',
        # 'Sec-Fetch-Dest': 'document',
        # 'Accept-Language': 'en-US,en;q=0.9',
        # },
        {
        'Connection': 'keep-alive',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-store',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': f'{random.choice(USER_AGENTS)}',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                    'application/signed-exchange;v=b3;q=0.9',
        },
        {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cache-Control': 'no-store',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': f'{random.choice(USER_AGENTS)}',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        },
        {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'User-Agent': f'{random.choice(USER_AGENTS)}',
        },
        {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Referer' : 'https://www.google.de',
        'User-Agent': f'{random.choice(USER_AGENTS)}',
        },
        {
        'User-Agent': f'{random.choice(USER_AGENTS)}'
        }
]

    return HEADERS[4]#random.choice(HEADERS)

#! Copied from https://curl.trillworks.com/
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.immobilienscout24.de/',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Sec-GPC': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}

params = (
    ('enteredFrom', 'one_step_search'),
)

def read_config_file(conf_filename):
    '''
    Read local file `config.ini`
    '''
    config = configparser.ConfigParser()
    config.read(conf_filename)

    return config


def download_img(img_url, img_new_path):
    '''
    Download img from url
    '''
    img_data = requests.get(img_url).content
    with open(img_new_path, 'wb') as handler:
        handler.write(img_data)

    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
def upload_file_s3(file_name, bucket, object_name=None):
    """[Upload a file to an S3 bucket]

    Args:
        file_name ([str]): [File to upload]
        bucket ([str]): [Bucket to upload to]
        object_name ([str], optional): [S3 object name. If not specified then file_name is used]. Defaults to None.

    Returns:
        [bool]: [True if uploaded]
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True
