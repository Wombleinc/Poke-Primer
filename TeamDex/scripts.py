# Christopher Duke
# TeamDex/scripts.py

import csv


def save_team_to_csv(pokemon_team):
    header = ['#', 'Pokemon', 'Held Item', 'Move 1', 'Move 2', 'Move 3', 'Move 4']

    with open('TeamDex\\team.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        i = 1
        for pokemon in pokemon_team.members:
            writer.writerow([i, pokemon.get_name(), pokemon.get_item(),
                             pokemon.get_move1(), pokemon.get_move2(), pokemon.get_move3(), pokemon.get_move4()])
            i += 1
