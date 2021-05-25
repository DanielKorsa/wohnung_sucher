
#  Install the Python Requests library:
# `pip install requests`
import requests
import pprint

def send_request():
    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/",
        params={
            "api_key": "R66OK3QOYRTRR40UP1A1XHZRTEJQE3TG8ECW9LQHTGEBVBZQC3ZKW3216466LNZ2PWDNHV940HVIMPYA",
            "url": "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?numberofrooms=3.0-&enteredFrom=one_step_search", 
            "premium_proxy": "true", 
            "country_code":"de"
        },
        
    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
    pprint.pprint(response)



send_request()