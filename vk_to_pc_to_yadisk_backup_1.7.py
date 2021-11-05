import requests
import os
import json
import time
import configparser
import posixpath
from datetime import datetime
from tqdm import tqdm
from yadisk import yadisk


def get_profile_list(user_id):
    params = {'access_token': vk_token,
              'v': api_version,
              'album_id': 'profile',
              'owner_id': user_id,
              'extended': '1',
              'photo_sizes': '1'
              }
    response = requests.get(get_photos_method_url, params=params)
    profile_list = response.json()
    return profile_list


def download_to_pc(profile_list):
    for file in tqdm(profile_list['response']['items']):
        time.sleep(1)
        file_name = str(file['likes']['count'])
        names_used = set()
        photo_url = file['sizes'][-1]['url']
        date = datetime.utcfromtimestamp(file['date']).strftime('%d.%m.%Y %H_%M_%S')
        if file_name in names_used:
            names_used.add(file_name)
        else:
            names_used.add(str(file['likes']['count']) + '__' + str(date))
        download_photo = requests.get(photo_url)
        with open(f'{pc_download_file_path}/{file_name}.jpg', 'wb') as f:
            f.write(download_photo.content)


def recursive_upload(y, from_dir, to_dir):
    for root, dirs, files in os.walk(from_dir):
        p = root.split(from_dir)[1].strip(os.path.sep)
        dir_path = posixpath.join(to_dir, p)
        for file in tqdm(files):
            time.sleep(1)
            file_path = posixpath.join(dir_path, file)
            p_sys = p.replace("/", os.path.sep)
            in_path = os.path.join(from_dir, p_sys, file)
            y.upload(in_path, file_path, overwrite=True)


def get_info_json(profile_list):
    photos_list = []
    for file in profile_list['response']['items']:
        photos_dict = {}
        size = file['sizes'][-1]['type']
        date = datetime.utcfromtimestamp(file['date']).strftime('%d.%m.%Y %H_%M_%S')
        file_name = str(file['likes']['count']) + '__' + str(date) + '.jpeg'
        photos_dict.update(file_name=file_name, size=size)
        photos_list.append(photos_dict)
    data_list = json.dumps(photos_list, indent=2)
    return data_list


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")

    vk_user_id = int(input('Please enter VK user_id: '))
    # vk_user_id = 552934290
    vk_token = config['vk_api']['access_token']
    api_version = config['vk_api']['api_version']
    get_photos_method_url = config['vk_api']['get_photos_method_url']
    pc_download_file_path = config['files_path']['download_file_path']
    yadisk_file_path = config['yadisk_api']['yadisk_file_path']
    yadisk_token = str(input('Please enter YA_disk token (case sensitive!): '))
    print("")

    vk_profile_list = get_profile_list(vk_user_id)

    y = yadisk.YaDisk(token=yadisk_token)
    to_dir = yadisk_file_path
    from_dir = pc_download_file_path

    print('Downloading files from VK to PC:')
    download_to_pc(vk_profile_list)

    print('\nUploading files from PC to Ya-disk:')
    recursive_upload(y, from_dir, to_dir)

    time.sleep(2)

    print('\nUploaded files info:')
    print(get_info_json(vk_profile_list))
