class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.admin = None
        self.bank_is_bankrupt = False

    def check_bank_status(self):
        total_balance = self.admin.check_total_bank_balance()
        if total_balance == 0:
            self.bank_is_bankrupt = True
            print("The bank is bankrupt !!")
        else:
            print(f"Bank is wealthy with Total Balance: {total_balance}")