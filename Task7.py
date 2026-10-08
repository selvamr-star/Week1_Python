class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal not allowed.")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

account = BankAccount("Kumar", 1000)
account.deposit(500)
account.withdraw(2000)  
account.withdraw(300)

print("Final balance:", account.balance)