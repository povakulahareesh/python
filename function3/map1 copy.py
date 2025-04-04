
# marks=[1,2,3,33,44,55]  # sequence 
# def add (mark):  # function 
#     return mark+1
# # print(add(2))
# map_obj=map(add,marks) # now we are  getting map object
# new_marks=list(map_obj)

# print(marks)
# print(new_marks)

# =======================================================
# #  now we can convert into lamda function 
# marks=[1,2,3,4,5,6,7]
# # def add (mark):  # function 
# #     return mark+1

# #  convert into lamda function 
# #  lambda keyword and argument list and return expression
# #   lambda excepts--> lamda arguments :expression 

# #  map excepting function and sequence 
# print(marks)
# print(list(map(lambda mark:mark+1,marks)))
# #  now we get object  and convert into list 
# ===================================
marks=[1,2,3,4,5,6,7]
#  map execepting function and sequence 
map_obj=map(lambda marks:marks+1,marks)
#  map function return one map object convert into list type 
# now we are getting map object 
new_marks=list(map_obj)
print(marks)
print(new_marks)

