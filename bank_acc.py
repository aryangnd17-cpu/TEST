class BalanceException(Exception):
    pass



class Bank_Account:
    def __init__(self,initialization,accName):

        self.balance=initialization
        self.name=accName

        print(f"\nAccount '{self.name}' created.\nbalance = ${self.balance:.2f}") 
    

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
      
    def deposite(self,amount):
        self.balance= self.balance+amount
        print("\ndeposite complete.")
        self.get_balance

    def variableTransaction(self,amount):
        if self.balance >=amount:
            return
        else:
            raise  BalanceException(
                f"\n Sorry, account {self.name} only has of ${self.balance:.2f}"
            )     

    def withdraw(self,amount):
        try:
            self.variableTransaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw complete.")

            self.get_balance()

        except BalanceException as error:
            print(f"withdraw interupted:{error}")      

    def tranfer(self,amount,account):
        try:
            print('\n**********\n\n Bignning Transfer ..')
            self.variableTransaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print("\nTransaction completed!☑️\n\n**********")
        except BalanceException as error:
            print("\n Transfer interrupted.✖️ {error}")    


class InterestRewardAcc(Bank_Account):
    def deposite(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDeposite complete")
        self.get_balance()

class savingsAcc(InterestRewardAcc):
    def __init__(self,initialization,accName):
        super().__init__(initialization,accName)
        self.fee=5
    def withdraw(self,amount):
        try:
            self.variableTransaction(amount + self.fee)
            self.balance=self.balance - (amount + self.fee)
            print("\nWithdraw complete")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw interupted: {error}")  


from bank_acc import *

Aryan = Bank_Account(10000, "Aryan")
Vipul = Bank_Account(12000, "Vipul")

Aryan.get_balance()
Vipul.get_balance()


Vipul.deposite(5000)
Vipul.withdraw(3000)
Vipul.tranfer(10000,Aryan)

Manish = InterestRewardAcc(20000, "Manish")
Manish.deposite(5000)
Manish.get_balance()
Manish.tranfer(3000,Aryan)

Vivek = savingsAcc(15000, "Vivek")

Vivek.get_balance()
Vivek.deposite(4000)
Vivek.tranfer(70000, Vipul)
Vivek.tranfer(7000, Vipul)
                        

    
