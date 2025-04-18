# Declared inside a class but outside any instance methods.

#  how to create class method using class method decorator 
#  how to create static method using static method decorator 
#  self is a ponter pointing to current object             
#  to refer  your class  members inside a class self  
#  to refer  your class  members outside a class object     
class Account:
    min_bal=400# static variable  # only one copy is going to create  at class level  
    def __init__(self,id,name): # constructor 
        self.name=name
        self.id=id
    def open_account(self): # instance method 
        self.acc_bal=200 # instance variable 
    @classmethod
    def get_min_bal(cls): # class method 
        pass 
    @staticmethod
    def cal_intrest(): # static method 
        tax=5 # local variable 
a1=Account(101,"rahul") 

# am going to print a1 in the form of dict formate  
print(a1.__dict__) 
     #  am printing my class in  the form of dict formate 
print(Account.__dict__)
        