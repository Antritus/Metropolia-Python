class Bank_account:
    name = ""
    balance = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def add(self, amount):
        self.balance += amount
        print(f"Added {amount} euros to the account")
        return self

    def spend(self, amount):
        if (self.balance < amount):
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Spent {amount} euros")
        return self

    def __str__(self):
        return f"Account name: {self.name}, Account balance: {self.balance}"

