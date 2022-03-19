from kivy.uix.label import Label
import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from functools import partial
# import sys
# sys.path.append('/Poke-Primer/')
import os

from MoveDex.code.scripts import move_list as MoveDex_move_list
from Trainer.classes import Team
from Trainer.scripts import all_pokemon_id_list, all_pokemon_name_list

from card import Card

from ItemDex.scripts import get_item_id_list, get_item_name_list

ROOT_DIR = os.path.split(os.path.dirname(__file__))[0] + "\\"

LabelBase.register(name='PokeFont',
                   fn_regular=ROOT_DIR + 'Pokemon Classic.ttf')
Window.size = (350, 700)

""" 
    This class creates a card for each pokemon/move/item that stores its id
    It generates a button for the asset to be displayed on the appropriate screen
    When the button is clicked, it creates a popup displaying the details about the asset
    Note: Nothing in here should need to be touched to connect to DBs
 """


class PokemonCard(BoxLayout):
    def __init__(self, id):
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
        full_button = BoxLayout(orientation='horizontal',
                                size_hint=(None, None), height=50)
        lbl_number = Label(text=str(poke_id), font_size=18,
                           size_hint=(None, None), size=(60, 40),
                           pos_hint={'x': .1}, font_name="PokeFont",
                           color=(.17, .23, .2, 1))
        button = Button(text=poke_name, size_hint=(None, None), size=(220, 40),
                        pos_hint={'x': .1},
                        background_normal=ROOT_DIR + 'dark_bg.jpg',
                        background_down=ROOT_DIR + 'light_bg.jpg',
                        color=(.64, .72, .66, 1), font_name="PokeFont")
        button.bind(on_release=partial(self.GetCardData))
        ball_button = Button(background_normal=ROOT_DIR + 'icon_ball.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
        full_button.add_widget(lbl_number)
        full_button.add_widget(button)
        full_button.add_widget(ball_button)
        return full_button

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
        pokeIDList = all_pokemon_id_list()
        pokeIDName = all_pokemon_name_list()
        """The above arrays need to be fixed to access dbs"""

        for poke in pokeIDList:
            pCard = PokemonCard(poke)
            full_button = pCard.CreatePokeButton(poke, pokeIDName[poke])
            self.ids.poke_grid.add_widget(full_button)

    pass


""" 
    This class controls the move buttons on the MoveDex screen
 """


class MoveDex(BoxLayout):

    def GenerateMoves(self):

        for move in MoveDex_move_list:
            mCard = PokemonCard(move.move_id)  # n + 1?
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

        i = 0
        for i in range(len(pokeIDList)):
            if pokeIDList[i] is not 0:
                pCard = PokemonCard(pokeIDList[i])
                button = pCard.CreatePokeButton(pokeIDList[i], pokeIDName[i])
                self.ids.trainer.add_widget(button)
            i += 1

    pass


class PokePrimerApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file("main.kv")


PokePrimerApp().run()
