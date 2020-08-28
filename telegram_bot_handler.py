# Telegram bot for sending messages with new flat ads

import requests

def bot_sendtext(bot_message, bot_token, bot_chat_id):
    
    # bot_token = ''
    # bot_chat_id = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()
    

# test = bot_sendtext("Testing Telegram bot")
# print(test)

#/bot_sucher189004455DasdiFHAi



