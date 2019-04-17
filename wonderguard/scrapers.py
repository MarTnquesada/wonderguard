'''Pulls information from the smogon/stats webpage'''

import requests
import json
import datetime

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
    print(newurl)
    response = scrape_txt(newurl)
    return response

def scrape_metagame(date_string=year_month, tier='gen7ou', threshold='1500'):
    newurl = base_url + date_string + '/metagame/' + tier + '-' + threshold + '.txt'
    print(newurl)
    response = scrape_txt(newurl)
    return response

def scrape_moveset(date_string=year_month, tier='gen7ou', threshold='1500'):
    newurl = base_url + date_string + '/moveset/' + tier + '-' + threshold + '.txt'
    print(newurl)
    response = scrape_txt(newurl)
    return response

if __name__ == "__main__":
    data = scrape_tier('2019-03', 'gen7ou', '1500')
    print(data['info'])
    for field in data['data']['Crobat']:
        print('----------------------------\n')
        print('*** ' + field + ' ***\n')
        print(data['data']['Crobat'][field])



    