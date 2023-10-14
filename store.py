class Store:
    def __init__(self, file_name, data, balance):
        self.profit = 0
        self.file_name = file_name
        self.data = data
        self.products = self.data.read_data(self.file_name)
        self.balance = balance

    def sell(self, name, quantity):
        if name in self.products.keys() and self.products[name]['quantity'] >= quantity:
            self.products[name]['quantity'] -= quantity
            self.profit += (self.products[name]['payment_price'] - self.products[name]['purchase_price']) * quantity
            self.check_del(name)
            self.balance.add(self.profit)
            print(f"your profit is {self.profit} and balance is {self.balance.get_balance()}")
        else:
            print(f"{name} is not available ")
        self.data.write_data(self.products, self.file_name)

    def add(self, product):
        if product.product_name in self.products.keys():
            self.products[product.product_name]['quantity'] += product.product_quantity
            self.balance.deduct(self.products[product.product_name]['purchase_price'])
        else:
            self.products[product.product_name] = {
                'quantity': product.product_quantity,
                'payment_price': product.payment_price,
                'purchase_price': product.purchase_price
            }
            self.balance.deduct(self.products[product.product_name]['purchase_price'])
        self.data.write_data(self.products, self.file_name)

    def check_del(self, name):
        if self.products[name]['quantity'] <= 0:
            del self.products[name]
        self.data.write_data(self.products, self.file_name)

    def show_profit(self):
        return self.profit

#
# if __name__ == '__main__':
#     filename = 'stor.json'
#
#     db = Data()
#     db.read_data(filename)
#     store = Store(filename, db)
#
#     product = Product('mango', 30, 5000)
#     product1 = Product('apple', 20, 400)
#     product2 = Product('orange', 40, 500)
#     product3 = Product('ananas', 40, 500)

    # store.add(product2)
    # store.add(product1)
    # store.sell(70, 'orange')
    # data = db.read_data(filename)
    #
    # print(data)
    # store.add(product2)
    # store.add(product3)
    # store.add(product)
    # print(data)
    # store.sell(90, 'ananas')
    # data = db.read_data(filename)
    # print(data)
    # profit = Store.show_profit()
