# The projection functions, that give us access to certain parts of a "movie" (a tuple)
from pokemon import pokemon_db
from match import match
from typing import List, Tuple, Callable, Any
def get_name(pokemon_db: List[Tuple[int, str, List[str], List[str], int, int, int, int, int, int, int, int]]) -> str:
    return pokemon_db[0]

def get_type(pokemon_db: List[Tuple[int, str, List[str], List[str], int, int, int, int, int, int, int, int]]) -> str:
    return pokemon_db[1]

def get_total(pokemon_db: List[Tuple[int, str, List[str], List[str], int, int, int, int, int, int, int, int]]) -> str:
    return pokemon_db[2]

# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def name_by_type(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """
    type = int(matches[0])
    result = []
    for pokemon in pokemon_db:
        if get_type(pokemon) == get_type:
            result.append(get_name(pokemon))
            print(result)
    return result

def name_by_ltotal_range(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get movies from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get movies made in 1991, 1992, 1993 & 1994)
    """
    low_total = 150
    total = int(matches[2])
    result = []
    for pokemon in pokemon_db:
        if low_total <= total <= 400:
            result.append(get_name(pokemon))
    print("These Are The Weak Ones:")
    return result
def name_by_htotal_range(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get movies from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get movies made in 1991, 1992, 1993 & 1994)
    """
    high_total = 401
    total = int(matches[2])
    result = []
    for pokemon in pokemon_db:
        if 401 <= total <= 1000:
            result.append(get_name(pokemon))
    print("These Are The Strong ones:")
    return result



def type_by_name(matches: List[str]) -> List[str]:
    """Finds director of movie based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the movie
    """
    name = matches[0]
    result = []
    for pokemon in pokemon_db:
        if name == get_name(pokemon):
            result.append(get_type(pokemon))
    return result


def total_by_name(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get movies from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get movies made in 1991, 1992, 1993 & 1994)
    """
    name = matches[0]
    result = []
    for pokemon in pokemon_db:
        if name == get_name(pokemon):
            result.append(get_total(pokemon))
    return result

# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("What pokemon have type _"), name_by_type),
    (str.split("what pokemon have between 150 total and _"), name_by_ltotal_range),
    (str.split("what pokemon have between 401 total and _"), name_by_htotal_range),
    (str.split("What type is _"), type_by_name),
    (str.split("what pokemon has _ total"), total_by_name),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes sourc, finds matching pattern and calls corresponding action. If it finds
    a match but has eno answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        val = match(pat, src)
        if val != None:
            result = act(val)
            if result:
                return result
            else:
                return["No answers"]
    return["I don't understand"]
        
def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
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