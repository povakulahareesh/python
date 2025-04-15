# class add:
#     pass
# a1=add()
# a2=add()
# id
# print(id(a1))# memory allocated can see using  id()
# print(a1)
# print(id(a2))
# print(a2)

# #  class names are going to start with capital letter 
# # class is a template/design/plan/draft/dt/ to create object
# # once object are created memeory allocation will be allocated 
# #  class contains variables and methods 



# variables ---> are three types -->  static,class , instance 
#  methosds: instance method(),class ,static, constr 
# ============================================================



class Account:
    a="hhhh"

    def open_Acc(self):
        #  self :Access instance variables
        #  self : self is a pointer pointing to the current object inside class to access class memebers 
        #  self  is a key word to access class members inside a class & out side a class object 
        print("account opened ")
        
    def deposit_Amount(self):
        print("amount deposited")
    def withdrawl(self):
        print("withdrawl succeess")
a1=Account() 
#  with help of object we can acceess class methods 
a1.open_Acc()       
a1.deposit_Amount()      
a1.withdrawl()   
#  printing object in the form of dict    
print(a1.__dict__)
# __dict__ print all class members in the form of string 
#  printing class   info  in the form of dict 
print(Account.__dict__)

# ====================================

# class Employee:
#     ''' employeee class will be created  '''
#     def get_emp_details(self):
#         pass
