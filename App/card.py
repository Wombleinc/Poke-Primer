"""
    This is the class that's going to pull one thing from the database
    and put it in a format the UI can use.
    The asset ID is being stored in self.number
"""
from MoveDex.code.scripts import get_move_accuracy, get_move_category, get_move_name, get_move_power, get_move_pp, get_move_sprite_url, get_move_type
from Trainer.scripts import get_pokemon_icon_url, get_pokemon_info
from ItemDex.request_item import get_item_name, get_item_effect, get_item_category, get_item_sprite_url

class CardPokemon:

    def __init__(self, id):
        self.number = str(id)
        info = get_pokemon_info(id)
        self.name = info['Name']
        self.genus = info['Genus']
        self.type_1 = info['Type 1']
        self.type_2 = info['Type 2']
        self.hp = info['HP']
        self.attack = info['Attack']
        self.defense = info['Defense']
        self.special_attack = info['Special Attack']
        self.special_defense = info['Special Defense']
        self.speed = info['Speed']
        self.generation = info['Generation']
        self.icon_url = get_pokemon_icon_url(id)

class CardItem:
    def __init__(self, id):
        self.number = str(id)
        self.name = get_item_name(id)
        self.description = get_item_effect(id)
        self.category = get_item_category(id)
        self.sprite_url = get_item_sprite_url(id)

class CardMove:
    def __init__(self, id):
        self.number = str(id)
        self.name = get_move_name(id)
        self.power = get_move_power(id)
        self.accuracy = get_move_accuracy(id)
        self.type = get_move_type(id)
        self.category = get_move_category(id)
        self.pp = get_move_pp(id)
        self.sprite_url = get_move_sprite_url(id)