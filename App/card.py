"""
    This is the class that's going to pull one thing from the database
    and put it in a format the UI can use.
    The asset ID is being stored in self.number
"""
class Card:

    def __init__(self, id):
        self.number = str(id)
        pokeIDName = ["MissingNo", "Bulbasaur", "Ivysaur", "Venusaur","Poke Ball", "Town Map", "Bicycle", "??????", " ", " ","Scratch", "Vise Grip", "Guillotine", "Razor Wind"]
        pokeIDDesc = ["The glitch Pokemon", "The plant Pokemon", "An Evolved Pokemon", "Watch Out!",
                      "A Ball thrown at wild Pokémon to catch them.", "A map of the local area. It identifies your present location.",
                      "Lets you travel twice as fast as walking.", "Allows surfing over water without the need for Pokémon and/or Badges.", " ", " ","Normal", "Normal", "Normal", "Normal"]
        self.name = pokeIDName[id]
        self. description = pokeIDDesc[id]
