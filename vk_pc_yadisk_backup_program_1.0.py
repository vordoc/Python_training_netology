import requests
import os
import json
import time
import configparser
import posixpath
from datetime import datetime
from tqdm import tqdm
from yadisk import yadisk
from pprint import pprint


def get_photos_method(user_id):
    params = {'access_token': vk_token,
              'v': api_version,
              'album_id': 'profile',
              'owner_id': user_id,
              'extended': '1',
              'photo_sizes': '1'
              }
    response = requests.get(get_photos_method_url, params=params)
    profile_list = response.json()
    # pprint(profile_list)

    for file in tqdm(profile_list['response']['items']):
        time.sleep(1)
        # size = file['sizes'][-1]['type']
        photo_url = file['sizes'][-1]['url']
        date = datetime.utcfromtimestamp(file['date']).strftime('%d.%m.%Y %H_%M_%S')
        file_name = str(file['likes']['count']) + '__' + str(date)
        download_photo = requests.get(photo_url)
        with open(f'{pc_download_file_path}/{file_name}.jpg', 'wb') as f:
            f.write(download_photo.content)


def recursive_upload(y, from_dir, to_dir):
    for root, dirs, files in os.walk(from_dir):
        time.sleep(1)
        p = root.split(from_dir)[1].strip(os.path.sep)
        dir_path = posixpath.join(to_dir, p)
        # y.mkdir(dir_path)
        for file in tqdm(files):
            time.sleep(1)
            file_path = posixpath.join(dir_path, file)
            p_sys = p.replace("/", os.path.sep)
            in_path = os.path.join(from_dir, p_sys, file)
            y.upload(in_path, file_path, overwrite=True)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")

    vk_user_id = 552934290
    vk_token = config['vk_api']['access_token']
    api_version = config['vk_api']['api_version']
    get_photos_method_url = config['vk_api']['get_photos_method_url']
    pc_download_file_path = config['files_path']['download_file_path']
    get_upload_url_api = config['yadisk_api']['get_upload_url_api']
    yadisk_file_path = config['yadisk_api']['yadisk_file_path']
    yadisk_token = config['yadisk_api']['api_token']
    # mkdir_url = config['yadisk_api']['mkdir_url']

    get_photos_method(vk_user_id)

    y = yadisk.YaDisk(token=yadisk_token)
    # print(y.check_token())
    to_dir = yadisk_file_path
    from_dir = pc_download_file_path

    recursive_upload(y, from_dir, to_dir)
