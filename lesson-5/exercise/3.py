import requests
from pprint import pprint
url = 'https://api.github.com/search/repositories'
param = {'q':'requests+lenguage:python'}
response  =requests.get(url,params=param)
response_json = response.json()
items = response_json['items']
for item in items:
    pprint(item['name']) #json formatted
    pprint(item['description'])