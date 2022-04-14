from kivy.uix.label import Label
import kivy
from kivy.lang import Builder
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.core.window import Window
from functools import partial
import sys

from numpy import spacing
sys.path.append('/Poke-Primer-main/')
import os

from MoveDex.code.scripts import get_move_id_list, get_move_name_list, get_move_sorting_list, get_move_type_list
from Trainer.classes import Team, TrainerBag, TrainerMoves, all_pokemon_name_list
from Trainer.scripts import all_pokemon_id_list, get_pokemon_sorting_list

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
    def FormatStats(self, p, a, t, c, pp):
        return "Power: "+str(p)+"\nAccuracy: "+str(a)+"\nType: "+str(t)+"\nCategory: "+str(c)+"\nPower Points: "+str(pp)  
    
    def GetCardMoveData(self, *args):
        myCard = CardMove(self.id)
        move = GridLayout(cols=1,padding = 20, spacing = 20)
        buttons = BoxLayout(orientation="horizontal", padding = 5, spacing = 30)
        content = BoxLayout(orientation="vertical")
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

        descLabel = Label(text=MoveCard.FormatStats(self,myCard.power, myCard.accuracy, myCard.type, myCard.category,myCard.pp),
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont")
        image = AsyncImage(source=myCard.sprite_url,
                        height=50,
                        allow_stretch=True)
        if Trainer.check_for_added(self.id, 2):
            add_label = Label(text="On Shelf:",
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        size_hint=(None, .5), size=(150, 40))
            self.card_ball_button = Button(background_normal='icon_move_added.png',
                            background_down='icon_move_added_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.card_ball_button.bind(on_release=self.RemoveFromTrainer)
        else:
            add_label = Label(text="Add to Shelf:",
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        size_hint=(None, None), size=(150, 40))
            self.card_ball_button = Button(background_normal='icon_move.png',
                            background_down='icon_move_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.card_ball_button.bind(on_release=self.AddToTrainer)
        close_btn = Button(text="Close", on_press=self.popup.dismiss,
                        size_hint=(None, None), size=(80, 40),
                        pos=(250, 0),
                        background_normal= 'dark_bg.jpg',
                        background_down= 'light_bg.jpg',
                        color=(.64, .72, .66, 1),
                        font_name="PokeFont")
        move.add_widget(image)
        move.add_widget(descLabel)
        content.add_widget(move)
        buttons.add_widget(close_btn)
        buttons.add_widget(add_label)
        buttons.add_widget(self.card_ball_button)
        content.add_widget(buttons)
        self.popup.open()

    def CreateMoveButton(self, move_id, move_name, move_type, owned):
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
        button.bind(on_release=partial(self.GetCardMoveData))
        if owned:
            self.ball_button = Button(background_normal='icon_move_added.png',
                            background_down='icon_move_added_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
        else:
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

        Trainer.trainerMoves.add_move(self.id)
        Trainer.trainerMoves.save_moves_to_json()

    def RemoveFromTrainer(self, *args):
        self.ball_button.background_normal='icon_move.png'
        self.ball_button.background_down='icon_move_down.png'
        self.ball_button.unbind(on_release=self.RemoveFromTrainer)
        self.ball_button.bind(on_release=self.AddToTrainer)

        Trainer.trainerMoves.remove_move(self.id)
        Trainer.trainerMoves.save_moves_to_json()

class ItemCard(BoxLayout):
    def __init__(self, id):
        self.id = id

    def FixIcons(self, i):
        item_buttons = poke_app.main_sm.get_screen("main").ids.info_sm.get_screen("item").ids.item_grid.children
        for item in item_buttons:
            for part in item.children:
                if part.text == str(i):
                    found_item_button = item
                    break
        inBag = Trainer.check_for_added(i, 3)
        for part in found_item_button.children:
            if part.__class__.__name__ == "Button":
                if inBag:   
                    if part.background_normal =='icon_item.png':
                        part.background_normal='icon_item_added.png'
                        part.background_down='icon_item_added_down.png'
                        part.unbind(on_release=self.AddToTrainer)
                        part.bind(on_release=self.RemoveFromTrainer)
                else:
                    if part.background_normal =='icon_item_added.png':
                        part.background_normal='icon_item.png'
                        part.background_down='icon_item_down.png'
                        part.unbind(on_release=self.RemoveFromTrainer)
                        part.bind(on_release=self.AddToTrainer)

    def FormatDesc(self, desc):
        formatted = ""
        for i, letter in enumerate(desc):
            if letter != "\n":
                if i % 22 == 0:
                    formatted += '\n'
                formatted += letter
        return formatted
    
    def GetCardItemData(self, *args):
            myCard = CardItem(self.id)
            item = GridLayout(cols=1,padding = 20, spacing = 50)
            buttons = BoxLayout(orientation="horizontal",padding = 10, spacing = 20)
            content = BoxLayout(orientation="vertical")
            self.popup = Popup(title=myCard.number + " " +myCard.name,
                            size_hint=(None, None),
                            size=(400,800),
                            auto_dismiss=False,
                            content=content,
                            background = 'light_bg.jpg',
                            title_color=(.17, .23, .2, 1),
                            title_font="PokeFont",
                            title_size="18",
                            separator_color=(.17, .23, .2, 1),
                            separator_height=4)
            self.popup.bind(on_dismiss=lambda x: self.FixIcons(self.id))
            catLabel = Label(text=myCard.category,
                            size_hint=(None, None),
                            color=(.17, .23, .2, 1),
                            font_name="PokeFont",
                            font_size=24,
                            width=380)
            descLabel = Label(text=ItemCard.FormatDesc(self,myCard.description),
                            size_hint=(None, None),
                            pos_hint=(None, .5),
                            color=(.17, .23, .2, 1),
                            font_name="PokeFont",
                            font_size=18,
                            width=380)
            image = AsyncImage(source=myCard.sprite_url,
                        pos=(0,10),
                        size_hint_y=None,
                        width=500,
                        allow_stretch=True,
                        keep_ratio=True)
            if Trainer.check_for_added(self.id, 3):
                add_label = Label(text="In Bag:",
                            color=(.17, .23, .2, 1),
                            font_name="PokeFont",
                            size_hint=(None, None), size=(150, 40))
                self.card_ball_button = Button(background_normal='icon_item_added.png',
                                background_down='icon_item_added_down.png',
                                size_hint=(None, None), size=(40, 40),
                                pos=(50, 0), border=(0, 0, 0, 0))
                self.card_ball_button.bind(on_release=self.RemoveFromTrainer)
            else:
                add_label = Label(text="Add to Bag:",
                            color=(.17, .23, .2, 1),
                            font_name="PokeFont",
                            size_hint=(None, None), size=(150, 40))
                self.card_ball_button = Button(background_normal='icon_item.png',
                                background_down='icon_item_down.png',
                                size_hint=(None, None), size=(40, 40),
                                pos=(50, 0), border=(0, 0, 0, 0))
                self.card_ball_button.bind(on_release=self.AddToTrainer)
            close_btn = Button(text="Close", on_press=self.popup.dismiss,
                        size_hint=(None, None), size=(80, 40),
                        pos=(250, 0),
                        background_normal= 'dark_bg.jpg',
                        background_down= 'light_bg.jpg',
                        color=(.64, .72, .66, 1),
                        font_name="PokeFont")
            item.add_widget(image)
            item.add_widget(catLabel)
            item.add_widget(descLabel)
            content.add_widget(item)
            buttons.add_widget(close_btn)
            buttons.add_widget(add_label)
            buttons.add_widget(self.card_ball_button)
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
        if not Trainer.check_for_added(self.id, 3):
            self.ball_button.background_normal='icon_item_added.png'
            self.ball_button.background_down='icon_item_added_down.png'
            self.ball_button.unbind(on_release=self.AddToTrainer)
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
            print("Adding")
        
            # This function now saves teams to json instead of csv
            Trainer.trainerBag.add_item(self.id)
            Trainer.trainerBag.save_bag_to_json()
            print(Trainer.check_for_added(self.id, 3))
        else:
            self.ball_button.background_normal='icon_item.png'
            self.ball_button.background_down='icon_item_down.png'
            self.ball_button.unbind(on_release=self.RemoveFromTrainer)
            self.ball_button.bind(on_release=self.AddToTrainer)
            print("Removing")
            
            Trainer.trainerBag.remove_item(self.id)
            Trainer.trainerBag.save_bag_to_json()
            print(Trainer.check_for_added(self.id, 3))
    def RemoveFromTrainer(self, *args):
        if Trainer.check_for_added(self.id, 3):
            self.ball_button.background_normal='icon_item.png'
            self.ball_button.background_down='icon_item_down.png'
            self.ball_button.unbind(on_release=self.RemoveFromTrainer)
            self.ball_button.bind(on_release=self.AddToTrainer)
            print("Removing")
            
            Trainer.trainerBag.remove_item(self.id)
            Trainer.trainerBag.save_bag_to_json()
            print(Trainer.check_for_added(self.id, 3))
        else:

            self.ball_button.background_normal='icon_item_added.png'
            self.ball_button.background_down='icon_item_added_down.png'
            self.ball_button.unbind(on_release=self.AddToTrainer)
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
            print("Adding")
        
            # This function now saves teams to json instead of csv
            Trainer.trainerBag.add_item(self.id)
            Trainer.trainerBag.save_bag_to_json()
            print(Trainer.check_for_added(self.id, 3))

class PokemonCard(BoxLayout):
    def __init__(self, id):
        self.id = id

    def FixIcons(self, pokemon):
        poke_buttons = poke_app.main_sm.get_screen("main").ids.info_sm.get_screen("poke").ids.poke_grid.children
        for poke in poke_buttons:
            for part in poke.children:
                if part.text == str(pokemon):
                    found_poke_button = poke
                    break 
        inTeam = Trainer.check_for_added(pokemon, 1)
        for part in found_poke_button.children:
            if part.__class__.__name__ == "Button":
                if inTeam:   
                    if part.background_normal =='icon_ball.png':
                        part.background_normal='icon_ball_added.png'
                        part.background_down='icon_ball_added_down.png'
                        part.unbind(on_release=self.AddToTrainer)
                        part.bind(on_release=self.RemoveFromTrainer)
                else:
                    if part.background_normal =='icon_ball_added.png':
                        part.background_normal='icon_ball.png'
                        part.background_down='icon_ball_down.png'
                        part.unbind(on_release=self.RemoveFromTrainer)
                        part.bind(on_release=self.AddToTrainer)

    def FormatStats(self, hp, at, de, sa, sd, sp):
        return "HP: "+str(hp)+"\nAttack: "+str(at)+"\nDefense: "+str(de)+"\nSp.Attack: "+str(sa)+"\nSp.Defense: "+str(sd)+"\nSpeed: "+str(sp)
    
    def GetCardPokemonData(self, *args):
        myCard = CardPokemon(self.id)
        pokemon = GridLayout(cols=1,padding = 20, spacing = 20)
        buttons = BoxLayout(orientation="horizontal", padding = 5, spacing = 30)
        content = BoxLayout(orientation="vertical")
        self.popup = Popup(title=myCard.number + " " +myCard.name,
                        size_hint=(None, None),
                        size=(400,800),
                        auto_dismiss=False,
                        content=content,
                        background = 'light_bg.jpg',
                        title_color=(.17, .23, .2, 1),
                        title_font="PokeFont",
                        title_size="18",
                        separator_color=(.17, .23, .2, 1),
                        separator_height=4)
        self.popup.bind(on_dismiss=lambda x: self.FixIcons(self.id))
        genusLabel = Label(text=myCard.genus,
                        size_hint=(None, None),
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        font_size=24,
                        width=380)
        typeLabel = Label(text=myCard.type_1 + " / "+ myCard.type_2,
                        size_hint=(None, None),
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        font_size=24,
                        width=380)
        statLabel = Label(text=PokemonCard.FormatStats(self, myCard.hp, myCard.attack, myCard.defense, myCard.special_attack, myCard.special_defense, myCard.speed),
                        size_hint=(None, None),
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        font_size=20,
                        width=380)
        genLabel = Label(text="Generation: "+str(myCard.generation),
                        size_hint=(None, None),
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        width=380)
        image = AsyncImage(source=myCard.icon_url,
                        pos=(0,10),
                        size_hint_y=None,
                        width=500,
                        allow_stretch=True,
                        keep_ratio=True)
        if Trainer.check_for_added(self.id, 1):
            add_label = Label(text="In Team:",
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        size_hint=(None, .5), size=(150, 40))
            self.card_ball_button = Button(background_normal='icon_ball_added.png',
                            background_down='icon_ball_added_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.card_ball_button.bind(on_release=self.RemoveFromTrainer)
        else:
            add_label = Label(text="Add to Team:",
                        color=(.17, .23, .2, 1),
                        font_name="PokeFont",
                        size_hint=(None, None), size=(150, 40))
            self.card_ball_button = Button(background_normal='icon_ball.png',
                            background_down='icon_ball_down.png',
                             size_hint=(None, None), size=(40, 40),
                             pos=(50, 0), border=(0, 0, 0, 0))
            self.card_ball_button.bind(on_release=self.AddToTrainer)
        close_btn = Button(text="Close", on_press=self.popup.dismiss,
                        size_hint=(None, None), size=(80, 40),
                        pos=(250, 0),
                        background_normal= 'dark_bg.jpg',
                        background_down= 'light_bg.jpg',
                        color=(.64, .72, .66, 1),
                        font_name="PokeFont")
        pokemon.add_widget(image)
        pokemon.add_widget(genusLabel)
        pokemon.add_widget(typeLabel)
        pokemon.add_widget(statLabel)
        pokemon.add_widget(genLabel)
        content.add_widget(pokemon)
        buttons.add_widget(close_btn)
        buttons.add_widget(add_label)
        buttons.add_widget(self.card_ball_button)
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
        if not Trainer.check_for_added(self.id, 3):
            self.ball_button.background_normal='icon_ball_added.png'
            self.ball_button.background_down='icon_ball_added_down.png'
            self.ball_button.unbind(on_release=self.AddToTrainer)
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
            print("Adding")

            Trainer.trainerTeam.add_from_id_to_team(self.id)
            Trainer.trainerTeam.save_team_to_json()
        else:
            self.ball_button.background_normal='icon_ball.png'
            self.ball_button.background_down='icon_ball_down.png'
            self.ball_button.unbind(on_release=self.RemoveFromTrainer)
            self.ball_button.bind(on_release=self.AddToTrainer)
            print("Removing")
            Trainer.trainerTeam.remove_pokemon(self.id)
            Trainer.trainerTeam.save_team_to_json()
    def RemoveFromTrainer(self, *args):
        if Trainer.check_for_added(self.id, 1):
            self.ball_button.background_normal='icon_ball.png'
            self.ball_button.background_down='icon_ball_down.png'
            self.ball_button.unbind(on_release=self.RemoveFromTrainer)
            self.ball_button.bind(on_release=self.AddToTrainer)
            print("Removing")

            Trainer.trainerTeam.remove_pokemon(self.id)
            Trainer.trainerTeam.save_team_to_json()
        else:

            self.ball_button.background_normal='icon_ball_added.png'
            self.ball_button.background_down='icon_ball_added_down.png'
            self.ball_button.unbind(on_release=self.AddToTrainer)
            self.ball_button.bind(on_release=self.RemoveFromTrainer)
            print("Adding")
            Trainer.trainerTeam.add_from_id_to_team(self.id)
            Trainer.trainerTeam.save_team_to_json()

class PokeDex(Screen):

    def GeneratePokemon(self, sort):
        self.ids.poke_grid.clear_widgets()
        self.ids.num.background_normal = "button_cat_normal.png"
        self.ids.name.background_normal = "button_cat_normal.png"
        self.ids.type.background_normal = "button_cat_normal.png"
        if sort == 0:
            """These two arrays are taking place of reading the data from the DB"""
            poke_sorting_list = get_pokemon_sorting_list()
            poke_sorted_list = sorted(poke_sorting_list, key=lambda i:i['id'])
            self.ids.num.background_normal = "button_cat_sel.png"
            """The above arrays need to be fixed to access dbs"""
        if sort == 1:
            """These two arrays are taking place of reading the data from the DB"""
            poke_sorting_list = get_pokemon_sorting_list()
            poke_sorted_list = sorted(poke_sorting_list, key=lambda i:i['name'])
            self.ids.name.background_normal = "button_cat_sel.png"
            """The above arrays need to be fixed to access dbs"""
        if sort == 2:
            """These two arrays are taking place of reading the data from the DB"""
            poke_sorting_list = get_pokemon_sorting_list()
            poke_sorted_list = sorted(poke_sorting_list, key=lambda i:i['type'])
            self.ids.type.background_normal = "button_cat_sel.png"
            """The above arrays need to be fixed to access dbs"""
        for poke in poke_sorted_list:
            pCard = PokemonCard(poke)
            full_button = pCard.CreatePokeButton(poke['id'], poke['name'], Trainer.check_for_added(poke['id'], 1))
            self.ids.poke_grid.add_widget(full_button)

class MoveDex(Screen):

    def GenerateMoves(self, sort):
        self.ids.move_grid.clear_widgets()
        self.ids.num.background_normal = "button_cat_normal.png"
        self.ids.name.background_normal = "button_cat_normal.png"
        self.ids.type.background_normal = "button_cat_normal.png"
        if sort == 0:
            move_sorting_list = get_move_sorting_list()
            move_sorted_list = sorted(move_sorting_list, key=lambda i:i['id'])
            self.ids.num.background_normal = "button_cat_sel.png"

        if sort == 1:
            move_sorting_list = get_move_sorting_list()
            move_sorted_list = sorted(move_sorting_list, key=lambda i:i['name'])
            self.ids.name.background_normal = "button_cat_sel.png"

        if sort == 2:
            move_sorting_list = get_move_sorting_list()
            move_sorted_list = sorted(move_sorting_list, key=lambda i:i['type'])
            self.ids.type.background_normal = "button_cat_sel.png"

        for move in move_sorted_list:
            mCard = MoveCard(move)
            full_button = mCard.CreateMoveButton(move['id'], move['name'], move['type'], Trainer.check_for_added(move['id'], 2))
            self.ids.move_grid.add_widget(full_button)

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
        for item in newList:
            iCard = ItemCard(item['id'])
            full_button = iCard.CreateItemButton(item['id'], item['name'], item['category'], Trainer.check_for_added(item['id'], 3))
            self.ids.item_grid.add_widget(full_button)

    pass

class Trainer(Screen):

    trainerTeam = Team()
    trainerBag = TrainerBag()
    trainerMoves = TrainerMoves()

    def check_for_added(id, category):
        if category == 1:
            ownedList = Trainer.trainerTeam.get_team_id_list()
        if category == 2:
            ownedList = Trainer.trainerMoves.get_move_id_list()
        if category == 3:
            ownedList = Trainer.trainerBag.get_item_id_list()
        for owned_member in ownedList:
            if owned_member == id:
                return True
        return False
    
    def ResetCatIcons(self):
        self.ids.poke.background_normal = "button_cat_normal.png"
        self.ids.moves.background_normal = "button_cat_normal.png"
        self.ids.item_button.background_normal = "button_cat_normal.png"
    
    def GenerateTeam(self):
        self.ids.trainer_grid.clear_widgets()
        self.ids.poke.background_normal = "button_cat_sel.png"
        pokeIDList = self.trainerTeam.get_team_id_list()
        pokeIDName = self.trainerTeam.get_team_name_list()
        i = 0
        for i in range(len(pokeIDList)):
            if pokeIDList[i] is not 0:
                pCard = PokemonCard(pokeIDList[i])
                button = pCard.CreatePokeButton(pokeIDList[i], pokeIDName[i], True)
                self.ids.trainer_grid.add_widget(button)
            i += 1
    
    def GenerateMoves(self):
        self.ids.trainer_grid.clear_widgets()
        self.ids.moves.background_normal = "button_cat_sel.png"
        
        move_id_list = self.trainerMoves.get_move_id_list()
        move_name_list = self.trainerMoves.get_move_name_list()
        move_type_list = self.trainerMoves.get_move_type_list()
        i = 0
        for i in range(len(move_id_list)):
            mCard = MoveCard(move_id_list[i])
            button = mCard.CreateMoveButton(move_id_list[i], move_name_list[i], move_type_list[i], True)
            self.ids.trainer_grid.add_widget(button)
            i += 1

    def GenerateItems(self):
        self.ids.trainer_grid.clear_widgets()
        self.ids.item_button.background_normal = "button_cat_sel.png"
        
        item_id_list = self.trainerBag.get_item_id_list()
        item_name_list = self.trainerBag.get_item_name_list()
        item_category_list = self.trainerBag.get_item_category_list()
        i = 0
        for i in range(len(item_id_list)):
            iCard = ItemCard(item_id_list[i])
            button = iCard.CreateItemButton(item_id_list[i], item_name_list[i], item_category_list[i], True)
            self.ids.trainer_grid.add_widget(button)
            i += 1

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

    main_sm = ScreenManager()
    def build(self):
        Builder.load_file("main.kv")
        
        self.main_sm.add_widget(MainScreen(name="main"))
        return self.main_sm

poke_app = PokePrimerApp()
poke_app.run()
