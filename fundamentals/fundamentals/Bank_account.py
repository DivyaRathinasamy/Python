class BankAccount:
    bank_name = "Bank of America"
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account.append(self)

      
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
         print(f"Balance:{self.balance}")
         print(self.int_rate)
         return self

            


    def yield_interest(self):
        if self.account_balance > 0:
            self.balance += self.balance * self.int_rate

        else:
            print("Insufficient Balance")
            return self


@classmethod
def print_all_accounts(cls):
    for account in cls:
        account.display_account_info()


account1 =BankAccount()
account2 =BankAccount()

account1.deposit(500).deposit(400).deposit(600).deposit(300).withdraw(100).display_account_info().yield_interest()
account2.deposit(200).deposit(300).withdraw(200).withdraw(100).withdraw(100).yield_interest().display_account_info()