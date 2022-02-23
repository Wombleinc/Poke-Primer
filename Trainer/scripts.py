# Christopher Duke
# TeamDex/scripts.py

import csv
import os
import pandas
from Trainer.classes import Pokemon
from Trainer.classes import Team


def save_team_to_csv(pokemon_team):
    header = ['#', 'Pokemon', 'Held Item', 'Move 1', 'Move 2', 'Move 3', 'Move 4']

    with open('Trainer\\team.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for count, pokemon in enumerate(pokemon_team.members):
            writer.writerow([count + 1, pokemon.get_name(), pokemon.get_item(),
                             pokemon.get_move1(), pokemon.get_move2(), pokemon.get_move3(), pokemon.get_move4()])


def load_pokemon_data():
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    # Define dataset path in reference to the root path
    DATASET_PATH = os.path.join(ROOT_DIR, '..\\assets\\Pokemon_edit.csv')

    # Read in dataset
    return pandas.read_csv(DATASET_PATH)


def create_pokemon_from_id(pokemon_id):
    pokemon_data_frame = load_pokemon_data()
    return Pokemon(str(pokemon_data_frame.get("name")[pokemon_id]))


def add_from_id_to_team(pokemon_id, team):
    team.add_pokemon(create_pokemon_from_id(pokemon_id))
