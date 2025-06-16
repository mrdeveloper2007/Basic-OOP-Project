class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initial_amount,account_name):
        self.balance=initial_amount
        self.account_name=account_name
        print(f"Account '{self.account_name}' created\n Balance:{self.balance:.2f}")
        print("\n")
    def getBalance(self):
        print(f"ACCOUNT NAME:{self.account_name}\n Balance:{self.balance:.2f}")
        print("\n")
    def deposit(self,deposit_amount,show_balance=True):
            self.balance+=deposit_amount
            print(f"Amount:{deposit_amount} deposited")
            if show_balance:    
                self.getBalance()
            print("\n")
    def ViableTransaction(self,amount):
        if self.balance>amount and amount>0:
            return True
        else:
            raise BalanceException(f"ACCOUNT:{self.account_name} has insufficient balance by {amount-self.balance}INR")
    def withdraw(self,amount):
        try:
            self.ViableTransaction(amount)
            self.balance-=amount
            print("winthdraw completed")
            self.getBalance()
        except BalanceException as error:
            print(f"withdraw interuppted:{error}")
    def transfer(self,amount,account):
        print("#######################################")

        try:
            self.ViableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount,show_balance=False)
            print("transfer completed")
        except BalanceException as error:
            print(f"transfer interuppted ERROR:{error}")
        print("#######################################")
        print("\n")
class InterestRewardAccount(BankAccount):
    def deposit(self,amount):
        self.balance=self.balance+(1.05*amount)
        print("DEPOSITED COMPLETED")
        self.getBalance()
class SavingsAccount(InterestRewardAccount):
    def __init__(self,initial_amount,account_name):
        super().__init__(initial_amount,account_name)
        self.fee=5
    def withdraw(self,amount):
        try:
            self.ViableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("withdraw sucessful")
            self.getBalance()
        except BalanceException as error:
            print(f"WITHDRAW INTERRUPTED:{error}")
if __name__=="__main__":
   print("welcome to DBANK")
