import csv
import os
import pandas
import json
from Item import Item


def load_item_data():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATASET_PATH = os.path.join(ROOT_DIR, '..\\PokemonData\\items.csv')

    return pandas.read_csv(DATASET_PATH)


def get_item_id_list():
    item_data_frame = load_item_data()
    item_id_list = []
    i = 0
    for i in range(0, 1607):
        item_id_list.append(item_data_frame.get("id")[i])
        i += 1
    return item_id_list


def get_item_name_list():
    item_data_frame = load_item_data()
    item_name_list = []
    i = 0
    for i in range(0, 1607):
        item_name_list.append(item_data_frame.get("name")[i].replace('-', ' ').title())
        i += 1
    return item_name_list


def write_items_to_json():
    url = "https://pokeapi.co/api/v2/item/"
    dictionary = {"item": []}
    for index in range(1, 1659):
        try:
            item_obj = Item(url + str(index))
            keys = ["ID", "Name", "Cost", "Attribute List", "Category", "Effect",
                    "Generation", "Sprite URL"]
            values = [item_obj.get_id(), item_obj.get_fancy_name(), item_obj.get_cost(),
                    item_obj.get_attribute_list(), item_obj.get_category(),
                    item_obj.get_effect(), item_obj.get_game_indices(), item_obj.get_sprite_url()]
            #dictionary[index - 1] = dict(zip(keys, values))
            dictionary["item"].append(dict(zip(keys, values)))
            print(dictionary)
        except json.decoder.JSONDecodeError:
            continue
    result = json.dumps(dictionary, indent=3)
    with open('item.json', 'w') as f:
        f.write(result)
