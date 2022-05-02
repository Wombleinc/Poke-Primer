#from prettytable import PrettyTable


# defines the "Move" object, of which every Pokémon move is a type
class Move:

    def __init__(self, move_id, name, move_type, category, pp, power, accuracy, gen):
        self.move_id = move_id
        self.name = name
        self.move_type = move_type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.gen = gen

    #def __str__(self):
        #pt = PrettyTable()
        #pt.field_names = ["ID", "Name", "Type", "Category", "PP", "Power", "Accuracy", "Gen"]
        #pt.add_row([self.move_id, self.name, self.move_type, self.category, self.pp, self.power,
                    #self.accuracy, self.gen])
        #return pt.__str__()
