from kivy.uix.label import Label
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from functools import partial
import sys

from numpy import spacing
sys.path.append('/Poke-Primer-main/')
import os

from MoveDex.code.scripts import get_move_id_list, get_move_name_list, get_move_type_list
from Trainer.classes import Team, TrainerBag, all_pokemon_name_list
from Trainer.scripts import all_pokemon_id_list

from card import CardPokemon
from card import CardItem
from card import CardMove

from ItemDex.scripts import get_item_id_name_cat_list

ROOT_DIR = os.path.split(os.path.dirname(__file__))[0] + "\\"

LabelBase.register(name='PokeFont',
                   fn_regular=ROOT_DIR + 'Pokemon Classic.ttf')
Window.size = (414, 896)

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

    def CreateItemButton(self, item_id, item_name, item_category, owned):
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
        if owned:
            self.ball_button = Button(background_normal='icon_item_added.png',
                            background_down='icon_item_added_down.png',
                            size_hint=(None, None), size=(40, 40),
                            pos=(50, 0), border=(0, 0, 0, 0))
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
        else:
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
        Trainer.trainerBag.add_item(self.id)
        Trainer.trainerBag.save_bag_to_json()

    def RemoveFromTrainer(self, *args):
        self.ball_button.background_normal='icon_item.png'
        self.ball_button.background_down='icon_item_down.png'
        self.ball_button.unbind(on_release=self.RemoveFromTrainer)
        self.ball_button.bind(on_release=self.AddToTrainer)

        Trainer.trainerBag.remove_item(self.id)
        Trainer.trainerBag.save_bag_to_json()

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

    def CreatePokeButton(self, poke_id, poke_name, inTeam):
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
        
        if inTeam:
            self.ball_button = Button(background_normal='icon_ball_added.png',
                            background_down='icon_ball_added_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
        else:
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

        Trainer.trainerTeam.add_from_id_to_team(self.id)
        Trainer.trainerTeam.save_team_to_json()

    def RemoveFromTrainer(self, *args):
        self.ball_button.background_normal='icon_ball.png'
        self.ball_button.background_down='icon_ball_down.png'
        self.ball_button.unbind(on_release=self.RemoveFromTrainer)
        self.ball_button.bind(on_release=self.AddToTrainer)

        Trainer.trainerTeam.remove_pokemon(self.id)
        Trainer.trainerTeam.save_team_to_json()

class PokeDex(Screen):

    def GeneratePokemon(self, sort):
        self.ids.poke_grid.clear_widgets()
        self.ids.num.background_normal = "button_cat_normal.png"
        self.ids.name.background_normal = "button_cat_normal.png"
        self.ids.type.background_normal = "button_cat_normal.png"
        if sort == 0:
            """These two arrays are taking place of reading the data from the DB"""
            pokeIDList = all_pokemon_id_list()
            pokeIDName = all_pokemon_name_list()
            self.ids.num.background_normal = "button_cat_sel.png"
            """The above arrays need to be fixed to access dbs"""
        if sort == 1:
            """These two arrays are taking place of reading the data from the DB"""
            pokeIDList = all_pokemon_id_list()
            pokeIDName = all_pokemon_name_list()
            self.ids.name.background_normal = "button_cat_sel.png"
            """The above arrays need to be fixed to access dbs"""
        if sort == 2:
            """These two arrays are taking place of reading the data from the DB"""
            pokeIDList = all_pokemon_id_list()
            pokeIDName = all_pokemon_name_list()
            self.ids.type.background_normal = "button_cat_sel.png"
            """The above arrays need to be fixed to access dbs"""
        teamList = Trainer.trainerTeam.get_team_id_list()
        for poke in pokeIDList:
            pCard = PokemonCard(poke)
            full_button = pCard.CreatePokeButton(poke, pokeIDName[poke], Trainer.check_for_added(poke, 1))
            self.ids.poke_grid.add_widget(full_button)

class MoveDex(Screen):

    def GenerateMoves(self, sort):
        self.ids.move_grid.clear_widgets()
        self.ids.num.background_normal = "button_cat_normal.png"
        self.ids.name.background_normal = "button_cat_normal.png"
        self.ids.type.background_normal = "button_cat_normal.png"
        if sort == 0:
            move_list = get_move_id_list()
            self.ids.num.background_normal = "button_cat_sel.png"

        if sort == 1:
            move_list = get_move_name_list()
            self.ids.name.background_normal = "button_cat_sel.png"

        if sort == 2:
            move_list = get_move_type_list()
            self.ids.type.background_normal = "button_cat_sel.png"

        for item in move_list:
            iCard = ItemCard(item['id'])
            full_button = iCard.CreateItemButton(item['id'], item['name'], item['category'])
            self.ids.move_grid.add_widget(full_button)

    pass

class ItemDex(Screen):
    
    def GenerateItems(self, sort):
        self.ids.item_grid.clear_widgets()
        self.ids.num.background_normal = "button_cat_normal.png"
        self.ids.name.background_normal = "button_cat_normal.png"
        self.ids.type.background_normal = "button_cat_normal.png"
        if sort == 0:
            itemIDNameCatList = get_item_id_name_cat_list()
            newList = sorted(itemIDNameCatList, key=lambda i: i['id'])
            self.ids.num.background_normal = "button_cat_sel.png"
        if sort == 1:
            itemIDNameCatList = get_item_id_name_cat_list()
            newList = sorted(itemIDNameCatList, key=lambda i: i['name'])
            self.ids.name.background_normal = "button_cat_sel.png"
        if sort == 2:
            itemIDNameCatList = get_item_id_name_cat_list()
            newList = sorted(itemIDNameCatList, key=lambda i: i['category'])
            self.ids.type.background_normal = "button_cat_sel.png"
        itemList = Trainer.trainerBag.get_item_id_list()
        i = 0
        for item in newList:
            iCard = ItemCard(item['id'])
            full_button = iCard.CreateItemButton(item['id'], item['name'], item['category'], Trainer.check_for_added(item, 3))
            self.ids.item_grid.add_widget(full_button)

    pass


class Trainer(Screen):

    trainerTeam = Team()
    trainerBag = TrainerBag()

    def check_for_added(id, category):
        if category == 1:
            ownedList = Trainer.trainerTeam.get_team_id_list()
        if category == 2:
            ownedList = Trainer.trainerTeam.get_team_id_list()
        if category == 3:
            ownedList = Trainer.trainerBag.get_item_id_list()
        for owned_member in ownedList:
            if owned_member == id:
                return True
        return False
    
    def GenerateTeam(self):
        pokeIDList = self.trainerTeam.get_team_id_list()
        pokeIDName = self.trainerTeam.get_team_name_list()
        self.ids.trainer_grid.clear_widgets()
        i = 0
        for i in range(len(pokeIDList)):
            if pokeIDList[i] is not 0:
                pCard = PokemonCard(pokeIDList[i])
                button = pCard.CreatePokeButton(pokeIDList[i], pokeIDName[i], True)
                self.ids.trainer_grid.add_widget(button)
            i += 1
    
    def GenerateItems(self):
        item_id_list = self.trainerBag.get_item_id_list()
        item_name_list = self.trainerBag.get_item_name_list()
        item_category_list = self.trainerBag.get_item_category_list()
        self.ids.trainer_grid.clear_widgets()
        i = 0
        for i in range(len(item_id_list)):
            mCard = ItemCard(item_id_list[i])
            button = mCard.CreateItemButton(item_id_list[i], item_name_list[i], item_category_list[i], True)
            self.ids.trainer_grid.add_widget(button)
            i += 1

    pass

class NavScreen(Screen):
    def FixMenu(self, screen_choice):    
        self.ids.p.background_normal = "button_nav_normal.png"
        self.ids.m.background_normal = "button_nav_normal.png"
        self.ids.i.background_normal = "button_nav_normal.png"
        self.ids.t.background_normal = "button_nav_trainer.png"
        self.ids.p.background_down = "button_nav_down.png"
        self.ids.m.background_down = "button_nav_down.png"
        self.ids.i.background_down = "button_nav_down.png"
        if screen_choice == 0:
            self.ids.p.background_normal = "button_nav_sel.png"
            self.ids.p.background_down = "button_nav_sel_down.png"

        if screen_choice == 1:
            self.ids.m.background_normal = "button_nav_sel.png"
            self.ids.m.background_down = "button_nav_sel_down.png"

        if screen_choice == 2:
            self.ids.i.background_normal = "button_nav_sel.png"
            self.ids.i.background_down = "button_nav_sel_down.png"

        if screen_choice == 3:
            self.ids.t.background_normal = "button_nav_train_sel.png"


class MainScreen(Screen):  
    def ButtonClick(self, screen_choice):

        if screen_choice == 0:
            self.ids.info_sm.current = "poke"

        if screen_choice == 1:
            self.ids.info_sm.current = "move"

        if screen_choice == 2:
            self.ids.info_sm.current = "item"

        if screen_choice == 3:
            self.ids.info_sm.current = "trainer"

class ScreenManagement(ScreenManager):
    pass
class PokePrimerApp(App):

    def build(self):
        Builder.load_file("main.kv")
        main_sm = ScreenManager()
        main_sm.add_widget(MainScreen(name="main"))
        return main_sm

poke_app = PokePrimerApp()
poke_app.run()
