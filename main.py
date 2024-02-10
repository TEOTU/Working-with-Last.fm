import requests
import json
import requests_cache
import time
from IPython.core.display import clear_output
import pandas as pd


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


requests_cache.install_cache()
responses = []
page = 1
total_pages = 116461

while page <= total_pages:
    payload = {
        'method': 'chart.gettopartists',
        'limit': 1000,
        'page': page
    }

    # print some output so we can see the status
    print("Requesting page {}/{}".format(page, total_pages))
    # clear the output to make things neater
    clear_output(wait=True)

    # make the API call
    response = lastfm_get(payload)

    # if we get an error, print the response and halt the loop
    if response.status_code != 200:
        print(response.text)
        break
    try:
        # try to parse JSON
        data = response.json()

        # extract pagination info
        page = int(data['artists']['@attr']['page'])
        total_pages = int(data['artists']['@attr']['totalPages'])

        # append response
        responses.append(response)

        # if it's not a cached result, sleep
        if not getattr(response, 'from_cache', False):
            time.sleep(0.25)

    except json.JSONDecodeError:
        # if the response is not in JSON format, print an error message
        print("Invalid JSON in response.")
        page += 1

    page += 1


if __name__ == '__main__':
    frames = [pd.DataFrame(r.json()['artists']['artist']) for r in responses]  # breaking to dataframes
    artists = pd.concat(frames)  # turning into a single dataframe
    artists = artists.drop('image', axis=1)  # dropping the images urls

