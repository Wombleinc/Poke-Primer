from prettytable import PrettyTable


# defines the "Move" object, of which every Pokémon move is a type
class Move:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.accuracy = 0
        self.pp = 0
        self.priority = 0  # might cut
        self.power = 0

    def __str__(self):
        pt = PrettyTable()
        pt.field_names = ["ID", "Name", "Accuracy", "PP", "Priority", "Power"]
        pt.add_row([self.id, self.name, self.accuracy, self.pp, self.priority,
                    self.power])
        return pt.__str__()
