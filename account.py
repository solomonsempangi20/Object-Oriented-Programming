class Account:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0: