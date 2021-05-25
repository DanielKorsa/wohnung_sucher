# Telegram bot for sending messages with new flat ads

import requests

def bot_sendtext(bot_message, bot_token, bot_chat_id):
    """[Push txt msg from Telegram Bot]

    Args:
        bot_message ([str]): [Message]
        bot_token ([str]): [Telegram Token]
        bot_chat_id ([str]): [Chat ID]

    Returns:
        [dict]: [Response Json]
    """
    # bot_token = ''
    # bot_chat_id = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=HTML&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def bot_sendpic(pic_path, bot_token, bot_chat_id):
    """[Push a picture to Telegram chat]

    Args:
        pic_path ([str]): [Path to pic (on S3)]
        bot_token ([str]): [Telegram Token]
        bot_chat_id ([str]): [Chat ID]

    Returns:
        [type]: [description]
    """
    url = 'https://api.telegram.org/bot' + bot_token + '/sendPhoto'
    files = {'photo': open(pic_path, 'rb')}
    data = {'chat_id' : bot_chat_id}
    r = requests.post(url, files=files, data=data)

    return (r.status_code, r.reason, r.content)



# def bot_send_inline_img(pic_path, bot_message, bot_token, bot_chat_id):
    
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=HTML&text=' + bot_message

    
#     <a href="' + image + '">&#8205;</a>
#     response = requests.get(send_text)

#     return response.json()
    