class MomoWallet:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = value


Solomon_wallet = MomoWallet("Solomon", 100000)
print(f"{Solomon_wallet.owner_name}'s balance: Ugsh {Solomon_wallet.balance}")
