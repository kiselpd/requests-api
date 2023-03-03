import requests


def send_get_request(url : str):
    return requests.get(url)

def find_max_intelligence(heroes_json_data, hero_names):
    intelligence_dict = {hero["name"]: hero["powerstats"]["intelligence"] for hero in heroes_json_data if hero["name"] in hero_names}
    return {key: intelligence_dict[key] for key in intelligence_dict.keys() if intelligence_dict[key] == max(intelligence_dict.values())}

def solution():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    hero_names = ["Hulk", "Captain America", "Thanos"]

    req = send_get_request(url)
    
    if req.status_code == 200:
        smartest_hero = find_max_intelligence(req.json(), hero_names)
        print(smartest_hero)


if __name__ == '__main__':
    solution()