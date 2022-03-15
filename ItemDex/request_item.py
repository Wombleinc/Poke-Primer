import requests
import json


def request_item_from_url(url):
    url_result = requests.get(url)
    url_result = url_result.text
    poke_api_item_data = json.loads(url_result)
    return poke_api_item_data


def request_item(item_id):
    with open('..\\PokemonData\\item.json', 'r') as json_file:
        item_dictionary = json.load(json_file)
    index = item_id - 1
    return item_dictionary["item"][index]


def get_item_id(item_id):
    return request_item(item_id)["ID"]


def get_item_name(item_id):
    return request_item(item_id)["Name"]


def get_item_cost(item_id):
    return request_item(item_id)["Cost"]


def get_item_attribute_list(item_id):
    return request_item(item_id)["Attribute List"]


def get_item_category(item_id):
    return request_item(item_id)["Category"]


def get_item_effect(item_id):
    return request_item(item_id)["Effect"]


def get_item_generation(item_id):
    return request_item(item_id)["Generation"]


def get_item_sprite_url(item_id):
    return request_item(item_id)["Sprite URL"]
