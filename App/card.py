"""This is the class that's going to pull one thing from the database
and put it in a format the UI can use."""
class Card:

    def __init__(self, id):
        self.number = str(id)
        self.name = "mew"
        self. description = "mew is cute"
