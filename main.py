from Balance import Balance
from store import Store
from product import *
from read_file import *


def main(store):
    while True:
        action = input("enter: exit, add or sell, balance: ")
        if action == "exit":
            break
        elif action == "add":
            try:
                name = str(input("enter the name of product "))
                quantity = int(input(f"enter the quantity of the {name} "))
                purchase_price = float(input(f"enter the purchase price of {name} "))
                product = Product(name, quantity, purchase_price)
                store.add(product)

            except ValueError:
                print("sorry something went wrong! ")
        elif action == "sell":
            try:
                name = input("enter the product: ")
                quantity = float(input(f"enter the quantity of {name} "))
                store.sell(name, quantity)
            except ValueError:
                print("smth went wrong ")
        elif action == "balance":
            print(store.balance.get_balance())


if __name__ == '__main__':
    data = Data()
    file_stor = 'stor.json'
    file_balance = 'balance.json'
    balance = Balance(file_balance)
    store = Store(file_stor, data, balance)
    main(store)



