class BankAccount:
    # 1. Creating a method. Not a function, because this is inside a class
    # 2. Always need the word self
    def __init__(self, holder_name, balance, account_type): 
        self.holder_name = holder_name
        self.balance = balance
        self.account_type = account_type
        self._rates = {
            'personal' : 10,
            'business' : 50
        }
        # This is fine, but currently, this accessible outside of the class
        # I.e. we can go to app.py and set self.rates = something else
        # This shouldn't be allowed

    def pay_in(self, amount):
        self.balance += amount
    # When we call this, it'll add onto the right balanced

    def pay_monthly_fee(self):
        self.balance -= self._rates[self.account_type]
        # This works instead of using a if and elif for account types. And it'll work as we add more account types

 