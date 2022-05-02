#import os
#import pandas
import json
import os
import sys
# sys.path.append('/Poke-Primer-main/')

ROOT_DIR = os.path.split(os.path.dirname(__file__))[0] + "\\"

#def load_item_data():
    #ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    #DATASET_PATH = os.path.join(ROOT_DIR, '..\\PokemonData\\items.csv')

    #return pandas.read_csv(DATASET_PATH)


def get_item_id_list():
    with open(ROOT_DIR + "PokemonData\\item.json", 'r') as json_file:
        item_dictionary = json.load(json_file)
    item_id_list = []
    for i in range(0, 1658):
        item_id_list.append(item_dictionary["item"][i]["ID"])
    return item_id_list


def get_item_name_list():
    with open(ROOT_DIR + "PokemonData\\item.json", 'r') as json_file:
        item_dictionary = json.load(json_file)
    item_name_list = []
    for i in range(0, 1658):
        item_name_list.append(item_dictionary["item"][i]["Name"])
    return item_name_list

def get_item_category_list():
    with open(ROOT_DIR + "PokemonData\\item.json", 'r') as json_file:
        item_dictionary = json.load(json_file)
    item_category_list = []
    for i in range(0, 1658):
        item_category_list.append(item_dictionary["item"][i]["Category"])
    return item_category_list

def get_item_id_name_cat_list():
    with open(ROOT_DIR + "PokemonData\\item.json", 'r') as json_file:
        item_dictionary = json.load(json_file)
    item_id_name_cat_list = []
    for i in range(0, 309): 
        item_id_name_cat_list.append(dict(id=item_dictionary["item"][i]["ID"],
                                          name=item_dictionary["item"][i]["Name"],
                                          category=item_dictionary["item"][i]["Category"]))
    return item_id_name_cat_list


# def write_first_gen_items_to_json():
#     dictionary = {"item": []}
#     with open("C:/PokePrimer-jsons/item.json", 'r') as json_file:
#         item_dictionary = json.load(json_file)
#     id_counter = 0
#     for item in item_dictionary["item"]:
#         if "generation-iii" in item["Generation"]:
#             id_counter += 1
#             item["ID"] = id_counter
#             dictionary["item"].append(item)
#     result = json.dumps(dictionary, indent=3)
#     with open('C:/PokePrimer-jsons/gen_one_item.json', 'w') as outfile:
#         outfile.write(result)

#def write_items_to_json():
#    url = "https://pokeapi.co/api/v2/item/"
#    dictionary = {"item": []}
#    for index in range(1, 1659):
#        try:
#            item_obj = Item(url + str(index))
#            keys = ["ID", "Name", "Cost", "Attribute List", "Category", "Effect",
#                    "Generation", "Sprite URL"]
#            values = [item_obj.get_id(), item_obj.get_fancy_name(), item_obj.get_cost(),
#                    item_obj.get_attribute_list(), item_obj.get_category(),
#                    item_obj.get_effect(), item_obj.get_game_indices(), item_obj.get_sprite_url()]
#            #dictionary[index - 1] = dict(zip(keys, values))
#            dictionary["item"].append(dict(zip(keys, values)))
#            print(dictionary)
#        except json.decoder.JSONDecodeError:
#            continue
#    result = json.dumps(dictionary, indent=3)
#    with open('../PokemonData/item.json', 'w') as f:
#        f.write(result)