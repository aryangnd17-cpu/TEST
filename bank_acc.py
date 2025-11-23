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
                        
    