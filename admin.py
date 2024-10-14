from user import User
class Admin:
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.bank_balance = 0
        self.users = []
        self.loan_feature_on = True

    def create_account(self, name, email, address, account_type):
        new_user = User(name, email, address, account_type)
        self.users.append(new_user)
        print(f"Account Created For {name}, Account Number: {new_user.account_number}")
        return new_user

    def delete_account(self, account_number):
        user = self.find_user(account_number)
        if user:
            self.bank_balance -= user.balance
            self.users.remove(user)
            print(f'Account Number: {account_number} is deleted.')
        else:
            print(f"Account Number: {account_number} is not found.")

    def find_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None
    
    def users_list(self):
        print("User Account List:")
        for user in self.users:
            print(f"Name: {user.name}, Account Number: {user.account_number}, Email: {user.email}, Account Type: {user.account_type}")
    
    def check_total_bank_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total Available Balance in Bank: {total_balance}")
        return total_balance
    
    def check_total_loan_amount(self):
        total_loans = sum(user.loans_taken for user in self.users) * 2000
        print(f"Total Loan Amount given: {total_loans}")
        return total_loans

    def on_off_loan_feature(self):
        self.loan_feature_on = not self.loan_feature_on
        if self.loan_feature_on:
            state = "on"
        else:
            state = "off"
        print(f"Loan feature is now {state}.")
    
    def get_existing_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None
