from pprint import pprint

import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': F'OAuth {self.token}'}
        params = {"path": file_path, "overwrite": "true"}
        response_link = requests.get(upload_url, headers=headers, params=params)
        upload_link = response_link.json()['href']
        response_upload = requests.put(upload_link, data=open(file_path, 'rb'))
        response_upload.raise_for_status()
        if response_upload.status_code == 201:
            print("Success")

if __name__ == '__main__':
    path_to_file = input('Введите имя файла для загрузки: ')
    token = input('Введите ваш токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)