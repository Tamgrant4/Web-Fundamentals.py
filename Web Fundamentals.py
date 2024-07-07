# Q 1
# Task 1
python -m venv venv  # Replace "venv" with your desired environment name
pip install requests

# Task 2
import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

data = fetch_pokemon_data("pikachu")

# Extract and print the name and abilities
name = data["name"]
abilities = [ability["ability"]["name"] for ability in data["abilities"]]

print(f"Name: {name}")
print("Abilities:", ", ".join(abilities))

# Task3 
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

pokemons = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemons:
    name = pokemon["name"]
    abilities = [ability["ability"]["name"] for ability in pokemon["abilities"]]
    print(f"Name: {name}")
    print("Abilities:", ", ".join(abilities))
    print()
def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon["weight"] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

average_weight = calculate_average_weight(pokemons)

for pokemon in pokemons:
    name = pokemon["name"]
    abilities = [ability["ability"]["name"] for ability in pokemon["abilities"]]
    print(f"Name: {name}")
    print("Abilities:", ", ".join(abilities))
    print()

print(f"Average Weight: {average_weight}")

# Q 2
# Task1 
python -m venv myenv
myenv\Scripts\activate
pip install requests

# Task 2
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    return response.json()["bodies"]

planets = fetch_planet_data()

for planet in planets:
    if planet["isPlanet"]:
        name = planet["englishName"]
        mass = planet["mass"]["massValue"] if planet["mass"] else "N/A"
        orbit_period = planet["sideralOrbit"]
        print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# Task3
import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    return [planet for planet in response.json()["bodies"] if planet["isPlanet"]]

def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda p: p["mass"]["massValue"] if p["mass"] else 0)
    return heaviest["englishName"], heaviest["mass"]["massValue"]

planets = fetch_planet_data()

name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} x 10^24 kg.")



