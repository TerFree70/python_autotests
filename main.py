import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7466c775e142a81f5c61f49eefe1f872'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

"""BODY_CREATE = {
    "name": "Vasya3",
    "photo_id": 2
}"""

BODY_CHANGE = {
    "pokemon_id": "42590",
    "name": "VASYA123",
    "photo_id": 2
}

BODY_POKEBOL = {
    "pokemon_id": "42590"
}

"""response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response.text)"""

"""response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(response_change.text)"""

response_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_CHANGE)
print(response_pokebol.text)


