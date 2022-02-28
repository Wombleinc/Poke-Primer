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
        pokemon_values = all_pokemon_list.values()
        poke_values_list = list(pokemon_values)
    return poke_values_list


def GetPokemonID():
    pokemon_list = []
    for i in range(1, 152):
        pokemon_list.append(i)
    return pokemon_list
