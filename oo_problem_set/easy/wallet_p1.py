class Wallet:
    def __init__(self, amount):
        self.amount = amount
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Wallet value must be an integer or float.")

        self._amount = amount

    def __add__(self, other):
        if isinstance(other, Wallet):
            return Wallet(self.amount + other.amount)
        
        return NotImplemented


wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True
# wallet3 = Wallet('a')
# print(wallet3.amount)