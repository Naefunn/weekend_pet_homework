from xml.dom.minidom import Element


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

def get_stock_count(dict):
    stock_num = len(dict["pets"])
    return stock_num

def get_pets_by_breed(dict, name):
    pets_with_name = []
    for item in dict["pets"]:
        if item["breed"] == name:
            pets_with_name.append(item)
    return pets_with_name
    
def find_pet_by_name(dict, name):
    for item in dict["pets"]:
        if item["name"] ==  name:
            return item

def remove_pet_by_name(dict, name):
    index = -1
    for item in dict["pets"]:
        index += 1
        if item["name"] == name:
            dict["pets"].pop(index)
    return dict

def add_pet_to_stock(dict, new_pet):
    dict["pets"].append(new_pet)
    return dict

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash
    return customer["cash"]


def get_customer_pet_count(customer):
    pet_count = 0
    pet_count += len(customer["pets"])
    return pet_count

# def add_pet_to_customer():
    












