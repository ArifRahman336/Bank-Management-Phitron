import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name 
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transactions = []
        self.account_number = random.randint(100,999)
        self.loans_taken = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited Amount: {amount}")
        print(f"Successfully deposited {amount} . Current balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw Amount: {amount}")
            print(f"Successfully withdraw {amount} . Current balance: {self.balance}")
    
    def check_available_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)
    
    def take_loan(self):
        if self.loans_taken < 2:
            self.balance += 2000
            self.loans_taken += 1
            self.transactions.append(f"Loan Taken: 2000")
            print("Loan Given 2000 tK")
        else:
            print("Error: Loan limit exceeded !!")
    
    def transfer_amount(self, amount, other_user):
        if amount > self.balance:
            print("Error: Balance is low !!")
        else:
            self.balance -= amount
            other_user.balance += amount
            self.transactions.append(f"Transferred {amount} To {other_user.name}")
            other_user.transactions.append(f"Received {amount} from {self.name}")
            print(f"Transferred {amount} to {other_user.name}.")