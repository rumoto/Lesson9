import requests

def get_hero_id_name(hero_list):
    """get_hero_id_name(hero_list) -> searching hero by name.
    return dict {'id': 'hero_id', 'name': hero_name}"""
    hero_id_and_name = []
    for hero in hero_list:
        url = f'https://superheroapi.com/api/2619421814940190/search/{hero}'
        response = requests.get(url)
        hero_info = response.json()['results']
        for value in hero_info:
            hero_current = {}
            if value['name'] == hero:
                hero_current['id'] = value['id']
                hero_current['name'] = value['name']
                hero_id_and_name.append(hero_current)
    return hero_id_and_name

def get_hero_intelligence(hero_list):
    """get_hero_intelligence(hero_list) -> input hero intelligence in hero dict.
    return dict {'id': 'hero_id', 'name': hero_name, 'intelligence': 'intelligence'}"""
    heroes = get_hero_id_name(hero_list)
    for id, hero in enumerate(heroes):

        url = f"https://superheroapi.com/api/2619421814940190/{hero['id']}/powerstats"
        response = requests.get(url)
        hero_intelligence = int(response.json()['intelligence'])
        hero['intelligence'] = hero_intelligence
        heroes[id] = hero

    return heroes

def compare_heroes_intelligence(hero_list):
    """compare_hero_intelligence(hero_list) -> compares heroes by intelligence.
    return dict {'id': 'hero_id', 'name': hero_name, 'intelligence': 'intelligence'}"""
    heroes = get_hero_intelligence(hero_list)
    intelligence = 0
    most_intelligence_hero = {}
    for hero in heroes:
        hero_intelligence = hero['intelligence']
        if hero_intelligence > intelligence:
            intelligence = hero_intelligence
            most_intelligence_hero = hero
    print(f"Самый умный: {most_intelligence_hero['name']}\nid: {most_intelligence_hero['id']}\nУровень IQ:{most_intelligence_hero['intelligence']}")

    return most_intelligence_hero

if __name__ == '__main__':
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    compare_heroes_intelligence(hero_list)