from PokeDex.PokeDex import *

"""
    This is the class that's going to pull one thing from the database
    and put it in a format the UI can use.
    The asset ID is being stored in self.number
"""
class Card:

    def __init__(self, id):
        pokemon = Pokemon(*Pokemon.pokemon_attributes(id))
        self.number = str(id)
        pokeIDName = all_pokemon_list()
        self.name = pokeIDName[id]
        self. description = pokemon.pokemon_info()
