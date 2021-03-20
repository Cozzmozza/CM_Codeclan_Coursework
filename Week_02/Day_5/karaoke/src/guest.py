class Guest:
    def __init__(self, name, wallet_balance):
        self.name = name
        self.wallet_balance = wallet_balance
    
    def remove_cash_from_wallet(self, amount):
        self.wallet_balance -= amount