'''
 decorator is a function  take one function  nothing but divide function as a argument  
 inside one function is there  it is doing some business logic  return that function reference 

 decorator is similar to  our inner function only 

# decorator is a function and return modified function 
 
 decorator is a function   take one function as a  argument  and return modified function 
'''



# def  division_check(func):
#     def inner(a,b):
#         if b==0: 
#             print("can't divide by zero")
#         else:
#             return func(a,b)
#             # print("hloo")
#     return inner      
#             # print("divide by zero ")
# #   decorator is a function and it take one function as a argument  and modify the function and return modify function  
# #  am adding my decorator 
# #  for our function am adding a one  decorator function  to verify b value 
# @division_check 
# def add(a,b):
#     print (a/b)
# add(10,5) #2.0   
# add(10,0) #ZeroDivisionError: division by zero   
# add(200,10)   

#  ========================================

# #  decorator function 
# #  it excepting  one function and modify the function and retURN modify function
# def modify(func):
#     def inner(a,b ):
#         if b==0:
#             print(" can't divide with zero")
#         else:
#             return func(a,b)
#     return inner    
# # normal function  
# #  just now am adding the decorator 

# @modify 
# # now my function is going to execute as it is  before we are adding one decorator 
# def add(a,b):
#     print(a+b)
# add(1,2)
# add(1,2)
# add(2,0)


# ===============================================================================

