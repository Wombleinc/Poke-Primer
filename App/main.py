from functools import partial

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp

from ItemDex.scripts import get_item_id_list, get_item_name_list
from MoveDex.code.scripts import move_list
from Trainer.classes import Team
from PokeDex.PokeDex import *
from card import Card

import MoveDex as movedex

Window.clearcolor = (1, 1, 1, 1)
Window.size = (540, 1140)

"""
    This class creates a card for each pokemon/move/item that stores its id
    It generates a button for the asset to be displayed on the appropriate screen
    When the button is clicked, it creates a popup displaying the details about the asset
    Note: Nothing in here should need to be touched to connect to DBs
 """


class PokemonCard(BoxLayout):
    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.popup = None
        self.id = id

    def GetCardData(self, *args):
        print(self.id)
        myCard = Card(self.id)
        content = BoxLayout(orientation="vertical")
        self.popup = Popup(title=myCard.name, size_hint=(None, None),
                           size=(400, 400), auto_dismiss=False,
                           content=content)
        numberLabel = Label(text=myCard.number)
        nameLabel = Label(text=myCard.name)
        descLabel = Label(text=myCard.description)

        button = Button(text="Add")
        button.bind(on_release=partial(self.AddToTrainer))
        close_btn = Button(text="Close", on_press=self.popup.dismiss)
        content.add_widget(numberLabel)
        content.add_widget(nameLabel)
        content.add_widget(descLabel)
        content.add_widget(button)
        content.add_widget(close_btn)
        self.popup.open()

    def CreatePokeButton(self, poke_id, poke_name):
        self.id = poke_id
        button = Button(text=str(poke_id) + " " + poke_name,
                        size_hint=(.95, None), size=(100, 40),
                        pos_hint={'center_x': .5})
        button.bind(on_release=partial(self.GetCardData))
        return button

    def AddToTrainer(self, *args):
        # This function now saves teams to json instead of csv
        ContentNavigationDrawer.pokeTeam.add_from_id_to_team(self.id)
        ContentNavigationDrawer.pokeTeam.save_team_to_json()


class ContentNavigationDrawer(BoxLayout):
    pokeTeam = Team()
    pass


""" 
    This class controls the pokemon buttons on the PokeDex screen
    This needs to be hooked up to the DB with a list of IDs and Names
"""


class PokeDex(BoxLayout):

    def GeneratePokemon(self):
        """These two arrays are taking place of reading the data from the DB"""
        pokeIDList = GetPokemonID()
        pokeIDName = all_pokemon_list()
        """The above arrays need to be fixed to access dbs"""

        for poke in pokeIDList:
            pCard = PokemonCard(poke)
            button = pCard.CreatePokeButton(poke, pokeIDName[poke - 1])
            self.ids.poke.add_widget(button)

    pass


""" 
    This class controls the move buttons on the PokeDex screen
    This needs to be hooked up to the DB with a list of IDs and Names
 """


class MoveDex(BoxLayout):

    def GenerateMoves(self):
        """These two arrays are taking place of reading the data from the DB"""
        # pokeIDList = [0, 1, 2, 3]
        # moveIDList = [10, 11, 12, 13]
        # moveIDName = ["Scratch", "Vise Grip", "Guillotine", "Razor Wind"]
        """The above arrays need to be fixed to access dbs"""

        # for move in pokeIDList:
            # mCard = PokemonCard(moveIDList[move])
            # button = mCard.CreatePokeButton(moveIDList[move], moveIDName[move])
            # self.ids.move.add_widget(button)

        for move in move_list:
            mCard = PokemonCard(move.move_id)
            button = mCard.CreatePokeButton(move.move_id, move.name)
            self.ids.move.add_widget(button)

    pass


""" 
    This class controls the item buttons on the PokeDex screen
    This needs to be hooked up to the DB with a list of IDs and Names
 """


class ItemDex(BoxLayout):

    def GenerateItems(self):
        """These two arrays are taking place of reading the data from the DB"""
        itemIDList = get_item_id_list()
        itemIDName = get_item_name_list()
        """The above arrays need to be fixed to access dbs"""

        i = 0
        for item in itemIDList:
            iCard = PokemonCard(itemIDList[i])
            button = iCard.CreatePokeButton(itemIDList[i], itemIDName[i])
            self.ids.item.add_widget(button)
            i += 1

    pass


""" 
    This class controls the team buttons on the PokeDex screen
    This needs to be hooked up to where the team info is being stored
"""


class Trainer(BoxLayout):

    def GenerateTeam(self):
        pokeIDList = ContentNavigationDrawer.pokeTeam.get_team_id_list()
        pokeIDName = ContentNavigationDrawer.pokeTeam.get_team_name_list()

        for i in range(len(pokeIDList)):
            if pokeIDList[i] is not 0:
                pCard = PokemonCard(pokeIDList[i])
                button = pCard.CreatePokeButton(pokeIDList[i], pokeIDName[i])
                self.ids.trainer.add_widget(button)
            i += 1

    pass


class PokePrimerApp(MDApp):

    def build(self):
        return Builder.load_file("main.kv")


PokePrimerApp().run()
