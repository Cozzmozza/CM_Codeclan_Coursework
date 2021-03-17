from src.bank_account import *

account_1 = BankAccount('John', 500, 'business')
account_2 = BankAccount('Cozza', 100, 'personal')

account_1.pay_monthly_fee()
account_2.pay_monthly_fee()

print(account_1.balance)
print(account_2.balance)


