from bank_account import *
Divyanshu=BankAccount(12000000000,"Divyanshu Jha")
DJHA=BankAccount(1000000000,"DJHA")
Tony=BankAccount(20000000,"Tony")
DJHA.getBalance()
DJHA.deposit(90000000)
Tony.withdraw(100)
Divyanshu.transfer(100,Tony)
Tony.getBalance()
dj=SavingsAccount(0,"dj")
dj.deposit(10000000)


