from admin import Admin
from user import User
from bank import Bank

arif_bank = Bank("Bank of Arif")

admins = []

def get_existing_admin(email, password):
    for admin in admins:
        if admin.email == email or admin.password == password:
            return admin
    return None

def is_duplicate_admin(email, password):
    for admin in admins:
        if admin.email == email or admin.password == password:
            return True
    return False

def admin_menu():
    email = input("Enter Admin Email: ")
    password = input("Enter Admin Password: ")

    existing_admin = get_existing_admin(email, password)
    
    if existing_admin:
        admin = existing_admin
        print(f'Welcome Back Mr. {admin.name}!')
    else:
        name = input("Enter Admin Name: ")
        address = input("Enter Admin Address: ")

        if is_duplicate_admin(email, password):
            print("Admin with this email or password already exists")
            return
        
        admin = Admin(name, email, password, address)
        admins.append(admin)
        arif_bank.admin = admin
        print(f"Admin {admin.name} created !!")

    while True:
        print(f"\nWelcome Mr. {admin.name}!!")
        print("1. Add New User Account")
        print("2. Delete User Account")
        print("3. View All User Accounts")
        print("4. Check Total bank Balance")
        print("5. Check Total Loan Amount")
        print("6. On/Off Loan Feature")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter User Name: ")
            email = input("Enter User Email: ")
            address = input("Enter User Address: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            admin.create_account(name, email, address, account_type)
        
        elif choice == 2:
            account_number = int(input("Enter User Account Number to Delete: "))
            admin.delete_account(account_number)

        elif choice == 3:
            admin.users_list()
        
        elif choice == 4:
            admin.check_total_bank_balance()
        
        elif choice == 5:
            admin.check_total_loan_amount()

        elif choice == 6:
            admin.on_off_loan_feature()

        elif choice == 7:
            break

        else:
            print("Error: Invalid Input, please try again.")

def user_menu():
    # name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
  
    exisiting_user =arif_bank.admin.get_existing_user(email)
    
    if exisiting_user:
        user = exisiting_user
        print(f"Welcome Mr. {user.name}")
    else:
        name = input("Enter Your Name: ")
        address = input("Enter Your Address: ")
        account_type = input("Enter Account Type (Savings/Current): ")

        if arif_bank.admin is not None:
            user = arif_bank.admin.create_account(name, email, address, account_type)
        else:
            print("Error: There is no Admin. Please at first add Admin.")

    while True:
                print(f"\nWelcome Mr. {user.name} !!")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Transfer Money")
                print('4. Check Balance')
                print("5. Check Transaction History")
                print("6. Take loan")
                print("7. Check Bank Status")
                print("8. Exit")

                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    amount = float(input("Enter amount to deposit: "))
                    user.deposit(amount)
            
                elif choice == 2:
                    amount = float(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
            
                elif choice == 3:
                    other_user_account_number = int(input("Enter recipient's account number: "))
                    other_user = arif_bank.admin.find_user(other_user_account_number)
                    if other_user:
                        amount = float(input(f"Enter amount to transfer to {other_user.name}: "))
                        user.transfer_amount(amount, other_user)
                    else:
                        print("Recipient account not found. ")
            
                elif choice == 4:
                    user.check_available_balance()

                elif choice == 5:
                    user.check_transaction_history()

                elif choice == 6:
                    if arif_bank.admin.loan_feature_on:
                        user.take_loan()
                    else:
                        print("Loan Feature Disabled!!")
            
                elif choice == 7:
                    arif_bank.check_bank_status()
            
                elif choice == 8:
                    break

                else:
                    print("Error: Invalid Input, please try again.")

while True:
    print(f"\nWelcome to {arif_bank.bank_name}!!")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        admin_menu()

    elif choice == 2:
        user_menu()
    
    elif choice == 3:
        print(f'Thank you for using {arif_bank.bank_name}. Goodbye!! See you again!!')
        break

    else:
        print("Error: Invalid Input, please try again.")