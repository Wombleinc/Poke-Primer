import json
import sys

sys.path.append('/Poke-Primer-main/')
sys.path.append('..')
sys.path.append('../../MoveDex')

from MoveDex.code.move import Move


def build_move_dict():
    with open("PokemonData/moves.json", 'r') as move_json:
        move_dict = json.load(move_json)
    return move_dict

def get_move_id_list():
    move_dict = build_move_dict()
    move_id_list = []
    for i in range(0,850):
        move_id_list.append(move_dict['move'][i]['#'])
    return move_id_list

def get_move_name_list():
    move_dict = build_move_dict()
    move_name_list = []
    for i in range(0,850):
        move_name_list.append(move_dict['move'][i]['Name'])
    return move_name_list

def get_move_type_list():
    move_dict = build_move_dict()
    move_type_list = []
    for i in range(0,850):
        move_type_list.append(move_dict['move'][i]['Type'])
    return move_type_list

def get_move_master_list():
    move_dict = build_move_dict()
    move_list_sort = []
    for i in range(0,850):
        move_list_sort.append(dict(id=move_dict['move'][i]['#'],name=move_dict['move'][i]['Name'],type=move_dict['move'][i]['Type']))
    return move_list_sort

def get_move_move_list():
    move_dict = build_move_dict()
    move_list = []
    for i in range(0,850):
        generic_move = Move(
            move_dict['move'][i]['#'],
            move_dict['move'][i]['Name'],
            move_dict['move'][i]['Type'],
            move_dict['move'][i]['Category'],
            move_dict['move'][i]['PP'],
            move_dict['move'][i]['Power'],
            move_dict['move'][i]['Accuracy'],
            move_dict['move'][i]['Gen'],
        )
        move_list.append(generic_move)
    return move_list

# cards stuff - these grab the move name, power, acuracy,
# type, category, and PP and pass them to cards.py

def get_move_name(id):
    move_list = get_move_move_list()
    move_name = None

    for move in move_list:
        if move.move_id == id:
            move_name = move.name

    return move_name

def get_move_power(id):
    move_list = get_move_move_list()
    move_power = None

    for move in move_list:
        if move.move_id == id:
            move_power = move.power

    return move_power

def get_move_accuracy(id):
    move_list = get_move_move_list()
    move_accuracy = None

    for move in move_list:
        if move.move_id == id:
            move_accuracy = move.accuracy

    return move_accuracy

def get_move_type(id):
    move_list = get_move_move_list()
    move_type = None

    for move in move_list:
        if move.move_id == id:
            move_type = move.move_type

    return move_type

def get_move_category(id):
    move_list = get_move_move_list()
    move_category = None

    for move in move_list:
        if move.move_id == id:
            move_category = move.category

    return move_category

def get_move_pp(id):
    move_list = get_move_move_list()
    move_pp = None

    for move in move_list:
        if move.move_id == id:
            move_pp = move.pp

    return move_pp