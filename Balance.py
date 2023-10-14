from read_file import Data


class Balance:
    def __init__(self, file_name):
        self._file_name = file_name
        self.data = Data()
        self._amount = self.data.read_data(self._file_name)

    def add(self, money):
        self._amount += money
        self.data.write_data(self._amount, self._file_name)

    def deduct(self, money):
        self._amount -= money
        self.data.write_data(self._amount, self._file_name)

    def get_balance(self):
        return self.data.read_data(self._file_name)

