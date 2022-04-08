from kivy.uix.label import Label
import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from functools import partial
import sys

from numpy import spacing
sys.path.append('/Poke-Primer-main/')
from MoveDex.code.scripts import get_move_id_list, get_move_name_list, get_move_type_list

import os

from Trainer.classes import Team
from Trainer.scripts import all_pokemon_id_list, all_pokemon_name_list

from card import CardPokemon
from card import CardItem
from card import CardMove

from ItemDex.scripts import get_item_id_name_cat_list

ROOT_DIR = os.path.split(os.path.dirname(__file__))[0] + "\\"

LabelBase.register(name='PokeFont',
                   fn_regular=ROOT_DIR + 'Pokemon Classic.ttf')
Window.size = (350, 700)

class MoveCard(BoxLayout):
    def __init__(self, id):
        self.id = id
        
    def GetCardMoveData(self, *args):
        print(self.id)
        myCard = CardMove(self.id)
        move = MDBoxLayout(orientation="horizontal")
        buttons = MDBoxLayout(orientation="horizontal")
        content = MDBoxLayout(orientation="vertical")
        self.popup = Popup(title=myCard.number + " " +myCard.name,
                        size_hint=(None, None),
                        size=(350,500),
                        auto_dismiss=False,
                        content=content,
                        background = 'light_bg.jpg',
                        title_color=(.17, .23, .2, 1),
                        title_font="PokeFont",
                        title_size="18",
                        separator_color=(.17, .23, .2, 1),
                        separator_height=4)

        descLabel = Label(text=myCard.description,
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont")
        image = Image(source='poke01.png',
                        height=50,
                        allow_stretch=True)
        button = Button(text="Add",
                    size_hint=(.3, .2),
                    size=(50,50),
                    background_normal= 'dark_bg.jpg',
                    background_down= 'light_bg.jpg',
                    color=(.64, .72, .66, 1),
                    font_name="PokeFont")
        button.bind(on_release=partial(self.AddToTrainer))
        close_btn = Button(text="Close", on_press=self.popup.dismiss,
                        size_hint=(.3, .2),
                        background_normal= 'dark_bg.jpg',
                        background_down= 'light_bg.jpg',
                        color=(.64, .72, .66, 1),
                        font_name="PokeFont")
        move.add_widget(image)
        move.add_widget(descLabel)
        content.add_widget(move)
        buttons.add_widget(button)
        buttons.add_widget(close_btn)
        content.add_widget(buttons)
        self.popup.open()

    def CreateMoveButton(self, move_id, move_name):
        self.id = move_id
        full_button = BoxLayout(orientation='horizontal',
                                size_hint=(None, None), height=50)
        lbl_number = Label(text=str(move_id), font_size=18,
                           size_hint=(None, None), size=(60, 40),
                           pos_hint={'x': .1}, font_name="PokeFont",
                           color=(.17, .23, .2, 1))
        button = Button(text=move_name, size_hint=(None, None), size=(220, 40),
                        pos_hint={'x': .1},
                        background_normal=ROOT_DIR + 'dark_bg.jpg',
                        background_down=ROOT_DIR + 'light_bg.jpg',
                        color=(.64, .72, .66, 1), font_name="PokeFont")
        button.bind(on_release=partial(self.GetCardPokemonData))
        self.ball_button = Button(background_normal='icon_move.png',
                            background_down='icon_move_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
        self.ball_button.bind(on_release=self.AddToTrainer)
        full_button.add_widget(lbl_number)
        full_button.add_widget(button)
        full_button.add_widget(self.ball_button)
        return full_button

    def AddToTrainer(self, *args):
        self.ball_button.background_normal='icon_move_added.png'
        self.ball_button.background_down='icon_move_added_down.png'
        self.ball_button.unbind(on_release=self.AddToTrainer)
        self.ball_button.bind(on_release=self.RemoveFromTrainer)
      
        # This function now saves teams to json instead of csv
        ContentNavigationDrawer.pokeTeam.add_from_id_to_team(self.id)
        ContentNavigationDrawer.pokeTeam.save_team_to_json()

    def RemoveFromTrainer(self, *args):
        self.ball_button.background_normal='icon_move.png'
        self.ball_button.background_down='icon_move_down.png'
        self.ball_button.unbind(on_release=self.RemoveFromTrainer)
        self.ball_button.bind(on_release=self.AddToTrainer)

class ItemCard(BoxLayout):
    def __init__(self, id):
        self.id = id

    def GetCardItemData(self, *args):
            print(self.id)
            myCard = CardItem(self.id)
            item = MDBoxLayout(orientation="horizontal")
            buttons = MDBoxLayout(orientation="horizontal",padding = 10, spacing = 20)
            content = MDBoxLayout(orientation="vertical")
            self.popup = Popup(title=myCard.number + " " +myCard.name,
                            size_hint=(None, None),
                            size=(350,500),
                            auto_dismiss=False,
                            content=content,
                            background = 'light_bg.jpg',
                            title_color=(.17, .23, .2, 1),
                            title_font="PokeFont",
                            title_size="18",
                            separator_color=(.17, .23, .2, 1),
                            separator_height=4)

            descLabel = Label(text=myCard.description,
                            color=(.17, .23, .2, 1),
                            text_size=(None, None),
                            size=self.size,
                            font_name="PokeFont")
            add_label = Label(text="Add to Bag:",
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        size_hint=(None, None), size=(150, 40))
            self.ball_button = Button(background_normal='icon_item.png',
                            background_down='icon_item_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.ball_button.bind(on_release=self.AddToTrainer)
            close_btn = Button(text="Close", on_press=self.popup.dismiss,
                        size_hint=(None, None), size=(80, 40),
                        pos=(250, 0),
                        background_normal= 'dark_bg.jpg',
                        background_down= 'light_bg.jpg',
                        color=(.64, .72, .66, 1),
                        font_name="PokeFont")
            item.add_widget(descLabel)
            content.add_widget(item)
            buttons.add_widget(close_btn)
            buttons.add_widget(add_label)
            buttons.add_widget(self.ball_button)
            content.add_widget(buttons)
            self.popup.open()
    def CreateItemButton(self, item_id, item_name, item_category):
        self.id = item_id
        full_button = BoxLayout(orientation='horizontal',
                                size_hint=(None, None), height=50)
        lbl_number = Label(text=str(item_id), font_size=18,
                           size_hint=(None, None), size=(60, 40),
                           pos_hint={'x': .1}, font_name="PokeFont",
                           color=(.17, .23, .2, 1))
        button = Button(text=item_name, size_hint=(None, None), size=(220, 40),
                        pos_hint={'x': .1},
                        background_normal=ROOT_DIR + 'dark_bg.jpg',
                        background_down=ROOT_DIR + 'light_bg.jpg',
                        color=(.64, .72, .66, 1), font_name="PokeFont")
        button.bind(on_release=partial(self.GetCardItemData))
        self.ball_button = Button(background_normal='icon_item.png',
                            background_down='icon_item_down.png',
                            size_hint=(None, None), size=(40, 40),
                            pos=(50, 0), border=(0, 0, 0, 0))
        self.ball_button.bind(on_release=self.AddToTrainer)
        full_button.add_widget(lbl_number)
        full_button.add_widget(button)
        full_button.add_widget(self.ball_button)
        return full_button

    def AddToTrainer(self, *args):
        self.ball_button.background_normal='icon_item_added.png'
        self.ball_button.background_down='icon_item_added_down.png'
        self.ball_button.unbind(on_release=self.AddToTrainer)
        self.ball_button.bind(on_release=self.RemoveFromTrainer)
      
        # This function now saves teams to json instead of csv
        ContentNavigationDrawer.pokeTeam.add_from_id_to_team(self.id)
        ContentNavigationDrawer.pokeTeam.save_team_to_json()

    def RemoveFromTrainer(self, *args):
        self.ball_button.background_normal='icon_item.png'
        self.ball_button.background_down='icon_item_down.png'
        self.ball_button.unbind(on_release=self.RemoveFromTrainer)
        self.ball_button.bind(on_release=self.AddToTrainer)


class PokemonCard(BoxLayout):
    def __init__(self, id):
        self.id = id

    def GetCardPokemonData(self, *args):
        print(self.id)
        myCard = CardPokemon(self.id)
        pokemon = MDBoxLayout(orientation="horizontal")
        buttons = MDBoxLayout(orientation="horizontal", padding = 10, spacing = 20)
        content = MDBoxLayout(orientation="vertical")
        self.popup = Popup(title=myCard.number + " " +myCard.name,
                        size_hint=(None, None),
                        size=(350,500),
                        auto_dismiss=False,
                        content=content,
                        background = 'light_bg.jpg',
                        title_color=(.17, .23, .2, 1),
                        title_font="PokeFont",
                        title_size="18",
                        separator_color=(.17, .23, .2, 1),
                        separator_height=4)

        descLabel = Label(text=myCard.description,
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont")
        image = Image(source='poke01.png',
                        height=50,
                        allow_stretch=True)
        add_label = Label(text="Add to Team:",
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        size_hint=(None, None), size=(150, 40))
        self.ball_button = Button(background_normal='icon_ball.png',
                            background_down='icon_ball_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
        self.ball_button.bind(on_release=self.AddToTrainer)
        close_btn = Button(text="Close", on_press=self.popup.dismiss,
                        size_hint=(None, None), size=(80, 40),
                        pos=(250, 0),
                        background_normal= 'dark_bg.jpg',
                        background_down= 'light_bg.jpg',
                        color=(.64, .72, .66, 1),
                        font_name="PokeFont")
        pokemon.add_widget(image)
        pokemon.add_widget(descLabel)
        content.add_widget(pokemon)
        buttons.add_widget(close_btn)
        buttons.add_widget(add_label)
        buttons.add_widget(self.ball_button)
        content.add_widget(buttons)
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
        button.bind(on_release=partial(self.GetCardPokemonData))
        self.ball_button = Button(background_normal='icon_ball.png',
                            background_down='icon_ball_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
        self.ball_button.bind(on_release=self.AddToTrainer)
        full_button.add_widget(lbl_number)
        full_button.add_widget(button)
        full_button.add_widget(self.ball_button)
        return full_button

    def AddToTrainer(self, *args):
        self.ball_button.background_normal='icon_ball_added.png'
        self.ball_button.background_down='icon_ball_added_down.png'
        self.ball_button.unbind(on_release=self.AddToTrainer)
        self.ball_button.bind(on_release=self.RemoveFromTrainer)
      
        # This function now saves teams to json instead of csv
        ContentNavigationDrawer.pokeTeam.add_from_id_to_team(self.id)
        ContentNavigationDrawer.pokeTeam.save_team_to_json()

    def RemoveFromTrainer(self, *args):
        self.ball_button.background_normal='icon_ball.png'
        self.ball_button.background_down='icon_ball_down.png'
        self.ball_button.unbind(on_release=self.RemoveFromTrainer)
        self.ball_button.bind(on_release=self.AddToTrainer)


class PokeDex(BoxLayout):

    def GeneratePokemon(self, sort):
        self.ids.poke_grid.clear_widgets()
        if sort == 0:
            """These two arrays are taking place of reading the data from the DB"""
            pokeIDList = all_pokemon_id_list()
            pokeIDName = all_pokemon_name_list()
            """The above arrays need to be fixed to access dbs"""
        if sort == 1:
            """These two arrays are taking place of reading the data from the DB"""
            pokeIDList = all_pokemon_id_list()
            pokeIDName = all_pokemon_name_list()
            """The above arrays need to be fixed to access dbs"""
        if sort == 2:
            """These two arrays are taking place of reading the data from the DB"""
            pokeIDList = all_pokemon_id_list()
            pokeIDName = all_pokemon_name_list()
            """The above arrays need to be fixed to access dbs"""
        for poke in pokeIDList:
            pCard = PokemonCard(poke)
            full_button = pCard.CreatePokeButton(poke, pokeIDName[poke])
            self.ids.poke_grid.add_widget(full_button)        
    pass


class MoveDex(BoxLayout):

    def GenerateMoves(self, sort):

        if sort == 0:
            move_list = get_move_id_list()

        if sort == 1:
            move_list = get_move_name_list()

        if sort == 2:
            move_list = get_move_type_list()

        for item in move_list:
            iCard = ItemCard(item['id'])
            full_button = iCard.CreateItemButton(item['id'], item['name'], item['category'])
            self.ids.move_grid.add_widget(full_button)

    pass


class ItemDex(BoxLayout):

    def GenerateItems(self, sort):
        self.ids.item_grid.clear_widgets()
        if sort == 0:
            itemIDNameCatList = get_item_id_name_cat_list()
            newList = sorted(itemIDNameCatList, key=lambda i: i['id'])
        if sort == 1:
            itemIDNameCatList = get_item_id_name_cat_list()
            newList = sorted(itemIDNameCatList, key=lambda i: i['name'])
        if sort == 2:
            itemIDNameCatList = get_item_id_name_cat_list()
            newList = sorted(itemIDNameCatList, key=lambda i: i['category'])
        i = 0
        for item in newList:
            iCard = ItemCard(item['id'])
            full_button = iCard.CreateItemButton(item['id'], item['name'], item['category'])
            self.ids.item_grid.add_widget(full_button)

    pass


class Trainer(BoxLayout):

    def GenerateTeam(self):
        pokeIDList = ContentNavigationDrawer.pokeTeam.get_team_id_list()
        pokeIDName = ContentNavigationDrawer.pokeTeam.get_team_name_list()
        self.ids.trainer_grid.clear_widgets()
        i = 0
        for i in range(len(pokeIDList)):
            if pokeIDList[i] is not 0:
                pCard = PokemonCard(pokeIDList[i])
                button = pCard.CreatePokeButton(pokeIDList[i], pokeIDName[i])
                self.ids.trainer_grid.add_widget(button)
            i += 1

    pass


class ContentNavigationDrawer(BoxLayout):
    pokeTeam = Team()
    pass


class PokePrimerApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file("main.kv")


PokePrimerApp().run()
