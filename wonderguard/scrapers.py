'''Pulls information from the smogon/stats webpage'''

import requests
import json
import datetime
from model import PokemonMonthData

base_url = 'https://www.smogon.com/stats/'
now = datetime.datetime.now()
year_month = '{:02d}'.format(now.year) + '-' + '{:02d}'.format(now.month) 

def scrape_json(url):
    response = json.loads(requests.get(url).text)
    return response

def scrape_txt(url):
    response = requests.get(url).text
    return response

def scrape_tier(date_string=year_month, tier='gen7ou', threshold='1500'):
    newurl = base_url + date_string + '/chaos/'  + tier + '-' + threshold + '.json' 
    response = scrape_json(newurl)
    return response

def scrape_leads(date_string=year_month, tier='gen7ou', threshold='1500'):
    newurl = base_url + date_string + '/leads/' + tier + '-' + threshold + '.txt'
    response = scrape_txt(newurl)
    return response

def scrape_metagame(date_string=year_month, tier='gen7ou', threshold='1500'):
    newurl = base_url + date_string + '/metagame/' + tier + '-' + threshold + '.txt'
    response = scrape_txt(newurl)
    return response

def scrape_moveset(date_string=year_month, tier='gen7ou', threshold='1500'):
    newurl = base_url + date_string + '/moveset/' + tier + '-' + threshold + '.txt'
    response = scrape_txt(newurl)
    return response

def scrape_pokemon(name, date_string=year_month, tier='gen7ou', threshold='1500'):
    tier_data = scrape_tier(date_string=date_string, tier=tier, threshold=threshold)
    poke_data = tier_data['data'][name]
    lead_data = scrape_leads(date_string=date_string, tier=tier, threshold=threshold)
    pokemon_month_data = PokemonMonthData(name=name, tier=tier, usage=poke_data['usage'],
                                abilities=poke_data['Abilities'], items=poke_data['Items'],
                                moves=poke_data['Moves'], spreads=poke_data['Spreads'],
                                teammates=poke_data['Teammates'], checks=None, lead_usage=None)
    return pokemon_month_data

if __name__ == "__main__":
    '''
    data = scrape_tier('2019-03', 'gen7ou', '1500')
    print(data['info'])
    for field in data['data']['Crobat']:
        print('----------------------------\n')
        print('*** ' + field + ' ***\n')
        print(data['data']['Crobat'][field])
    '''
    poke = scrape_pokemon('Crobat', '2019-03', 'gen7ou', '1500')
    print(poke)



    