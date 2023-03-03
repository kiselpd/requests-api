import requests
from pprint import pprint

class StackOverflowAPI:
    def __init__(self) -> None:
        self.url = "https://api.stackexchange.com"

    def __create_params_for_get(self, tagged: str, from_data: str, to_data: str, order: str, sort: str):
        return {"tagged": tagged,
                "todate": to_data,
                "fromdate": from_data,
                "order": order,
                "sort": sort,
                "site": "stackoverflow"}

    def get_list_questions(self, tag: str, from_date: str="", to_date: str="", order: str="desc", sort: str="activity") -> list:
        get_req = requests.get(self.url+"/questions", params=self.__create_params_for_get(tag, from_date, to_date, order, sort))

        if get_req.status_code == 200:
            print("Удачный запрос!")
            return get_req.json()
        else:
            print("Неудачный запрос!")
            return None
        
    


if __name__ == "__main__":
    api_worker = StackOverflowAPI()
    python_list = api_worker.get_list_questions(tag="python", from_date="2023-03-01")
