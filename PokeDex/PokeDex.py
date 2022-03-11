import requests
import json



POKEDEX_SIZE = 10
pokemon_id = 1

def request_data(url):
    urlResult = requests.get(url)
    urlResult = urlResult.text
    pokeApiData = json.loads(urlResult)
    return pokeApiData

class Pokemon:
    # collect attribute data for class
    def pokemon_attributes(pokemon_id):
        url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
        pokemon_attributes = []
        data = request_data(url)
        for key in data:
            if key != 'past_types':
                pokemon_attributes.append(data[key])
        return pokemon_attributes

    def __init__(self, abilities, base_experience, forms, game_indices,
                 height, held_items, id_num, is_default, location_area_encounters, moves,
                 name, order, species, sprites, stats, types, weight):
        self.abilities = abilities
        self.base_experience = base_experience
        self.forms = forms
        self.game_indices = game_indices
        self.height = height
        self.held_items = held_items
        self.id_num = id_num
        self.is_default = is_default
        self.location_area_encounters = location_area_encounters
        self.moves = moves
        self.name = name
        self.order = order
        self.species = species
        self.sprites = sprites
        self.stats = stats
        self.types = types
        self.weight = weight

    # extract pokemon abilities
    def pokemon_ability(self):
        abilities = ''
        for item in self.abilities:
            if item['is_hidden'] == True:
                abilities = abilities + ', ' + item['ability']['name'] + '(hidden)'
            else:
                abilities = abilities + ', ' + item['ability']['name']
        abilities = abilities.replace(',', '', 1)
        abilities = abilities.strip()
        return abilities

    def pokemon_types(self):
        typ = ''
        for item in self.types:
            typ = typ + ', ' + (item['type']['name'])
        typ = typ.replace(',', '', 1)
        typ = typ.strip()
        return typ

    def pokemon_stats(self):
        stat_dict = {}
        for item in self.stats:
            stat_dict[item['stat']['name']] = item['base_stat']
        return stat_dict

    # species data request
    def species_data(self):
        base_url = 'https://pokeapi.co/api/v2/pokemon-species/'
        pokemon_specie = self.species['name']
        url = base_url + pokemon_specie
        data = request_data(url)
        return data

    # collect all pokemon data and print is nicely
    def pokemon_info(self):
        name = self.name.title()
        id_num = str(self.id_num)
        height = str(self.height / 10) + ' m'
        weight = str(self.weight / 10) + ' Kg'
        base_experience = str(self.base_experience)
        stats = self.pokemon_stats()
        hp = str(stats['hp'])
        attack = str(stats['attack'])
        defense = str(stats['defense'])
        sp_attack = str(stats['special-attack'])
        sp_defense = str(stats['special-defense'])
        speed = str(stats['speed'])

        # make only one call to collect all species data
        # uses more memory but runs much faster
        species_data = self.species_data()

        def species_description(data):
            for item in data['flavor_text_entries']:
                if item['language']['name'] == 'en':
                    description = item['flavor_text']
                    break
            # making description more readable
            description = description.replace('\n', ' ', 10)
            description = description.replace('\x0c', ' ', 10)
            return description

        color = species_data['color']['name']
        gender_rate = species_data['gender_rate']
        species_description = species_description(species_data)
        species = self.species['name']
        types = self.pokemon_types()
        abilities = self.pokemon_ability()

        def pokemon_genus(data):
            for item in species_data['genera']:
                if item['language']['name'] == 'en':
                    genus = item['genus']
                    break
            return genus

        genus = pokemon_genus(species_data)

        str1 = f"\nHeight: {height: <20}Hp: {hp: <18}\nWeight: {weight: <20}Attack: {attack: <18}"
        str2 = f"\nBase experience: {base_experience: <11}Defense: {defense: <18}\nColor: {color: <21}Special attack: {sp_attack: <18}"
        str3 = f"\nGender rate: {gender_rate: <15}Special defense: {sp_defense: <18}"
        str4 = f"\nGenus: {genus: <21}Speed: {speed: <18}"
        str5 = f"\nSpecies: {species}\n\t{species_description}\nTypes: {types}\nAbilities: {abilities}"

        info_string = str1 + str2 + str3 + str4 + str5

        return info_string

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
    with open("..\\PokemonData\\pokemon_data.json", "r") as json_file:
        pokemon_data = json.load(json_file)

    return pokemon_data

