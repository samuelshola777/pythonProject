class AccountClass:
    def __init__(self, account_name=None, account_balance=None):
        self.account_name = None
        self.account_balance = 0.0

    def set_account_name(self, account_name):
        self.account_name = account_name

    def withdraw(self, amount_withdraw):
        self.account_balance -= amount_withdraw

    def deposit(self, amount_deposite):
        self.account_balance += amount_deposite

    def view_balance(self):
        return self.account_balance


if __name__ == '__main__':
    bank_account = AccountClass()

    entered_name = input("please enter an account name \n")

    bank_account.set_account_name(entered_name)

    money = float(input("  please make some deposit \n"))

    bank_account.deposit(money)

    print("your current account balance is   ",bank_account.view_balance())

    money = float(input("how much do You want to withdraw \n"))

    bank_account.withdraw(money)

    print("your current account balance is   ", bank_account.view_balance())

