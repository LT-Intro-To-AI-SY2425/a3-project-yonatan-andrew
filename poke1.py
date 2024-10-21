import csv
from typing import List
from typing import List, Tuple 

# Load the Pokémon data
def load_pokemon_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# Function to find the type of a specific Pokémon by name
def find_type_by_name(pokemon_data, name):
    for pokemon in pokemon_data:
        if pokemon['Name'].strip().lower() == name.strip().lower():
            return [pokemon['Type1'], pokemon['Type2']]
    return None

# Function to get all Pokémon of a specific type
def get_pokemon_by_type(pokemon_data, type_name):
    return [pokemon['Name'] for pokemon in pokemon_data if pokemon['Type1'].strip().lower() == type_name.strip().lower() or pokemon['Type2'].strip().lower() == type_name.strip().lower()]

# Function to get HP values of Pokémon of a specific type
def get_hp_by_type(pokemon_data, type_name):
    return [pokemon['HP'] for pokemon in pokemon_data if pokemon['Type1'].strip().lower() == type_name.strip().lower() or pokemon['Type2'].strip().lower() == type_name.strip().lower()]

# Function to count Pokémon with total score greater than a specific value
def count_high_total(pokemon_data, score_threshold):
    return len([pokemon for pokemon in pokemon_data if int(pokemon['Total']) > score_threshold])

def get_pokemon_types(pokemon_name: str, filename: str) -> str:
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].strip('"') == pokemon_name:
                type1 = row['Type1'].strip('"')
                type2 = row['Type2'].strip('"')
                return f"{pokemon_name} types: {type1} {'and ' + type2 if type2 else ''}"
    return f"{pokemon_name} not found." 

def get_pokemon_by_type(pokemon_data: List[dict], pokemon_type: str) -> List[str]:
    matched_pokemons = []
    
    for pokemon in pokemon_data:
        type1 = pokemon['Type1']
        type2 = pokemon['Type2']
        
        if type1 == pokemon_type or type2 == pokemon_type:
            matched_pokemons.append(pokemon['Name'])  # Assuming 'Name' is the key for Pokémon names
            
    return matched_pokemons 

def get_high_total_score_pokemon(threshold: int, filename: str) -> List[str]:
    results = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['Total']) > threshold:
                results.append(row['Name'].strip('"'))
    return results

def get_hp_by_type(pokemon_data: List[dict], pokemon_type: str) -> List[int]:
    hp_values = []
    
    for pokemon in pokemon_data:
        type1 = pokemon['Type1']
        type2 = pokemon['Type2']
        
        if type1 == pokemon_type or type2 == pokemon_type:
            hp_values.append(int(pokemon['HP']))  # Convert HP to integer
            
    return hp_values  

def count_pokemon_with_secondary_type(pokemon_type: str, filename: str) -> int:
    count = 0
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type2'].strip('"') == pokemon_type:
                count += 1
    return count 

def max_attack_by_type(pokemon_type: str, filename: str) -> int:
    max_attack = 0
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type1'].strip('"') == pokemon_type or row['Type2'].strip('"') == pokemon_type:
                max_attack = max(max_attack, int(row['Attack']))
    return max_attack 

def list_pokemon_with_primary_type(pokemon_type: str, filename: str) -> List[str]:
    results = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type1'].strip('"') == pokemon_type:
                results.append(row['Name'].strip('"'))
    return results 

def average_speed_by_type(pokemon_type: str, filename: str) -> float:
    total_speed = 0
    count = 0
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type1'].strip('"') == pokemon_type or row['Type2'].strip('"') == pokemon_type:
                total_speed += int(row['Speed'])
                count += 1
    return total_speed / count if count > 0 else 0 

def get_highest_defense_pokemon(filename: str) -> Tuple[str, int]:
    highest_defense = 0
    pokemon_name = ""
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['Defense']) > highest_defense:
                highest_defense = int(row['Defense'])
                pokemon_name = row['Name'].strip('"')
    return pokemon_name, highest_defense 

def get_pokemon_types_by_name(pokemon_name: str, filename: str) -> List[str]:
    types = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Name'].strip('"') == pokemon_name:
                types.append(row['Type1'].strip('"'))
                if row['Type2'].strip('"'):
                    types.append(row['Type2'].strip('"'))
    return types 
# Load the data
pokemon_data = load_pokemon_data('gen1.csv')

# Test Cases
print("Type of Charmander:", find_type_by_name(pokemon_data, 'Charmander'))  # ["Fire", " "]
print("Water type Pokémon:", get_pokemon_by_type(pokemon_data, 'Water'))  # List of Water type Pokémon
print("HP values of Grass Pokémon:", get_hp_by_type(pokemon_data, 'Grass'))  # List of HP values for Grass types
print("Count of Pokémon with total score > 500:", count_high_total(pokemon_data, 500))  # Count of high total Pokémon
print(get_pokemon_types("Pikachu", "gen1.csv"))  # Expected: Pikachu types: Electric
print("Water type Pokémon:", get_pokemon_by_type(pokemon_data, 'Water'))  # List of Water type Pokémon
print(get_high_total_score_pokemon(500, "gen1.csv"))  # Expected: List of Pokémon with Total > 500
print("Type of Charmander:", find_type_by_name(pokemon_data, 'Charmander'))  # Expected: ["Fire", " "]
print("Water type Pokémon:", get_pokemon_by_type(pokemon_data, 'Water'))  # Expected: List of Water type Pokémon
print("HP values of Grass Pokémon:", get_hp_by_type(pokemon_data, 'Grass'))  # Expected: List of HP values for Grass types
print("Count of Pokémon with total score > 500:", count_high_total(pokemon_data, 500))  # Expected: Count of high total Pokémon
print(get_pokemon_types("Pikachu", "gen1.csv"))  # Expected: Pikachu types: Electric
print("Count of Pokémon with secondary type 'Flying':", count_pokemon_with_secondary_type('Flying', 'gen1.csv'))  # Expected: Count of Flying secondary types
print("Max Attack for 'Water':", max_attack_by_type('Water', 'gen1.csv'))  # Expected: Max Attack for Water type Pokémon
print("List of Pokémon with primary type 'Grass':", list_pokemon_with_primary_type('Grass', 'gen1.csv'))  # Expected: List of Grass type Pokémon
print("Average Speed of 'Fire' type Pokémon:", average_speed_by_type('Fire', 'gen1.csv'))  # Expected: Average Speed of Fire type Pokémon
print("Highest Defense Pokémon:", get_highest_defense_pokemon("gen1.csv"))  # Expected: (Name, Defense)
print("Types of Bulbasaur:", get_pokemon_types_by_name("Bulbasaur", "gen1.csv"))  # Expected: List of types for Bulbasaur 
