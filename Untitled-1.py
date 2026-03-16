class BankAccount:
    def __init__(self,account_holder,balance,amount):
       self.balance=balance
       self.amount=amount
       self.account_holder=account_holder


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit complete{amount} current balance {self.balance}")
        else:
            print("deposit over zero requird")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"withdraw money{amount} {self.balance}")
        else:
            print("sorry,not enough mony" )

    def display_info(self):
        print(f"{self.account_holder}  {self.balance}")


def main():
my_account = BankAccount("Hend", 1000)
my_account.deposit(500)
my_account.withdraw(200)
my_account.display_info()
main()

