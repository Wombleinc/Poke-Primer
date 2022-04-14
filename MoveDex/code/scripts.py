import json
import sys

sys.path.append('/Poke-Primer-main/')

from MoveDex.code.move import Move

def build_move_dict():
    """Builds a dictionary of move data, including ID number, Name, Type, Category,
    PP, Power, Accuracy, and Gen, to save space doing this same process in every method."""
    with open("PokemonData/moves.json", 'r') as move_json:
        move_dict = json.load(move_json)
    return move_dict
    
def get_move_list():
    """Creates a list of Move objects from the dictionary created in build_move_dict(), 
    with the attributes properly associated."""
    move_dict = build_move_dict()
    move_list = []
    # uncomment below and comment "for i in range(0,165):" for all moves across all current generations
    # for i in range(0,850):
    for i in range(0,165): # limited to generation 1 for quicker access time
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

# Accessed by main.py

def get_move_id_list():
    """Gets a list of move ID's alone, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_id_list = []
    for move in move_list:
        move_id_list.append(move.move_id)
    return move_id_list

def get_move_name_list():
    """Gets a list of move names alone, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_name_list = []
    for move in move_list:
        move_name_list.append(move.name)
    return move_name_list

def get_move_type_list():
    """Gets a list of move types alone, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_type_list = []
    for move in move_list:
        move_type_list.append(move.move_type)
    return move_type_list

def get_move_sorting_list():
    """Populates a list of dictionaries of move ID-name-type triplets for sorting purposes in main.py.
    Original idea adapted from code in ItemDex."""
    move_list = get_move_list()
    move_sorting_list = []
    for move in move_list:
        move_sorting_list.append(dict(id=move.move_id, name=move.name, type=move.move_type))
    return move_sorting_list

# Accessed by cards.py

def get_move_name(id):
    """Grabs a specific move name by ID, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_name = None

    for move in move_list:
        if move.move_id == id:
            move_name = move.name

    return move_name

def get_move_power(id):
    """Grabs a specific move power by ID, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_power = None

    for move in move_list:
        if move.move_id == id:
            move_power = move.power

    return move_power

def get_move_accuracy(id):
    """Grabs a specific move accuracy by ID, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_accuracy = None

    for move in move_list:
        if move.move_id == id:
            move_accuracy = move.accuracy

    return move_accuracy

def get_move_type(id):
    """Grabs a specific move type by ID, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_type = None

    for move in move_list:
        if move.move_id == id:
            move_type = move.move_type

    return move_type

def get_move_category(id):
    """Grabs a specific move category (whether the move is physical or special) by ID, using the move_list of 
    Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_category = None

    for move in move_list:
        if move.move_id == id:
            move_category = move.category

    return move_category

def get_move_pp(id):
    """Grabs a specific move PP (Power Points) by ID, using the move_list of Move objects set up in get_move_list()."""
    move_list = get_move_list()
    move_pp = None

    for move in move_list:
        if move.move_id == id:
            move_pp = move.pp

    return move_pp