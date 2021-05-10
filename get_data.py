import json
import requests

class get_data:

    def get(self, end_point):
        with open('data.json') as json_file:
            data = json.load(json_file)
            needed_data = requests.get(data['base_url'] + end_point)
            return needed_data

    def get_pokemon(self, pokemon):
        with open (pokemon + '.json') as poke:
            return json.load(poke)
