import requests
class YaUploader:
    def __init__(self, _token: str):
        self.token = _token
    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net:443"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Downloads/{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get('href', '')
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка загрузки! Код ошибки: {response.status_code}"
if __name__ == '__main__':
    path_to_file = '/Users/albina/Downloads/эссе.docx'
    token = ''
    uploader = YaUploader(token)
    print(f"Загружаем файл {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
