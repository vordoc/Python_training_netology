import requests


def get_smartest_hero():
    name_search_url = "https://superheroapi.com/api/2619421814940190/search/"
    superheroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]

    for hero in superheroes:
        hero_r = requests.get(name_search_url + hero['name'])
        hero['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])

    return sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name']


if __name__ == '__main__':
    print(f'The smartest hero is {get_smartest_hero()}')
