import requests
from pprint import pprint
from config_vk_korovin import token


version = 5.131
owner_id = 552934290

params = {
    'access_token': token,
    'v': version,
    'owner_id': owner_id,
    'album_id': 'profile',
    'extended': '1'
}

resp = requests.get('https://api.vk.com/method/photos.get', params=params)

data = resp.json()

pprint(data)

