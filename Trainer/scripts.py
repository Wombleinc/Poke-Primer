# Christopher Duke
# Trainer/scripts.py
import requests
import json
import os
ROOT_DIR = os.path.split(os.path.dirname(__file__))[0] + "\\"

POKEDEX_SIZE = 151


def request_data(url):
    urlResult = requests.get(url)
    urlResult = urlResult.text
    pokeApiData = json.loads(urlResult)
    return pokeApiData


def get_pokemon_name(pokemon_id):
    index = pokemon_id - 1
    pokemon_data = load_pokemon_data()

    return pokemon_data['pokemon'][index]['Name']


def get_pokemon_info(pokemon_id):
    index = pokemon_id - 1
    pokemon_data = load_pokemon_data()

    info_dict = {
        "Name": pokemon_data['pokemon'][index]['Name'],
        "Genus": pokemon_data['pokemon'][index]['Genus'],
        "Type 1": pokemon_data['pokemon'][index]['Type 1'],
        "Type 2": pokemon_data['pokemon'][index]['Type 2'],
        "HP": pokemon_data['pokemon'][index]['HP'],
        "Attack": pokemon_data['pokemon'][index]['Attack'],
        "Defense": pokemon_data['pokemon'][index]['Defense'],
        "Special Attack": pokemon_data['pokemon'][index]['Special Attack'],
        "Special Defense": pokemon_data['pokemon'][index]['Special Defense'],
        "Speed": pokemon_data['pokemon'][index]['Speed'],
        "Generation": pokemon_data['pokemon'][index]['Generation'],
    }

    return info_dict


def get_pokemon_sorting_list():
    poke_data = load_pokemon_data()

    poke_dict = {}

    poke_sorting_list = []
    for pokemon in range(POKEDEX_SIZE):
        poke_sorting_list.append(dict(
            id=poke_data['pokemon'][pokemon]['ID'],
            name=poke_data['pokemon'][pokemon]['Name'],
            type=poke_data['pokemon'][pokemon]['Type 1']
            )
        )
    
    return poke_sorting_list


def get_pokemon_icon_url(pokemon_id):
    poke_data = request_data('https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id))

    poke_icon_url = poke_data['sprites']['versions']['generation-vii']['icons']['front_default']

    return poke_icon_url


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
    with open(ROOT_DIR + "PokemonData\\pokemon_data.json", "r", encoding='utf-8') as json_file:
        pokemon_data = json.load(json_file, )

    return pokemon_data
