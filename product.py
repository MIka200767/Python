class Product:
    def __init__(self, name, quantity, purchase_price):
        if isinstance(name, str) and isinstance(quantity, (int, float)) and isinstance(purchase_price, (int, float)):
            self._name = name
            self._quantity = quantity
            self._purchase_price = purchase_price
            self._payment_price = purchase_price + purchase_price * 0.25
        else:
            raise TypeError

    @property
    def product_name(self):
        return self._name

    @product_name.setter
    def product_name(self, value):
        self._name = value

    @property
    def product_quantity(self):
        return self._quantity

    @product_quantity.setter
    def product_quantity(self, value):
        self._quantity = value

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, value):
        self._purchase_price = value

    @property
    def payment_price(self):
        return self._payment_price

    @payment_price.setter
    def payment_price(self, value):
        self._payment_price = value


