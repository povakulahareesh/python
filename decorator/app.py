# page check is a decorator  and takes one function as a argument  it modify existing function and return the  modified function 
#  whenever  we want we can  add decorator 


# =====================================================
# def page_check(func):
#     def inner(name,login):
#         if login == False:
#             print("please try to login first")
#         else:
#             return func(name,login) 
#         return inner
# def  home_page(name,login):
#         print("home page",name)
# def order_page(name,login):
#         print("order page",name) 
# def payment_page(name,login):
#         print("payment page",name)       
# home_page("rahul",True)    
# order_page("rahul",True)    
# payment_page("rahul",True)
# ============================================================
# #  i  want to add one decorator
# def m(func):
#     #  am writting one more inner function
#     def inner(name,login):
#         if login == False:
#             print("please try to login first  ")
#         else:
#             return func(name,login)
#     return inner
# #  whenever we want add the decorator nothing but page check 

# def home_page(name,login):
#     print("home page",name)
# @m   
# def order_page(name,login):
#    print("order page",name)
# @m# am adding one decorator
# def payment_page(name,login):
#     print("payment  page",name)
# #  decorator only can apply to order page and payment page 
# #  anyone can access home page without  login also people can access home page 
# #  only order page and login page we need check user has login or not  
# home_page("rahul",True) # home page any one can acceess 
# order_page("rahul",True)
# payment_page("rahul",True)
# home_page("rahul",False) # home page any one can acceess 
# order_page("rahul",False)
# payment_page("rahul",False)
           
#======================================================  
# def hii(func):
#     def inner (a,b):
#             if b==0:
#                   print("hlo mama")
#             else:
#                   return func(a,b)
#     return inner
      
# @hii
# def add (a,b):
#       print(a+b)
# # add(1,2)      
# add(1,0)      


# ===============================================
# def hii(func):
#     def inner(a, b):
#         if b == 0:
#             print("hlo mama")
#         else:
#             return func(a, b)  # ✅ Call the original function
#     return inner  # ✅ Return the wrapper

# @hii
# def add(a, b):
#     print(a + b)

# # Test
# add(1, 0)  # Outputs: hlo mama
# add(1, 2)  # Outputs: 3

# =============================================================
















         