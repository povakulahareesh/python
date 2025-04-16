#  class contains variables and methods we call as classs memebers
#  methods means function
'''class Account:
variable+metyhod
a=account()
print(a)'''


# =======================================================
# class Account:
#     min=200
#     def op(self):
#         print("oo")
#     def ca(self):
#         print("cl") 
# a=Account()
# a.op()
# a.ca()
# print(a.min)
# ============================================================
# '''🧠 What is __doc__ in Python?
# The __doc__ attribute stores the docstring of a module, class, method, or function.

# A docstring is just a special string (usually at the top) that explains what the code does — like a built-in comment or help message.'''  
      


# class Account :
#     #  i am write a docstring
#     # The __doc__ attribute stores the docstring  
#     ''' account class created by narasimha '''
#     min_bal=500
#     def open_Account(self):
#         print("account opened succeess fully ")
# a1=Account() 
# a1.open_Account()       
# print(a1.min_bal)
# #  i want print my document string  how to print
# #  how to print class document string using class name with document attribute
# #  what is purpose of __doc__--> using that information am keeping inside my class 
# print(Account.__doc__)
    # ================================================================


    # variables   are threee types they are  instance variable and static  and local or class

    #  methods are three types --> instance , static ,class
    #  when to use instance variable & static variables
#  any variable value is(varried from object to object) means go with the instance variable
#  any variable value is not  varried from object to object means go with the static  variable
#  static variable    only one copy is going to create  at class  level shared to all objects



# class Employee:
#     def open_account(self):
#         print("account can be opened")
#     def deposit_amount(self,amount):
#         print("amount can be deposited",amount)
# a1=Employee()
# #  with the help of object we are accessing the class members  
# a1.open_account()
# a1.deposit_amount(700)  
# print(Employee.__dict__)   # used to print class in the form of dict       
# print(a1.__dict__)   # used to print class in the form of dict       


# ==============================================

#  constructor 
#  using init attribute we can create a object  
# constructor  is a special method for to initialize object values
 #  at the time of object creation constructor is going to execute automatically  only once 
# Text()    
# we can't execute constructor n no of times  
     # we can't invoke constructor method explicitly  

#  to initialize object value we required constructor 

# class Text :
#     def __init__(self):
#         print("consructor method can be executing")
#         #  at the time of object creation constructor is going to execute automatically  only once 
# Text()        
# Text()        
# Text()        
# Text()        
# Text()        
# Text()        
# ========================================================

# class Text:
#     def __init__(self,a,b):
#         print(a,b)
# Text(1,2)        
# Text("hhh","oooo")        
# =================================================


# self is called instance method 
#  normal method we can write business logic 
#  consructor method   is used to initialize the variables 
#   constructor are going to execute at the time of object creation  to initialize object values
class Employee: 
    ''' required special method  to initialize object values '''
    def __init__(self,id,name,sal):
        self.username=id
        self.userid=name
        self.usersal=sal
        print(" contructor method executing ")
    def open_account(self):  
        print("account opened")  
a1=Employee(102,"harish",3000)
#  normal method we can invoke n no of times 
a1.open_account()
a1.open_account()
a1.open_account()
a1.open_account()

print(a1.__dict__)

# ============================================

#  in java we can write a constructor

# class Account{
#     Account(id,name,amount){
#         this.acc_id=id
#         this.acc_name=name
#         this.acc_amount=amount

#     }
# }
# Account a1=new Account(101,'rahl',60000)




# ===========================================================
# class Employee: 
#     ''' required special method  to initialize object values '''
#     def __init__(self,id,name,sal):
#         self.username=id
#         self.userid=name
#         self.usersal=sal
#         print(" contructor method executing ")
        
#     def open_account(self):
#         print("account can be opened")
#     def deposit_amount(self,amount):
#         print("amount can be deposited",amount)
# a1=Employee(102,"harish",3000)
# #  with the help of object we are accessing the class members  
# a1.open_account()
# a1.deposit_amount(700) 

# # print(Employee.__dict__)   # used to print class in the form of dict       
# print(a1.__dict__)   # used to print class in the form of dict       



