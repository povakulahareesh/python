# a=5
# b=2
# print(a/b )
# print("buyreee")



# ZeroDivisionError: division by zero
# a=5
# b=0
# print(a/b )  
# print("buyreee")



# a=5
# b=0
# try:
#   print(a/b )  # this is in critical statement 
# except: 
#   print("buyreee")




# a=5
# b=0
# try:
#   print(a/b )  # this is in critical statement 
# #    if try block it work  try block will be printed  if the try block  will be  false  except   block willl be executed 
# #    the moment you get an error  this line this will give you the error  this is where  you will handle it 
# except Exception as e : 

# #  print("hey you cannot divide a number by zero ")
#  print("buyreee",e)  # which is also printed exception messsage which is division by zero 
# #  print("buyreee") 



# a=5
# b=2
# try:
#   print("resource open")
#   print(a/b )  # this is in critical statement 
#   print("resource closed")
# except Exception as e : 

# #  print("buyreee") 
#     print("buyreee",e) 



# a=5
# b=0
# try:
#   print("resource open")
#   print(a/b )  # this is in critical statement 
#   print("resource closed")
# except Exception as e :  # execepty bock will be executed only when we have an  error

# #  print("buyreee") 
#     print("buyreee",e) 
# finally:   # it will execute automatically 
#    print("resoureclosed")  



a=5
b=2

try:
    print("resource open")
    print(a/b )  # this is in critical statement 
    k= int(input("enter a number"))
    print(k)
except ZeroDivisionError as e :  # execepty bock will be executed only when we have an  error

#  print("buyreee") 
    print("buyreee",e) 
except ValueError as v:
    print("invalid input ",v)
except Exception as h:
    print("some thing went wrong ")


finally:   # it will execute automatically 
   print("resoureclosed")  