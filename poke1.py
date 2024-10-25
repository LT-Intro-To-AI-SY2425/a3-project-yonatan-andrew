import csv
from typing import List, Tuple

# Load the Pokémon data
def load_pokemon_data(file_path: str) -> List[dict]:
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [{key.strip(): value.strip() for key, value in pokemon.items()} for pokemon in reader]
        print("Headers:", reader.fieldnames)  # Check headers
        print("Sample Data:", data[:5])  # Print first 5 Pokémon
        return data

def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return 0

def find_type_by_name(pokemon_data, name):
    for pokemon in pokemon_data:
        if pokemon['Name'].lower() == name.lower():
            return [pokemon['Type1'], pokemon['Type2']]
    return None

def get_pokemon_by_type(pokemon_data, type_name):
    return [pokemon['Name'] for pokemon in pokemon_data 
            if pokemon['Type1'].lower() == type_name.lower() or 
               pokemon['Type2'].lower() == type_name.lower()]

def get_hp_by_type(pokemon_data, type_name):
    return [safe_int(pokemon['HP']) for pokemon in pokemon_data 
            if pokemon['Type1'].lower() == type_name.lower() or 
               pokemon['Type2'].lower() == type_name.lower()]

def count_high_total(pokemon_data, score_threshold):
    return len([pokemon for pokemon in pokemon_data if safe_int(pokemon['Total']) > score_threshold])

def max_attack_by_type(pokemon_data, pokemon_type: str) -> int:
    attacks = [safe_int(pokemon['Attack']) for pokemon in pokemon_data 
               if pokemon['Type1'].lower() == pokemon_type.lower() or 
                  pokemon['Type2'].lower() == pokemon_type.lower()]
    return max(attacks) if attacks else 0

def count_pokemon_with_secondary_type(pokemon_data, pokemon_type: str) -> int:
    return len([pokemon for pokemon in pokemon_data if pokemon['Type2'].lower() == pokemon_type.lower()])

def list_pokemon_with_primary_type(pokemon_data, pokemon_type: str) -> List[str]:
    return [pokemon['Name'] for pokemon in pokemon_data if pokemon['Type1'].lower() == pokemon_type.lower()]

def average_speed_by_type(pokemon_data, pokemon_type: str) -> float:
    speeds = [safe_int(pokemon['Speed']) for pokemon in pokemon_data 
              if pokemon['Type1'].lower() == pokemon_type.lower() or 
                 pokemon['Type2'].lower() == pokemon_type.lower()]
    return sum(speeds) / len(speeds) if speeds else 0

def get_highest_defense_pokemon(pokemon_data) -> Tuple[str, int]:
    highest_defense = 0
    pokemon_name = ""
    for pokemon in pokemon_data:
        if safe_int(pokemon['Defense']) > highest_defense:
            highest_defense = safe_int(pokemon['Defense'])
            pokemon_name = pokemon['Name']
    return pokemon_name, highest_defense

# Load the data
pokemon_data = load_pokemon_data('gen1.csv')

# Test Cases
print("Type of Charmander:", find_type_by_name(pokemon_data, 'Charmander'))
print("Water type Pokémon:", get_pokemon_by_type(pokemon_data, 'Water'))
print("HP values of Grass Pokémon:", get_hp_by_type(pokemon_data, 'Grass'))
print("Count of Pokémon with total score > 500:", count_high_total(pokemon_data, 500))
print("Max Attack for 'Water':", max_attack_by_type(pokemon_data, 'Water'))
print("Count of Pokémon with secondary type 'Flying':", count_pokemon_with_secondary_type(pokemon_data, 'Flying'))
print("List of Pokémon with primary type 'Grass':", list_pokemon_with_primary_type(pokemon_data, 'Grass'))
print("Average Speed of 'Fire' type Pokémon:", average_speed_by_type(pokemon_data, 'Fire'))
print("Highest Defense Pokémon:", get_highest_defense_pokemon(pokemon_data))
 