'''Main data types'''
from collections import namedtuple

class PokemonMonthData(namedtuple('PokemonMonthData', 
                        ['name', 'tier', 'usage', 'abilities', 'items', 
                        'moves', 'spreads', 'teammates', 'checks', 'lead_usage'])):
    pass

if __name__ == "__main__":
    pass
    