import unittest
import requests
import json
from get_data import get_data

class TestPokemon(unittest.TestCase):

    def test_valid_pokemon(self):
        my_data = get_data()
        pokemon = my_data.get('kakuna')
        my_pokemon = pokemon.json()
        data = my_data.get_pokemon('kakuna')
        self.assertEqual(pokemon.status_code, 200)
        self.assertEqual(data['weight'], my_pokemon['weight'])
        for i in my_pokemon['moves']:
            self.assertTrue(i['move']['name'] in data['moves'])
    
    def test_search_pokemon_by_number(self):
        my_data = get_data()
        pokemon = my_data.get('1')
        data = my_data.get_pokemon('bulbasaur')
        my_pokemon = pokemon.json()
        self.assertEqual(pokemon.status_code, 200)
        self.assertEqual(my_pokemon['name'], data['name'])

if __name__ == '__main__':
    unittest.main()
