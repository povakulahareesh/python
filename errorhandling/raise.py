# amount=int(input("enter number:"))
# acc_bal=199
# if acc_bal>amount:
#     print("jj")
# else:
#     print("goo and njoy")


class InsuffientBalErr(Exception):
    def _init_(self,msg):
        self.msg = msg

from InsuffientBalError import InsuffientBalErr


amount=int(input("Enter Amount:"))
acc_Bal = 15000

if acc_Bal < amount:
    #print("Low Balance")
    raise InsuffientBalErr("Low Balance")
else:
    print("Withdrawl and Enjoy")

