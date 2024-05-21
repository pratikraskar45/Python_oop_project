from bankaccounts import *

Pratik = BankAccount(1000, "Pratik")
Vishal = BankAccount(2000, "Vishal")

Pratik.get_balance()
Vishal.get_balance()

Vishal.deposit(500)

Pratik.withdraw(10000)
Pratik.withdraw(10)

Pratik.transfer(10000, Vishal)
Pratik.transfer(100, Vishal)

Pranali = InterestRewardsAcct(1000, "Pranali")

Pranali.get_balance()

Pranali.deposit(100)

Pranali.transfer(100, Pratik)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(10000, Vishal)
Blaze.transfer(1000, Vishal)