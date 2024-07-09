import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3beef84e267eb46479784133115a295b'
HEADER = {'Content-Type' : 'application/json'}
BODY_CREATE = {
    "name": "generate",
    "photo": "https://dolnikov.ru/pokemons/albums/002.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response)