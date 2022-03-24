"""
    This is the class that's going to pull one thing from the database
    and put it in a format the UI can use.
    The asset ID is being stored in self.number
"""
from Trainer.scripts import get_pokemon_genus, get_pokemon_name

class CardPokemon:

    def __init__(self, id):
        self.number = str(id)
        self.name = get_pokemon_name(id)
        self.description = get_pokemon_genus(id)

class CardItem:
    def __init__(self, id):
        self.number = str(id)
        self.name = get_item_name(id)
        self.description = get_item_genus(id)

class CardMove:
    def __init__(self, id):
        self.number = str(id)
        self.name = get_move_name(id)
        self.description = get_move_genus(id)