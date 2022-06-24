def get_pet_shop_name(name):
    return name["name"]


def get_total_cash(total):
    return total["admin"]["total_cash"]


def add_or_remove_cash(total_cash, add_cash):
    total_cash["admin"]["total_cash"] += add_cash
    return total_cash

def get_pets_sold(dict):
    return dict["admin"]["pets_sold"]

def increase_pets_sold(dict, new_pet):
    dict["admin"]["pets_sold"]+= new_pet
    return dict







