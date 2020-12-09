## Data Abstraction ##


# Treat all the following code as being behind an abstraction layer, you shouldn't need to look at it!

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    lat_dist = (get_lat(city1) - get_lat(city2)) ** 2
    lon_dist = (get_lon(city1) - get_lon(city2)) ** 2
    return sqrt(lat_dist + lon_dist)

def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    coordinate = make_city('point', lat, lon)
    if distance(coordinate, city1) < distance(coordinate, city2):
        return get_name(city1)
    else:
        return get_name(city2)



def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    >>> change_abstraction(False)
    """


## Dictionaries

def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split()
    return { word: word_list.count(word) for word in word_list }




def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> e = replace_all(d, 3, 'poof')

    >>> e == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    new_d = d.copy()
    for i in new_d:
        if new_d[i] == x:
            new_d[i] = y
    return new_d




def make_politician(name, party, age):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> isinstance(woodrow, dict)
    True
    """
    # Make sure you use a dictionary in your implementation!
    return { 'name': name, 'party': party, 'age': age }


def get_pol_name(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_pol_name(woodrow)
    'Woodrow Wilson'
    """
    return politician['name']


def get_party(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_party(woodrow)
    'Democrat'
    """
    return politician['party']



def get_age(politician):
    """
    >>> woodrow = make_politician('Woodrow Wilson', 'Democrat', 57)
    >>> get_age(woodrow)
    57
    """
    return politician['age']



## Optional Questions


full_roster = {
    "Manny Machado" : "Dodgers",
    "Yasiel Puig" : "Dodgers",
    "Aaron Judge" : "Yankees",
    "Clayton Kershaw" : "Dodgers",
    "Giancarlo Stanton" : "Yankees"
}

full_stats = {
    "Manny Machado": ["SO", "1B", "3B", "SO", "HR"],
    "Yasiel Puig": ["3B", "3B", "1B", "1B", "SO"],
    "Aaron Judge": ["SO", "HR", "HR", "1B", "SO"],
    "Clayton Kershaw": ["1B", "SO", "SO", "1B", "SO"],
    "Giancarlo Stanton": ["HR", "SO", "3B", "SO", "2B"],
}

def get_team(player):
    """Returns team that the provided player is a member of.

    >>> get_team("Manny Machado")
    'Dodgers'
    >>> get_team("Aaron Judge")
    'Yankees'
    """
    "*** YOUR CODE HERE ***"


def get_stats(player):
    """Returns the statistics associated with the provided player.
    >>> get_stats("Manny Machado")
    ['SO', '1B', '3B', 'SO', 'HR']
    >>> get_stats('Aaron Judge')
    ['SO', 'HR', 'HR', '1B', 'SO']
    """
    "*** YOUR CODE HERE ***"




# Following Functions have been given to you, do NOT modify

def calculate_batting_average(stats):
    hits = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat != "SO":
            hits += 1
        total_bats += 1
    return float(round(hits/total_bats, 1))

def calculate_slugging_percent(stats):
    bases = 0
    total_bats = 0
    for at_bat in stats:
        if at_bat == "1B":
            bases += 1
        elif at_bat == "2B":
            bases += 2
        elif at_bat == "3B":
            bases += 3
        elif at_bat == "HR":
            bases += 4
        total_bats += 1
    return float(round(bases/total_bats, 1))

# Modify Functions below

def calculate_team_BA(team):
    """Given a single team name, returns the mean batting average of all players on that team. You are encouraged to use previous functions that you've defined already
    >>> calculate_team_BA('Dodgers')
    0.6
    >>> calculate_team_BA('Yankees')
    0.6
    """
    "*** YOUR CODE HERE ***"


def calculate_all_team_SP():
    """Returns a dictionary mapping every team to the average slugging percentage of all players on that team. You are encouraged to use previous functions that you've defined already.
    >>> calculate_all_team_SP()
    {'Dodgers': 1.2, 'Yankees': 1.8}
    """
    "*** YOUR CODE HERE ***"
