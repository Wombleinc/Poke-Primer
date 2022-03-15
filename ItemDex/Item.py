import request_item
import requests
import json


def request_data(url):
    urlResult = requests.get(url)
    urlResult = urlResult.text
    pokeApiData = json.loads(urlResult)
    return pokeApiData


class Item:

    def __init__(self, id):
        self.id = request_item.get_item_id(id)
        self.name = request_item.get_item_name(id)
        self.cost = request_item.get_item_cost(id)
        self.attribute_list = request_item.get_item_attribute_list(id)
        self.category = request_item.get_item_category(id)
        self.effect = request_item.get_item_effect(id)
        self.generation = request_item.get_item_generation(id)
        self.sprite_url = request_item.get_item_sprite_url(id)

    #def __init__(self, url):
    #    self.id = request_item.get_item_id(url)
    #    self.name = request_item.get_item_name(url)
    #    self.fancy_name = request_item.get_item_fancy_name(url)
    #    self.cost = request_item.get_item_cost(url)
    #    self.attribute_list = request_item.get_item_attribute_list(url)
    #    self.category = request_item.get_item_category(url)
    #    self.effect = request_item.get_item_effect(url)
    #    self.game_indices = request_item.get_item_game_indices(url)
    #    self.sprite_url = request_item.get_item_sprite_url(url)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_attribute_list(self):
        return self.attribute_list

    def get_category(self):
        return self.category

    def get_effect(self):
        return self.effect

    def get_generation(self):
        return self.generation

    def get_sprite_url(self):
        return self.sprite_url

    def __str__(self):
        return f"ID: {self.get_id()}\nName: {self.get_name()}\n" \
               f"Cost: {self.get_cost()}\nAttribute List: {self.get_attribute_list()}\nCategory: {self.get_category()}\n" \
               f"Effect: {self.get_effect()}\nGeneration: {self.get_generation()}\nSprite URL: {self.get_sprite_url()}\n"
