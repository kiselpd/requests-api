import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.host = "https://cloud-api.yandex.net"

    def get_headers(self): #Получить заголовок для запроса
        return {"Content-Type" : "application/json",
                "Authorization": f"OAuth {self.token}"}
    
    def get_upload_link(self, file_name: str): #Получить ссылку для загрузки файла
        get_params = {"path": f"/{file_name}", "overwrite": True}
        req = requests.get(f"{self.host}/v1/disk/resources/upload/", headers=self.get_headers(), params=get_params)
        return req.json().get("href")
    
    def upload_file(self, file_path: str, dir_name=''): #Загрузить файл
        file_name_poz = file_path.rfind("/")
        file_name = file_path if file_name_poz == -1 else file_path[file_name_poz + 1 : ]
        
        upload_link = self.get_upload_link(dir_name+file_name)
        response = requests.put(upload_link, data=open(file_path, "rb"), headers = self.get_headers())

        # print(response.status_code)

        if response.status_code == 201:
            print(f"Файл {file_name} загружен!")

    def create_dir(self, dir_name: str): #создать директорию
        put_params = {"path": dir_name}
        response = requests.put(f"{self.host}/v1/disk/resources/", headers=self.get_headers(), params=put_params)

        if response.status_code ==  409:
            print(f"Папка {dir_name} уже сущетвует!")

        if response.status_code == 201:
            print(f"Папка {dir_name} создана!")
        

if __name__ == '__main__':
    path_to_txt_file = "content/text.txt"
    path_to_png_file = "content/picture.png"
    dir = "netology-test/"
    token = ...

    uploader = YaUploader(token)
    result_create_dir = uploader.create_dir(dir)
    result_upload_file = uploader.upload_file(path_to_txt_file, dir) # параметр dir необязателен, тогда файл загружается в корневой каталог