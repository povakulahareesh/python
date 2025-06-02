# # marks=[1,2,3,4,5,6]
# # reduce(lambda x,y:x+y)

# #  import the reduce function 

# from functools import reduce

# marks=[35,36,37,38,39]
# #  we provide function and sequence  
# #   a value is 35 and b value is 36 == 71 
# #  now  a value 71  b value 37 
# #  same for all elements 
# result=reduce(lambda x,y:x+y,marks)
# print(result)



# ===========================================================

#  inner function 
# def outer():
#     print('outer function')
#     def inner():
#         print('inner function')
#     inner()    
# outer()        
# ==============================================
#  // i want execute inner function outside a function--> # using   return inner function reference only  
#  // using return  function reference  and callable 


# def outer():
#     print('outer function')
#     def inner():
#         print('inner function')
#     #  return inner reference 
#     # return 100 
# #  this time am going to return  inner function reference 
#     return inner
# value=outer() 
# # print(value)
# print(value())

# ==========================================================



# def outer():
#     print('outer function')
#     def inner():
#         print('inner function')

#         #  return inner function reference 
#     return inner
# inner=outer()
# #  outer function reference inner function reference 

# inner()
# inner()

# ==================================================================


# def   user_uppercase(add):
#     def innner():
#         msg=add()
#         return  msg.upper()
#     return innner 
# @user_uppercase 
# def add():
#     return "hii rahul thathooi"
# print(add())
# ======================================

# def user_uppercase(add):
#     def inner():
#         a=add()
#         return a.upper()
#     return inner
# @user_uppercase
# def add():
#     print("hloo jagan")
# add()



#  manam am decorator thisukuntey adhey decorator name thisukovali 


def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        a=func()
        print("After the function runs")
        return a
    return wrapper

my_decorator
def say_hello():
    print("Hello!")  # manually decorate the function

say_hello()

