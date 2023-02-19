class BankAccount:

    # Constructor
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    # Method to deposit money in the account
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
           
    # Method to withdraw money from the account
    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
      
    # Method to get the balance of the account
    def get_balance(self):
        print(f' {self.account_name} has a balance of ${self.balance:.2f}') 