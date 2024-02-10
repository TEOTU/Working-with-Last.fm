import requests

USER_AGENT = 'Michael'
with open('api key.txt', 'r') as file:
    KEY = file.read()


def lastfm_get(payload):

    headers = {'user-agent': USER_AGENT}
    url = 'https://ws.audioscrobbler.com/2.0/'
    payload['api_key'] = KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response


print(lastfm_get({'method': 'chart.gettopartists'}).status_code)


