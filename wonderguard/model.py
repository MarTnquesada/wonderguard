'''Main data types'''
import attr

@attr.s
class PokemonMonthData(object):
    name = attr.ib()
    tier = attr.ib()
    usage = attr.ib()
    abilities = attr.ib()
    items = attr.ib()
    moves = attr.ib()
    spreads = attr.ib()
    teammates = attr.ib()
    checks = attr.ib()
    lead_usage = attr.ib()


if __name__ == "__main__":
    pass