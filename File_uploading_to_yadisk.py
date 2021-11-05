import requests
import configparser

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'False'}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        response = self.get_upload_link(disk_file_path=disk_file_path)
        url = response.get('href', '')

        if url:
            response = requests.put(url=url, data=open(filename, 'rb'))
            print(response.status_code)

            response.raise_for_status()
            if response.status_code == 201:
                print('Success')

        else:
            print('Empty URL')


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")
    token = config['yadisk_api']['api_token']
    disk_file_path = '/test/Somebullshit.txt'
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(disk_file_path, 'Somebullshit.txt')
