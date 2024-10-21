from pokemon import pokemon_db
from match import match
from typing import List, Tuple, Callable, Any

# Projection functions to access specific parts of the Pokémon data tuples
def get_name(pokemon: Tuple[str, str, int, List[str]]) -> str:
    return pokemon[0]

def get_type(pokemon: Tuple[str, str, int, List[str]]) -> str:
    return pokemon[1]

def get_total(pokemon: Tuple[str, str, int, List[str]]) -> int:
    return pokemon[2]

# Actions that take a list argument and return a list of results
def name_by_type(matches: List[str]) -> List[str]:
    type_query = matches[0]
    result = []
    for pokemon in pokemon_db:
        if type_query in get_type(pokemon).lower():
            result.append(get_name(pokemon))
    return result
def name_by_total_range(matches: List[str]) -> List[str]:
    low_total = int(matches[0])
    high_total = int(matches[1])
    return [get_name(pokemon) for pokemon in pokemon_db if low_total <= get_total(pokemon) <= high_total]

def type_by_name(matches: List[str]) -> List[str]:
    name = matches[0]
    for pokemon in pokemon_db:
        if name.lower() == get_name(pokemon).lower():  # C
            return [get_type(pokemon)]
    return []
# Pattern-action list for the natural language query system
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (["what", "pokemon", "have", "type", "_"], name_by_type),
    (["what", "pokemon", "have", "between", "_", "total", "and", "_"], name_by_total_range),
    (["what", "type", "is", "_"], type_by_name),
]

def search_pa_list(src: List[str]) -> List[str]:
    """Finds matching pattern and calls the corresponding action."""
    for pat, act in pa_list:
        val = match(pat, src)
        if val is not None:
            result = act(val)
            return result if result else ["No answers"]
    return ["I don't understand"]

def query_loop() -> None:
    """Simple query loop for user interaction."""
    print("Welcome to the Pokémon database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

# Run the query loop if this script is executed
if __name__ == "__main__":
    query_loop()
