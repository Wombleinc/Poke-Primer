# Christopher Duke
# Trainer/classes.py
from Trainer.scripts import load_pokemon_data


def create_pokemon_from_id(pokemon_id):
    """
    :param pokemon_id: The id to create a pokemon from
    :return: a pokemon with the id and the name that matches it
    """
    pokemon_data_frame = load_pokemon_data()
    return Pokemon(pokemon_id, str(pokemon_data_frame.get("name")[pokemon_id - 1]))


def add_from_id_to_team(pokemon_id, team):
    """
    :param pokemon_id: The id to create a pokemon from
    :param team: The user's pokemon team
    :return: Nothing, but the specified pokemon is created and stored in the user's pokemon team
    """
    team.add_pokemon(create_pokemon_from_id(pokemon_id))


class Pokemon:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.item = None
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_item(self):
        return self.item

    def get_move1(self):
        return self.move1

    def get_move2(self):
        return self.move2

    def get_move3(self):
        return self.move3

    def get_move4(self):
        return self.move4

    def set_name(self, name):
        self.name = name

    def set_item(self, item):
        self.item = item

    def set_move1(self, move1):
        self.move1 = move1

    def set_move2(self, move2):
        self.move2 = move2

    def set_move3(self, move3):
        self.move3 = move3

    def set_move4(self, move4):
        self.move4 = move4

    def __str__(self):
        return "Name: " + self.get_name() + ", Item: " + str(self.get_item()) + \
               ", Move 1: " + str(self.get_move1()) + ", Move 2: " + str(self.get_move2()) + \
               ", Move 3: " + str(self.get_move3()) + ", Move 4: " + str(self.get_move4()) + "\n"


class Team:
    MAXIMUM_CAPACITY = 6

    def __init__(self, *args):
        self.members = []

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
        if len(self.members) < self.MAXIMUM_CAPACITY:
            self.members.append(pokemon)

    def delete_pokemon(self, pokemon):
        if len(self.members) != 0:
            self.members.remove(pokemon)

    def __str__(self):
        return_string = "List of Pokemon:\n"
        for pokemon in self.members:
            return_string += pokemon.__str__()
        return return_string
