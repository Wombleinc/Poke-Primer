import json
import sys


sys.path.append('/Poke-Primer-main/')

def build_move_dict():
    with open("PokemonData/moves.json", 'r') as move_json:
        move_dict = json.load(move_json)
    return move_dict

def get_move_id_list():
    move_dict = build_move_dict()
    move_id_list = []
    for i in range(0,20):
        move_id_list.append(move_dict["move"][i]['#'])
    return move_id_list

def get_move_name_list():
    move_dict = build_move_dict()
    move_name_list = []
    for i in range(0,20):
        move_name_list.append(move_dict["move"][i]["Name"])
    return move_name_list

def get_move_type_list():
    move_dict = build_move_dict()
    move_type_list = []
    for i in range(0,20):
        move_type_list.append(move_dict["move"][i]["Type"])
    return move_type_list

# def get_move_master_list():
#     move_dict = build_move_dict()
#     move_list = []
#     for i in range(0,850):
#         move_list.append(dict(id=move_dict["move"][i][""]))
