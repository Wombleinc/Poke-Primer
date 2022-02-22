# Christopher Duke
# TeamDex/classes.py

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.item = None
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None

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
