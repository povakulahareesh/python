# class employee:
#  we are using static method decorator
#     @staticmethod
#     def m1():
#          pass
#     @classmethod   
#     def m2():
#         pass

# ==================================
#  i have one more function is there  am adding some decorator here 
#  what is the decorator user upper case
def   user_uppercase(func):
    def innner():
        msg=func()
        return  msg.upper()
    return innner 
#  decorator takes one function as a argument  and return modified function
     # the main objective of decorator function is   it return  extend functionality of the existing function 
     # just am adding some decorator      
#  decorator is a function  take add() function as a argument  and return  modified functionality    
#  decorator can convert  my value to upper case 
#  decorator can modify  the  functionality 
#  am adding some decorator 
@user_uppercase 
def add():
    return "hii rahul thathooi"
print(add())

