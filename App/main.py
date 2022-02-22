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

from card import Card

Window.clearcolor = (1, 1, 1, 1)
Window.size = (540, 1140)

class PokemonCard(BoxLayout):
    def __init__(self, id):
        self.id = id
 
    
    def GetCardData(self, id):
        myCard = Card(id)
        content = BoxLayout(orientation="vertical")
        self.popup = Popup(title=myCard.name, size_hint=(None, None),
                           size=(400, 400), auto_dismiss=False, content=content)
        numberLabel = Label(text=myCard.number)
        nameLabel = Label(text=myCard.name)
        descLabel = Label(text=myCard.description)
        """This is the line that would add to trainer"""
        button = Button(text="Add")
        close_btn = Button(text="Close", on_press=self.popup.dismiss)
        content.add_widget(numberLabel)
        content.add_widget(nameLabel)
        content.add_widget(descLabel)
        content.add_widget(button)
        content.add_widget(close_btn)
        self.popup.open()

    def CreatePokeButton(self, poke_id):
        self.id = poke_id
        content = BoxLayout(orientation="vertical")
        button = Button(text=str(self.id))
        content.add_widget(button)
    def method(self, number):
        self.label.text = str(number)
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class CardPopUp(Popup):
    
    pass

class PokeDex(BoxLayout):
    
    def GeneratePokemon(self):
        pokeList = [1,2,3]
        for poke in pokeList:
            content = BoxLayout(orientation="vertical")
            button = Button(text=str(poke))
            content.add_widget(button)
            print(poke)
    pass


class PokePrimerApp(MDApp):
    
    def build(self):
        return Builder.load_file("main.kv")



PokePrimerApp().run()