import requests

URL = "https://api.pokemonbattle.ru/v2" 
TOKEN = "5e834725ece2a0e81abdef142f8dade3"
HEADER = {"Content-Type" : "application/json", "trainer_token":TOKEN}

body_create = {
    "name": "Бульба",
    "photo_id": 26
}

body_new_name = {
    "pokemon_id": "287997",
    "name": "Мегазавр",
    "photo_id": 26
}

body_add_pokeball = {
    "pokemon_id": "287997"
}

"""response_crate = requests.post(url = f"{URL}/pokemons", headers = HEADER, json= body_create)
print(response_crate.text)"""

"""response_new_name = requests.put(url = f"{URL}/pokemons", headers = HEADER, json= body_new_name)
print(response_new_name.text)"""

"""response_crate = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json= body_add_pokeball)
print(response_crate.text)"""

response_crate = requests.put(url = f"{URL}/trainers/delete_pokeball", headers = HEADER, json= body_add_pokeball)
print(response_crate.text)