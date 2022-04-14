# Christopher Duke
# Trainer/classes.py
import json
import os

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

        if "item" in kwargs:
            self.item = None
        else:
            self.item = None

        if "move_1" in kwargs:
            self.move_1 = None
        else:
            self.move_1 = None

        if "move_2" in kwargs:
            self.move_2 = None
        else:
            self.move_2 = None

        if "move_3" in kwargs:
            self.move_3 = None
        else:
            self.move_3 = None

        if "move_4" in kwargs:
            self.move_4 = None
        else:
            self.move_4 = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_item(self):
        return self.item

    def get_move_1(self):
        return self.move_1

    def get_move_2(self):
        return self.move_2

    def get_move_3(self):
        return self.move_3

    def get_move_4(self):
        return self.move_4

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_item(self, item):
        self.item = item

    def set_move_1(self, move_1):
        self.move_1 = move_1

    def set_move_2(self, move_2):
        self.move_2 = move_2

    def set_move_3(self, move_3):
        self.move_3 = move_3

    def set_move_4(self, move_4):
        self.move_4 = move_4


class Team:
    MAXIMUM_CAPACITY = 6

    def __init__(self, *args):
        self.members = [Pokemon(), Pokemon(), Pokemon(), Pokemon(), Pokemon(), Pokemon()]

        if 0 < len(args) <= 6:
            for pokemon in args:
                self.add_pokemon(pokemon)
        if len(args) > 6:
            print("Too many Pokemon")

    def get_pokemon(self, name):
        for count, pokemon in enumerate(self.members):
            if name == pokemon.get_name():
                return self.members[count]
        raise Exception("No such Pokemon on your team.")

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

    def add_pokemon(self, pokemon):
        count = 0
        for member in self.members:
            if member.id != 0:
                count += 1

        if count < self.MAXIMUM_CAPACITY:
            self.members.pop(count)
            self.members.insert(count, pokemon)
        else:
            print("Team's too big! Data wasn't changed.")
    
    def remove_pokemon(self, id):
        count = 0
        remove_id = 0
        for member in self.members:
            if member.id != 0:
                if member.id == id:
                    remove_id = count
                    break
                count += 1
            self.members.pop(remove_id)
            self.members.append(Pokemon())

    def add_from_id_to_team(self, pokemon_id):
        """
        :param pokemon_id: The id to create a pokemon from
        :param team: The user's pokemon team
        :return: Nothing, but the specified pokemon is created and stored in the user's pokemon team
        """
        self.add_pokemon(create_pokemon_from_id(pokemon_id))

    def save_team_to_json(self):
        team_dict = {
            "pokemon": [
                {
                    "slot": 1,
                    "id": int(self.members[0].get_id()),
                    "name": self.members[0].get_name(),
                    "item": self.members[0].get_item(),
                    "move_1": self.members[0].get_move_1(),
                    "move_2": self.members[0].get_move_2(),
                    "move_3": self.members[0].get_move_3(),
                    "move_4": self.members[0].get_move_4()
                },
                {
                    "slot": 2,
                    "id": int(self.members[1].get_id()),
                    "name": self.members[1].get_name(),
                    "item": self.members[1].get_item(),
                    "move_1": self.members[1].get_move_1(),
                    "move_2": self.members[1].get_move_2(),
                    "move_3": self.members[1].get_move_3(),
                    "move_4": self.members[1].get_move_4()
                },
                {
                    "slot": 3,
                    "id": int(self.members[2].get_id()),
                    "name": self.members[2].get_name(),
                    "item": self.members[2].get_item(),
                    "move_1": self.members[2].get_move_1(),
                    "move_2": self.members[2].get_move_2(),
                    "move_3": self.members[2].get_move_3(),
                    "move_4": self.members[2].get_move_4()
                },
                {
                    "slot": 4,
                    "id": int(self.members[3].get_id()),
                    "name": self.members[3].get_name(),
                    "item": self.members[3].get_item(),
                    "move_1": self.members[3].get_move_1(),
                    "move_2": self.members[3].get_move_2(),
                    "move_3": self.members[3].get_move_3(),
                    "move_4": self.members[3].get_move_4()
                },
                {
                    "slot": 5,
                    "id": int(self.members[4].get_id()),
                    "name": self.members[4].get_name(),
                    "item": self.members[4].get_item(),
                    "move_1": self.members[4].get_move_1(),
                    "move_2": self.members[4].get_move_2(),
                    "move_3": self.members[4].get_move_3(),
                    "move_4": self.members[4].get_move_4()
                },
                {
                    "slot": 6,
                    "id": int(self.members[5].get_id()),
                    "name": self.members[5].get_name(),
                    "item": self.members[5].get_item(),
                    "move_1": self.members[5].get_move_1(),
                    "move_2": self.members[5].get_move_2(),
                    "move_3": self.members[5].get_move_3(),
                    "move_4": self.members[5].get_move_4()
                }
            ]
        }

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
        new_move = Move(id)
        self.members.append(new_move)
    
    def remove_move(self, id):
        for move in self.members:
            if move.get_id() == id:
                self.members.remove(move)
                break
    
    def get_move_id_list(self):
        move_list = []
        for move in self.members:
            move_list.append(move.get_id())
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