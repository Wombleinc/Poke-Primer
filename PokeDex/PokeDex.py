import requests
import json

def request_data(url):
    urlResult = requests.get(url)
    urlResult = urlResult.text
    pokeApiData = json.loads(urlResult)
    return pokeApiData


def all_pokemon_list():
    url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=152'
    data = request_data(url)
    all_pokemon_list = {}
    id_count = 0
    for item in data['results']:
        id_count += 1
        all_pokemon_list[id_count] = item['name']
    return all_pokemon_list


def GetPokemonID():
    pokemon_list = all_pokemon_list()
    n = 0
    i = 0
    while i != 151:
        for i in range(1, 152):
            print(f"ID: {i: <3}")

def GetPokeName():
    pokemon_list = all_pokemon_list()
    n = 0
    i = 0
    while i != 151:
        for i in range(1, 152):
            print(f"Name: {pokemon_list[i].title(): <22}")

GetPokemonID()
GetPokeName()
