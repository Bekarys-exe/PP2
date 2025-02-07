class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} made. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withsdrawal denied. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} made. New balance: {self.balance}")

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

account = Account("Alice", 100)
print(account)

account.deposit(50)
account.withdraw(30)
account.withdraw(150)
account.deposit(200)
account.withdraw(100)

print(account)