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

#Fonction pour récuperer les matchs d'une équipe brievement résumés

def get_competitor_summary(urn_competitor):
    # Remplacez 'your_api_key_here' par votre véritable clé d'API

    api = SportradarAPI("soccer")
    endpoint = f"competitors/{urn_competitor}/summaries.json"
    api.call_api(endpoint)

# Exemple d'utilisation de la fonction pour obtenir les informations d'un concurrent
urn_competitor = "sr:competitor:12345"  # Remplacez par l'URN du concurrent souhaité
get_competitor_summary(urn_competitor)


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