# # // positional arguments 
# def add (a,b):
#     # print(a-b)
#      print(a+b)
#     #  argument position meands + and - 
#     #   if we are changing  the argument  position  what happen here  we are getting different values
#     #  if we change the position  we are getting  different values 
# add(10,20)    
# add(20,10)    
# ================================================================

# key word arguments 

# def add (a,b):  
#  print(a-b)
# #  print(b-a)
# #  print(a+b)
# #  position means like addition , substraction 
# # priviously  if we change the position of  arguments we are getting different results 
# #  even we are changing  the position differently but we are declaring as a     keyword arguments    
# # a&b is a keyword arguments 
# #  a,b is parameter or formal arguments  

# add(a=10,b=20)    
# add(b=20,a=10) 
# ===========================================

# def add (a,b,c):
#     print(a+b+c)
# add(a=10,b=20,c=30)  
# =====================
# default argument 
#  we are providing default value for our  positional atrguments  
#  default value 


# def add (a,b,c=100):
#     print(a+b+c)
# add(a=10,b=20)  
# ===================================

#  variable length arguments (*)
# def add (*a):
#     print(a)
# add(10)    
# add(10,20)    
# add(10,20,30)    
# add(10,20,30,40)    
# add(10,20,30,40,50)    
# add(10,20,30,40,50,60)  
# ==============================
#  functionm doing some business logic and return  some value 
#  multiple values are also possible
#   only python negative index is possible for  list  and
#  in function level we can return multiple values only  
#   function is going to return multiple values  
# #   
   
# def add (a,b):
#     return 10,20
#     # return a+b 
# print(add(1,2))
# #  java and java script return only single value  
# #  python return multiple values 

# ==================================

#  nested function 
#  functionn within  a function known as nested function 


# def add():
#     print("add")
    
#     def sub():
#         print("sunset")
#     sub() 
# add() 

# ===================================
#  orbitary arguments 
#  when we awant to give multiple aruments  on  single parameter we can use (*a)


# def add(*a):
#     print("this is function",a)
# add(1,2,3)    

# =====================================
#  keyword arguments 
#  whenn ewe want to give  arguments  to paramenters in this form (a=1,b=2) we use(**a)
def add(**a):

    print(a)
add(a=1,b=2)    

# ================================
# def add(a,b): # function defination and parameter 
#     return a+b # function body 
# print(add(2,3)) # function call and arguments   
# ============================================



  




