# class Account:
#     '''claass created by Narasimha'''

#     def open_account(self):
#         pass
#     def deposit_amount(self,amount):
#         pass 
#     @classmethod
#     def update_min_bal(cls,amount):
#         pass 
#     @staticmethod
#     def cal_interest():
#         pass

# ============================================
class Account:
    '''claass created by Narasimha'''

    def open_account(self):
        print("account created")
    def deposit_amount(self,amount):
        print("amount deposited ",amount)
    @classmethod
    def update_min_bal(cls,amount):
        print("updated",amount)
    @staticmethod
    def cal_interest():
        print("call")

a=Account()
# a.open_account()
# a.deposit_amount(200)
# a.update_min_bal(77)
# a.cal_interest()
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

# a.open_account()
# Account.open_account(a) # it is the correct way 
# Account.open_account()# — ❌ Error unless you pass an object

#  constructor 
# ======================================

# is a special method to initialize object  values 
#  will execute only once automatically  at the time of object creation 
# we can invoke  constructor  method explicitly 

#  


        
# class Text:
#     def __init__(self,id,name,sal):
#         self.acc_id=id
#         self.acc_name=name
#         self.acc_bal=sal
#     def deposit_amount(self,amount):
#         self.acc_bal=self.acc_bal+amount
            
        
# a=Text(11,"hhh",2000)
# a.deposit_amount(100)
# print(a.__dict__)



# class Text:
#     '''class created by hareeesh '''
#     a=10
#     def __init__(self):
#         self.b=20
#         self.c=30
#     def m1(self):
#         self.d=90
# t1=Text()            
