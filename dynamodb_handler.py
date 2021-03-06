#
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('wohnung_sucher_db')



# def get_item(id,key):
#     '''
#     Get item from db. id = ''
#     '''

#     response = table.get_item(
#         Key = {
#             id : key
#         }
#     )
#     return response


def put_item(flat_info):
    '''
    Insert a new item in DB
    '''
    response = table.put_item(
        Item = flat_info
    )
    return response


def scan_db(attribute, search_criteria):
    '''
    Scan database and get results based on attribute and search criteria
    '''
    response = table.scan(
        FilterExpression=Key(attribute).eq(search_criteria)
        #attr = 'source', search_criteria = 'immoscout24'
    )

    return response['Items']
