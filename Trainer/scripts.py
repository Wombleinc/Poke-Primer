# Christopher Duke
# Trainer/scripts.py
import csv
import os
import pandas

POKEDEX_SIZE = 10


def get_pokemon_id_list():
    """
    :return: list of all pokemon in the defined pokedex range by id
    """
    pokemon_data_frame = load_pokemon_data()
    pokemon_id_list = []
    i = 0
    for i in range(POKEDEX_SIZE):
        pokemon_id_list.append(pokemon_data_frame.get("id")[i])
        i += 1
    return pokemon_id_list


def get_pokemon_name_list():
    """
    :return: list of all pokemon in the defined pokedex range by name
    """
    pokemon_data_frame = load_pokemon_data()
    pokemon_name_list = []
    i = 0
    for i in range(POKEDEX_SIZE):
        pokemon_name_list.append(pokemon_data_frame.get("name")[i])
        i += 1
    return pokemon_name_list


def load_pokemon_data():
    """
    :return: a data frame of pokemon information to be read.
             This data is read from \PokemonData\Pokemon_edit.csv
    """
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # Define dataset path in reference to the root path
    DATASET_PATH = os.path.join(ROOT_DIR, '..\\PokemonData\\Pokemon_edit.csv')

    # Read in dataset
    return pandas.read_csv(DATASET_PATH)


def save_team_to_csv(pokemon_team):
    """
    :param pokemon_team: The user's pokemon team
    :return: Nothing, but a csv file is saved at \Trainer\team.csv with the user's pokemon team info
    """
    header = ['#', 'ID', 'Pokemon', 'Held Item', 'Move 1', 'Move 2', 'Move 3', 'Move 4']

    with open('..\\Trainer\\team.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for count, pokemon in enumerate(pokemon_team.members):
            writer.writerow([count + 1, pokemon.get_id(), pokemon.get_name(), pokemon.get_item(),
                             pokemon.get_move1(), pokemon.get_move2(), pokemon.get_move3(), pokemon.get_move4()])
