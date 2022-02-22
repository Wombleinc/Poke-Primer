# Christopher Duke
# TeamDex/scripts.py

import csv


def save_team_to_csv(pokemon_team):
    header = ['#', 'Pokemon', 'Held Item', 'Move 1', 'Move 2', 'Move 3', 'Move 4']

    with open('Trainer\\team.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        for count, pokemon in enumerate(pokemon_team.members):
            writer.writerow([count + 1, pokemon.get_name(), pokemon.get_item(),
                             pokemon.get_move1(), pokemon.get_move2(), pokemon.get_move3(), pokemon.get_move4()])
