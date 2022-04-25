# Christopher Duke
# Trainer/classes.py
import json
import os
from MoveDex.code.scripts import get_move_list

ROOT_DIR = os.path.split(os.path.dirname(__file__))[0] + "\\"

from Trainer.scripts import all_pokemon_name_list
from ItemDex.Item import Item
from MoveDex.code.move import Move


def create_pokemon_from_id(pokemon_id):
    """
    :param pokemon_id: The id to create a pokemon from
    :return: a pokemon with the id and the name that matches it
    """
    return Pokemon(id=pokemon_id, name=str(all_pokemon_name_list()[pokemon_id]))


class Pokemon:
    # This class now handles variable arguments
    def __init__(self, **kwargs):
        if "id" in kwargs:
            self.id = kwargs.get("id")
        else:
            self.id = 0

        if "name" in kwargs:
            self.name = kwargs.get("name")
        else:
            self.name = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name


class Team:
    def __init__(self, *args):
        self.members = []

    def add_pokemon(self, id):
        self.members.append(create_pokemon_from_id(id))
    
    def remove_pokemon(self, id):
        for pokemon in self.members:
            if pokemon.get_id() == id:
                self.members.remove(pokemon)
                break
    
    def get_team_id_list(self):
        pokemon_list = []
        for pokemon in self.members:
            pokemon_list.append(pokemon.get_id())
        return pokemon_list

    def get_team_name_list(self):
        pokemon_list = []
        for pokemon in self.members:
            pokemon_list.append(pokemon.get_name())
        return pokemon_list

    def save_team_to_json(self):
        team_dict = {
            "pokemon": []
        }

        for pokemon in self.members:
            new_data = {
                "id": int(self.members[0].get_id()),
                "name": self.members[0].get_name()
            }

            team_dict["pokemon"].append(new_data)

        with open(ROOT_DIR + "Trainer\\team.json", "w") as json_file:
            json.dump(team_dict, json_file, indent=4)

class TrainerBag:
    def __init__(self):
        self.members = []
    
    def add_item(self, id):
        new_item = Item(id)
        self.members.append(new_item)
    
    def remove_item(self, id):
        for item in self.members:
            if item.get_id() == id:
                self.members.remove(item)
                break
    
    def get_item_id_list(self):
        item_list = []
        for item in self.members:
            item_list.append(item.get_id())
        return item_list
    
    def get_item_name_list(self):
        item_list = []
        for item in self.members:
            item_list.append(item.get_name())
        return item_list
    
    def get_item_category_list(self):
        item_list = []
        for item in self.members:
            item_list.append(item.get_category())
        return item_list
    
    def save_bag_to_json(self):
        bag_dict = {
            "items": []
        }

        for item in self.members:
            new_data = {
                "item_id": int(item.get_id()),
                "item_name": item.get_name(),
                "item_category": item.get_category()
            }
            
            bag_dict["items"].append(new_data)

        with open(ROOT_DIR + "Trainer\\bag.json", "w") as json_file:
            json.dump(bag_dict, json_file, indent=4)

class TrainerMoves:

    def __init__(self):
        self.members = []
    
    def add_move(self, id):
        move_list = get_move_list()

        new_move = move_list[id-1]
        self.members.append(new_move)
    
    def remove_move(self, id):
        for move in self.members:
            if move.move_id == id:
                self.members.remove(move)
                break
    
    def get_move_id_list(self):
        move_list = []
        for move in self.members:
            move_list.append(move.move_id)
        return move_list
    
    def get_move_name_list(self):
        move_list = []
        for move in self.members:
            move_list.append(move.name)
        return move_list
    
    def get_move_type_list(self):
        move_list = []
        for move in self.members:
            move_list.append(move.move_type)
        return move_list
    
    def save_moves_to_json(self):
        move_dict = {
            "moves": []
        }

        for move in self.members:
            new_data = {
                "move_id": int(move.move_id),
                "move_name": move.name,
                "move_type": move.move_type,
                "move_category": move.category,
                "move_pp": move.pp,
                "move_power": move.power,
                "move_accuracy": move.accuracy
            }

            move_dict["moves"].append(new_data)
        
        with open(ROOT_DIR + "Trainer\\moves.json", "w") as json_file:
            json.dump(move_dict, json_file, indent=4)