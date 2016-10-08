#usr/bin/env python

import sys
import json


def version_input(sentance):
    return input(sentance) if sys.version_info >= (3,0) else raw_input(sentance)


def get_data():
    with open("input_data/p44.txt", 'r') as f:
        json_data = f.read()
    
    data = json.loads(json_data)
    return data


def search_product(json_data):
    while True:
        check = False
        product_name = version_input("What is the product name? ")
        for product in json_data["products"]:    
            if product["name"] == product_name:
                print("Name: %s\nPrice: $%.2f\nQuantity on hand: %s" \
                     % (product["name"], float(product["price"]), int(product["quantity"])))
                check = True
                break
        if check == True:
            break
        print("Sorry, that product was not found in our inventory.")


if __name__ == "__main__":
    json_data = get_data()
    search_product(json_data)

