import requests
from datetime import datetime
from pprint import pprint
from config_vk_korovin import token

def get_vk_photos():
    version = 5.131
    owner_id = 552934290
    params = {
        'access_token': token,
        'v': version,
        'owner_id': owner_id,
        'album_id': 'profile',
        'extended': '1'
    }
    response = requests.get('https://api.vk.com/method/photos.get', params=params)
    photos = {}
    if response.status_code == 200:
        result = response.json()
        # pprint(result)
        for items in result['response']['items']:
            pprint(items)
            name = items['likes']['count']
            url = items['sizes'][-1]['url']
            date = datetime.utcfromtimestamp(items['date']).strftime('%d_%m_%Y__%H_%M_%S')
            photos[str(name) + '__' + date] = url

    return photos

pprint (get_vk_photos())
