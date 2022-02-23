from kivy.uix.label import Label
import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.core.window import Window
from functools import partial

from card import Card

Window.clearcolor = (1, 1, 1, 1)
Window.size = (540, 1140)

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
                           size=(400, 400), auto_dismiss=False, content=content)
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
        button = Button(text=str(poke_id) + " " + poke_name, size_hint=(.95, None), size=(100,40), pos_hint={'center_x': .5})
        button.bind(on_release=partial(self.GetCardData))
        return button

    def AddToTrainer(self, *args):
        print (self.id)

class ContentNavigationDrawer(BoxLayout):
    pass

""" 
    This class controls the pokemon buttons on the PokeDex screen
    This needs to be hooked up to the DB with a list of IDs and Names
 """
class PokeDex(BoxLayout):
    
    def GeneratePokemon(self):
        
        """These two arrays are taking place of reading the data from the DB"""
        pokeIDList = [0,1,2,3]
        pokeIDName = ["MissingNo", "Bulbasaur", "Ivysaur", "Venusaur"]
        """The above arrays need to be fixed to access dbs"""

        for poke in pokeIDList:
            pCard = PokemonCard(poke)
            button =pCard.CreatePokeButton(poke, pokeIDName[poke])
            self.ids.poke.add_widget(button)
    pass

""" 
    This class controls the move buttons on the PokeDex screen
    This needs to be hooked up to the DB with a list of IDs and Names
 """
class MoveDex(BoxLayout):
    
    def GenerateMoves(self):

        """These two arrays are taking place of reading the data from the DB"""
        pokeIDList = [0,1,2,3]
        moveIDList = [10,11,12,13]
        moveIDName = ["Scratch", "Vise Grip", "Guillotine", "Razor Wind"]
        """The above arrays need to be fixed to access dbs"""

        for move in pokeIDList:
            mCard = PokemonCard(moveIDList[move])
            button =mCard.CreatePokeButton(moveIDList[move], moveIDName[move])
            self.ids.move.add_widget(button)
    pass

""" 
    This class controls the item buttons on the PokeDex screen
    This needs to be hooked up to the DB with a list of IDs and Names
 """
class ItemDex(BoxLayout):
    
    def GenerateItems(self):
        
        """These two arrays are taking place of reading the data from the DB"""
        pokeIDList = [0,1,2,3]
        itemIDList = [4,5,6,7]
        itemIDName = ["Poke Ball", "Town Map", "Bicycle", "??????"]
        """The above arrays need to be fixed to access dbs"""

        for item in pokeIDList:
            iCard = PokemonCard(itemIDList[item])
            button =iCard.CreatePokeButton(itemIDList[item], itemIDName[item])
            self.ids.item.add_widget(button)
    pass

""" 
    This class controls the team buttons on the PokeDex screen
    This needs to be hooked up to where the team info is being stored
 """
class Trainer(BoxLayout):
    
    def GenerateTeam(self):

        """These two arrays are taking place of reading the data from the DB"""
        pokeIDList = [0,1,2,3]
        pokeIDName = ["MissingNo", "Bulbasaur", "Ivysaur", "Venusaur"]
        """The above arrays need to be fixed to access dbs"""

        for poke in pokeIDList:
            pCard = PokemonCard(poke)
            button =pCard.CreatePokeButton(poke, pokeIDName[poke])
            self.ids.trainer.add_widget(button)

    pass

class PokePrimerApp(MDApp):
    
    def build(self):
        return Builder.load_file("main.kv")



PokePrimerApp().run()