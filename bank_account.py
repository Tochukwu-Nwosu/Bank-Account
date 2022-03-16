"""
Create an account class with details, deposit, withdraw, details contain (name, age, sex, account_number, balance)
"""
class Account:
    def __init__(self):
        pass
    def details (self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.sex = input("Enter your sex: ")
        self.account_number = input("Enter your account number: ")
        self.balance = float(input("Enter your account balance in naira: "))
    def deposit (self):
        deposit_amount = float(input("Enter amount to deposit in naira: "))
        self.balance += deposit_amount
        self.balance = float("{:.2f}".format(self.balance))
        print(f"Account Balance: NGN {self.balance}\n")
    def withdraw (self):
        withdraw_amount = float(input("Enter amount to withdraw in naira: "))
        if (withdraw_amount <= self.balance):
            self.balance -= withdraw_amount
            self.balance = float("{:.2f}".format(self.balance))
            print(f"Account Balance: NGN {self.balance}\n")
        else:
            print("Insuficcient Fund\n")


customer = Account()
customer.details()
customer.deposit()
customer.withdraw()
