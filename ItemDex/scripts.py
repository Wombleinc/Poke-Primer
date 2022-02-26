import csv
import os
import pandas


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
