class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.05, balance =0)


    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print(self.name,self.account.balance,self.type)

    def transfer_money(self,other_user,amount):
        self.make_withdrawl(amount)
        other_user.make_deposit(amount)
    


class BankAccount:
    bank_name = "Bank of America"
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

      
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



account=User("John", "John@dojo.com")
# account=User.display_account_info()
