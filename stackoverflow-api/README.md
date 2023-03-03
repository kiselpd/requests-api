## Получение со stackoverflow списка вопросов за период времени с определенным тегом

Самый важный сайт для программистов это [stackoverflow](https://stackoverflow.com/). И у него тоже есть [API](https://api.stackexchange.com/docs)
Нужно написать программу, которая выводит все вопросы за последние два дня и содержит тэг 'Python'.

### *Получение параметров для GET-запроса*
```
def __create_params_for_get(self, tagged: str, from_data: str, to_data: str, order: str, sort: str):
```

### *Получение списка вопросов с определенным фильтром*
```
def get_list_questions(self, tag: str, from_date: str="", to_date: str="", order: str="desc", sort: str="activity") -> list:
```

### *Создает из json-списка словарь вида {title: link}*
```
def get_link_dict(answers_list: list) -> dict:
```