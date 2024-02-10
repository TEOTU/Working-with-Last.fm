import requests
import json

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


def jprint(obj):
    # formatting the json object
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


response = lastfm_get({'method': 'chart.gettopartists'})
print(jprint(response.json()['artists']['@attr']))
