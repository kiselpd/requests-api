## Загрузка файла на Яндекс диск

### *Получение ссылки для загрузки*
````
def get_upload_link(self, file_name: str)
# file_name -> имя файла
````

### *Загрузка файла*
````
def upload_file(self, file_path: str, dir_name='')
# file_path -> путь до файла у пользователя
# dir_name(необязательно) -> имя папки, в которую хотим загрузить файл
````

### *Создание папки*
````
def create_dir(self, dir_name: str)
# dir_name -> имя папки
````

