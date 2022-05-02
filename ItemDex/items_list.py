import requests
import json
from Item import Item


def request_data(url):
    url_result = requests.get(url)
    url_result = url_result.text
    poke_api_data = json.loads(url_result)
    return poke_api_data


def all_item_objects_list():
    url = 'https://pokeapi.co/api/v2/item/?limit=1607'
    data = request_data(url)
    all_item_objects_list = {}
    id_count = 0
    for i in data['results']:
        all_item_objects_list[id_count] = Item(i['url'])
        id_count += 1

    return all_item_objects_list


def print_all_item_objects():  #TAKES A VERY LONG TIME TO EXECUTE
    items_list = all_item_objects_list()
    for i in range(0, 1607):
        print(items_list[i])


def all_items_list():
    url = 'https://pokeapi.co/api/v2/item/?limit=1607'
    data = request_data(url)
    all_items_list = {}
    id_count = 0
    for item in data['results']:
        id_count += 1
        all_items_list[id_count] = item['name']

    return all_items_list


def print_all_items():
    items_list = all_items_list()
    i = 0
    while i != 1607:
        for i in range(1, 1608):
            print(f"ID: {i: <3} Name: {items_list[i].title(): <22}")
