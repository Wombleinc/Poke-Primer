import requests
import json


def request_item(url):
    url_result = requests.get(url)
    url_result = url_result.text
    poke_api_item_data = json.loads(url_result)
    return poke_api_item_data


def get_item_id(item_url):
    return request_item(item_url)['id']


def get_item_name(item_url):
    return request_item(item_url)['name']


def get_item_fancy_name(item_url):
    string = get_item_name(item_url)
    return string.replace('-', ' ').title()


def get_item_cost(item_url):
    return request_item(item_url)['cost']


def get_item_attribute_list(item_url):
    attributes = request_item(item_url)['attributes']
    list = []
    for i in attributes:
        list.append(i['name'])
    return list


def get_item_category(item_url):
    return request_item(item_url)['category']['name']


def get_item_effect(item_url):
    effect_entries = request_item(item_url)['effect_entries']
    string = ''
    for i in effect_entries:
        string += i['effect']
    return string


def get_item_game_indices(item_url):
    game_indices = request_item(item_url)['game_indices']
    list = []
    for i in game_indices:
        list.append(i['generation']['name'])
    return list


def get_item_sprite_url(item_url):
    return request_item(item_url)['sprites']['default']


#print(get_item_id('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_name('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_fancy_name('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_cost('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_attribute_list('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_category('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_effect('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_game_indices('https://pokeapi.co/api/v2/item/1/'))
#print(get_item_sprite_url('https://pokeapi.co/api/v2/item/1/'))