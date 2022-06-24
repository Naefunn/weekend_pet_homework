def get_pet_shop_name(name):
    return name["name"]


def get_total_cash(total):
    return total["admin"]["total_cash"]


def add_or_remove_cash(total_cash, add_cash):
    total_cash["admin"]["total_cash"] += add_cash
    return total_cash



