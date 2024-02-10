import requests


headers = {
    'user-agent': 'Michael'
}
with open('api key.txt' 'r') as key:
    key = key


r = request.get('https://my-api-url', headers=headers)


