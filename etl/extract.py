import yaml
import json
import requests
import pandas as pd
import os

#recuperation gestion des token
with open('../config/config.yaml', 'r') as config_file:
    config_data = yaml.safe_load(config_file)
#création d'un dictionnaire de token
tokens = {}
#recuperation des valeur des token depuis la conf.yaml
foot_data = config_data.get('api_football-data', {}).get('token')
oddscomparison_futures = config_data.get('oddscomparison-futures', {}).get('token')
soccer_advanced_analytics = config_data.get('soccer-advanced-analytics', {}).get('token')
soccer_extended = config_data.get('soccer-extended', {}).get('token')
soccer = config_data.get('soccer', {}).get('token')

'''
https://api.sportradar.com/oddscomparison-futures/trial/v2
https://api.sportradar.com/soccer-advanced-analytics/trial/v1
https://api.sportradar.com/soccer-extended/trial/v4
https://api.sportradar.com/soccer/trial/v4

'''

#ajout des tokens au dict precedement créé
if foot_data:
    tokens['api_football-data'] = foot_data
if oddscomparison_futures:
    tokens['oddscomparison-futures'] = oddscomparison_futures
if soccer_advanced_analytics:
    tokens['soccer-advanced-analytics'] = soccer_advanced_analytics
if soccer_extended:
    tokens['soccer-extended'] = soccer_extended
if soccer:
    tokens['soccer'] = soccer


import requests

class SportradarAPI:
    def __init__(self, token_name):
        self.token_name = token_name
        self.base_url = self._get_base_url()
        
    def _get_base_url(self):
        if self.token_name == 'oddscomparison_futures':
            return 'https://api.sportradar.com/oddscomparison-futures/trial/v2/en/'
        elif self.token_name == 'soccer_advanced_analytics':
            return 'https://api.sportradar.com/soccer-advanced-analytics/trial/v1/en/'
        elif self.token_name == 'soccer_extended':
            return 'https://api.sportradar.com/soccer-extended/trial/v4/en/'
        else:
            return 'https://api.sportradar.com/soccer/trial/v4/en/'
        
    def call_api(self, endpoint):
        # Vérifiez si le nom du token existe dans le dictionnaire
        if self.token_name in tokens:
            url = self.base_url + endpoint  # Utilisez l'endpoint passé en argument

            # Dictionnaire d'en-têtes avec votre token
            params = {
                'api_key': tokens[self.token_name],
            }

            # Requête HTTP
            response = requests.get(url, params=params)

            # Vérifiez la réponse
            if response.status_code == 200:
                data = response.json()
                print(data)
            else:
                print(f"Erreur : {response.status_code} from {self.base_url}")
        else:
            print(f"Le token {self.token_name} n'existe pas dans le dictionnaire.")

# Exemple d'utilisation de la classe SportradarAPI

#api = SportradarAPI("soccer")
SportradarAPI("soccer").call_api("competitions/sr:competition:7/info.json")

'''
#fonction d'appel à sportradar
def appel_api_sportradar(token_name, endpoint):
    # Vérifiez si le nom du token existe dans le dictionnaire
    if token_name in tokens:

        if token_name == 'oddscomparison_futures':
            base_url = f'https://api.sportradar.com/oddscomparison-futures/trial/v2/en/'
        elif token_name == 'soccer_advanced_analytics':
            base_url = f'https://api.sportradar.com/soccer-advanced-analytics/trial/v1/en/'
        elif token_name == 'soccer_extended':
            base_url = f'https://api.sportradar.com/soccer-extended/trial/v4/en/'
        else:
            base_url = f'https://api.sportradar.com/soccer/trial/v4/en/'

       
        url = base_url + endpoint  # Utilisez l'endpoint passé en argument

        # Dictionnaire d'en-têtes avec votre token
        params = {
            'api_key': tokens[token_name],
        }

        # Requête HTTP
        response = requests.get(url, params=params)

        # Vérifiez la réponse
        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Erreur : {response.status_code} from {base_url}")
    else:
        print(f"Le token {token_name} n'existe pas dans le dictionnaire.")

# Exemple d'appel à la fonction en utilisant le nom du token et l'endpoint
appel_api_sportradar("soccer", "competitions/sr:competition:7/info.json")
'''

'''
#!exemple d'appels (1)
if 'soccer-advanced-analytics' in tokens:

    base_url = 'https://api.sportradar.com/soccer-advanced-analytics/trial/v1/en/'
    endpoint = 'players/mappings.json?offset=0&start=5&limit=5'
    url = base_url + endpoint

    #dictionnaire d'en-têtes avec votre token
    params = {
        'api_key': tokens["soccer-advanced-analytics"],
    }
    #requête HTTP
    response = requests.get(url, params=params)

    # Vérifiez la réponse
    if response.status_code == 200:
        data = response.json()
        # Traitez les données ici
    else:
        print(f"Erreur : {response.status_code}")



#!exemple d'appels (2)
if 'oddscomparison-futures' in tokens:

    base_url = 'https://api.sportradar.com/oddscomparison-futures/trial/v2/en/'
    endpoint = 'books.json'
    url = base_url + endpoint

    #dictionnaire d'en-têtes avec votre token
    params = {
        'api_key': tokens["oddscomparison-futures"],
    }
    #requête HTTP
    response = requests.get(url, params=params)

    # Vérifiez la réponse
    if response.status_code == 200:
        data = response.json()
        # Traitez les données ici
    else:
        print(f"Erreur : {response.status_code}")



#!exemple d'appels (3)
if 'soccer-extended' in tokens:

    base_url = 'https://api.sportradar.com/soccer-extended/trial/v4/en/'
    endpoint = 'players/sr:player:43247/profile.json'
    url = base_url + endpoint

    #dictionnaire d'en-têtes avec votre token
    params = {
        'api_key': tokens["soccer-extended"],
    }
    #requête HTTP
    response = requests.get(url, params=params)

    # Vérifiez la réponse
    if response.status_code == 200:
        data = response.json()
        # Traitez les données ici
    else:
        print(f"Erreur : {response.status_code}")

'''
'''
info LDC
{'id': 'sr:competition:7', 'name': 'UEFA Champions League', 'gender': 'men', 'category': {'id': 'sr:category:393', 'name': 'International Clubs'}},

{
            "id": "sr:season:106479",
            "name": "UEFA Champions League 23/24",
            "start_date": "2023-06-27",
            "end_date": "2024-06-01",
            "year": "23/24",
            "competition_id": "sr:competition:7"
        }
        

"groups": [
                        {
                            "id": "sr:league:74527",
                            "name": "UEFA Champions League 23/24, Group B",
                            "group_name": "B"
                        }
                    ]
                    
SEVILLE LENS : "id": "sr:sport_event:43459327"
LENS - ARSENAL : "id": "sr:sport_event:43459331"
LENS - PSV : "id": "sr:sport_event:43459429"
PSV - LENS : "id": "sr:sport_event:43459443"
ARSENAL - LENS : "id": "sr:sport_event:43459453"
LENS - SEVILLE : "id": "sr:sport_event:43459457"

ARSENAL : "competitor:42"

'''