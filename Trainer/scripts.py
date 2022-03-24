# Christopher Duke
# Trainer/scripts.py
import requests
import json
import sys
sys.path.append('/Poke-Primer-main/')

POKEDEX_SIZE = 10


def request_data(url):
    urlResult = requests.get(url)
    urlResult = urlResult.text
    pokeApiData = json.loads(urlResult)
    return pokeApiData


def get_pokemon_name(pokemon_id):
    index = pokemon_id - 1
    pokemon_data = load_pokemon_data()

    return pokemon_data['pokemon'][index]['Name']


def get_pokemon_genus(pokemon_id):
    index = pokemon_id - 1
    pokemon_data = load_pokemon_data()

    return pokemon_data['pokemon'][index]['Genus']


def all_pokemon_name_list():
    pokemon_data = load_pokemon_data()
    all_pokemon_list = {}

    for count, pokemon in enumerate(pokemon_data['pokemon']):
        if count < POKEDEX_SIZE:
            all_pokemon_list[count + 1] = pokemon_data['pokemon'][count]['Name']
        else:
            pass

    return all_pokemon_list


def all_pokemon_id_list():
    pokemon_data = load_pokemon_data()

    all_pokemon_list = {}

    for i in range(len(pokemon_data['pokemon'])):
        if i < POKEDEX_SIZE:
            all_pokemon_list[i + 1] = i + 1
        else:
            pass

    return all_pokemon_list


def load_pokemon_data():
    """
    :return: a json file of pokemon information to be read.
             This data is read from \PokemonData\pokemon_data.json
    """
    with open("PokemonData/pokemon_data.json", "r") as json_file:
        pokemon_data = json.load(json_file)

    return pokemon_data
