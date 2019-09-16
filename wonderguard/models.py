import attr


@attr.s
class Pokemon(object):
    name = attr.ib()
    tier = attr.ib()
    type1 = attr.ib()
    type2 = attr.ib()
    abilities = attr.ib()
    moves = attr.ib()
    base_hp = attr.ib()
    base_atk = attr.ib()
    base_def = attr.ib()
    base_spatk = attr.ib()
    base_spdef = attr.ib()


@attr.s
class PokemonMonthData(object):
    name = attr.ib()
    tier = attr.ib()
    date = attr.ib()
    usage = attr.ib()
    abilities = attr.ib()
    items = attr.ib()
    moves = attr.ib()
    spreads = attr.ib()
    teammates = attr.ib()
    checks = attr.ib()
    viability = attr.ib()
    lead_usage = attr.ib()
