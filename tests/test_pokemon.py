import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7466c775e142a81f5c61f49eefe1f872'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '6387'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200