# Pulls information from the smogon/stats webpage
import sys
import os
from wonderguard.models import Pokemon, PokemonMonthData
import requests
import json
import datetime
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('..', 'config')))

BASE_URL = 'https://www.smogon.com/stats/'
now = datetime.datetime.now()
now_year_month = '{:02d}'.format(now.year) + '-' + '{:02d}'.format(now.month)


def scrape_json(url):
    """

    :param url:
    :return:
    :rtype: dict
    """
    response = json.loads(requests.get(url).text)
    return response


def scrape_txt(url):
    """

    :param url:
    :return:
    :rtype: str
    """
    response = requests.get(url).text
    return response


def scrape_tier(date_string=now_year_month, tier='gen7ou', threshold='1500'):
    """

    :param date_string:
    :param tier:
    :param threshold:
    :return: DataFrame with the information relative to that tier
    :rtype: DataFrame
    """
    file_path = 'cache/' + date_string + '_chaos_' + tier + '-' + threshold + '.csv'
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path, index_col=0)
        print(df.loc['Crobat'])
    else:
        url = BASE_URL + date_string + '/chaos/' + tier + '-' + threshold + '.json'
        response = scrape_json(url)['data']
        df = pd.DataFrame.from_dict(response).transpose()
        df.to_csv(file_path, index=True, header=True)
    return df


def scrape_leads(date_string=now_year_month, tier='gen7ou', threshold='1500'):
    url = BASE_URL + date_string + '/leads/' + tier + '-' + threshold + '.txt'
    response = scrape_txt(url)
    return response


def scrape_metagame(date_string=now_year_month, tier='gen7ou', threshold='1500'):
    url = BASE_URL + date_string + '/metagame/' + tier + '-' + threshold + '.txt'
    response = scrape_txt(url)
    return response


def scrape_moveset(date_string=now_year_month, tier='gen7ou', threshold='1500'):
    url = BASE_URL + date_string + '/moveset/' + tier + '-' + threshold + '.txt'
    response = scrape_txt(url)
    return response


def scrape_pokemon_month_data(name, date_string=now_year_month, tier='gen7ou', threshold='1500'):
    tier_data = scrape_tier(date_string=date_string, tier=tier, threshold=threshold)
    poke_data = tier_data.loc[name]
    lead_data = scrape_leads(date_string=date_string, tier=tier, threshold=threshold)
    pokemon_month_data = PokemonMonthData(name=name, tier=tier, date=date_string, usage=poke_data['usage'],
                                          abilities=poke_data['Abilities'], items=poke_data['Items'],
                                          moves=poke_data['Moves'], spreads=poke_data['Spreads'],
                                          teammates=poke_data['Teammates'], checks=poke_data['Checks and Counters'],
                                          viability=poke_data['Viability Ceiling'], lead_usage=None)
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
    poke = scrape_pokemon_month_data('Crobat', '2019-03', 'gen7ou', '1500')
    print(poke)



