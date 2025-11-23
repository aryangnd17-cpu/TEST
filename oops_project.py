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