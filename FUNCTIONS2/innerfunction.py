# function within a function klnown as inner function  
# inside a function we are writting one more function   known as inner function 
#  what is inner function ?--> inside afunction we are writing a function
#   inner function or nested function 

# def outer():
#     print("outer function ")
#     def inner():
#         print ("inner function ")
#     inner()
# outer()
# # xyz()# we  get name error         

# # print(min_bal)# # minimum balance is not there  
# ==============================

# how to execute  inner function  out side the function ?
#  every function have one address is there 
#  knowing function id 
# def mall():
#     pass
#     print(id(mall))
#     def store1():
#         pass
#     def store2():
#         pass
#     print(id(store1))
#     print(id(store2))#  knowing function id 
# mall()
# # print(id(mall))
# # print(id(mall()))
# ============================================>
# how to execute  inner function  out side the function ?--- using  return keyword and function name 


# def outer():
#     print("outer function ")
#     def inner():
#         print ("inner function ")
#     # return 100
#     # return 100,200
#     return inner

#     #  how to invoke inner function out side a function 
#     #  using return the function reference 
# result=outer()
# result()
# result()
# result()
# result()
# # print(result)

# ======================================

# local variable and global variable

# local variable
#  it can t access outside the variable 
# def account ():
#     min_bal=500  # scope is within the function
#     print(min_bal)#
# # local variable : inside function only--> we cant invoke out side the function 
# account() 



#  ======================================

# #global variable scope is entire module  

# a=100  # global variable 

# def funone():
#     print(a)

# def funtwo():
#     print(a)

# def funthree():
#     print(a)

# funone() 
# funtwo() 
# funthree() 

# #  a is a global variable we can access  in all functions  of the module 


# ===============================================================
#  how to cvonvert local variable as  global 
#  convert local variable to global 


# a=10  # #global variable scope is entire module or function  
# def fun1():
#     b=100 #  local variable scope is within the function
# def fun2():
#     a=20
#     print(a+b) 
# fun1()
# fun2()       


# =================================================
#  how to convert local variable as  global 
#  convert local variable to global 

# def fun1():
#     #  using global keyword  we can convert local  variable to  global variable 
#     #  we are convertying local variable to global
#     #  what is the need of global keyword  to declare globle variable as inside a function
#     #  
#     global a
#     a=100
# def fun2():
#     print(a)
# fun1()        
# fun2()        







