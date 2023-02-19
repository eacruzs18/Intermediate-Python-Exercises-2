from BankAccount import BankAccount

# Declare variables with name account and starting balance
bank_account_name = "Ed's Account"
starting_balance = 0.00

# Call constructor
x = BankAccount(bank_account_name, starting_balance) 

# Call the deposit method
x.deposit(1000.00)

# Call the withdraw
x.withdraw(800.00)

# Call the get_balance method
x.get_balance()