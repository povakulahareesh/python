class Account:
    '''claass created by Narasimha'''

    def open_account(self):
        print("account created")
    def deposit_amount(self,amount):
        print("amount deposited ")
    @classmethod
    def update_min_bal(cls,amount):
        print("updated")
    @staticmethod
    def cal_interest():
        print("call")

a=Account()

# print(a.__dict__)
# print(Account.__dict__)

# #  how to aceess class members using object?
# a.open_account()
# a.deposit_amount(5000) 
# a.update_min_bal(600)
# a.cal_interest()       

#  how to accesss class method  using object  and class name 
# a.update_min_bal(600)
# Account.update_min_bal(600)

#  constructor 
# ======================================

# is a special method to initialize object  values 
#  will execute only once automatically  at the time of object cfreation 
# we can invoke  constructor  method explicitly 

#  


# class Test:
#     def __init__(self):
#         print("special method")
#     def get_detailes(self):  
#         print("hhjjj")  
#     @classmethod
#     def update_test(cls): 
        



