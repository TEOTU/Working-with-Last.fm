import requests

USER_AGENT = 'Michael'
with open('api key.txt', 'r') as file:
    KEY = file.read()

headers = {
    'user-agent': USER_AGENT
}
payload = {
    'api_key': KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}

r = requests.get('https://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
print(r.status_code)


