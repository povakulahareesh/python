#  map,filter,reduce these all are excepting function and  sequence as a argument

# numbers =[1,2,3,4,5,6,7,8,9,10]
# odd_number=[]

#  without function 

# for num in numbers:

#     if num%2 !=0:
#         odd_number.append(num)
# print(odd_number)        
# print(numbers)        
# ===============================================
#  with function

#  what is sequence  ----> collection of elements known as a sequence
# In Python, a sequence is an ordered collection of elements that can be accessed by their index, and includes types like lists, tuples, and strings. 
#  sequence is nothing but a  collection of elements that can be accessed by their index  like list ,tuple,strings 
#  


# #  with function

# numbers =[1,2,3,4,5,6,7,8,9,10]
# def odd(number):
#     if number%2 !=0:
#         return True 
#     else:
#         return False
#      # filter excepting function and  sequence  
# print(list(filter(odd,numbers)) )   
# print(numbers)

# ============================================


#  with function

# numbers =[1,2,3,4,5,6,7,8,9,10]
# def odd(number):
#     if number%2 !=0:
#         return True 
#     else:
#         return False
#      # filter excepting function and  sequence  
# new_odd=filter(odd,numbers)
# odd_num= list(filter(odd,numbers))
# print(numbers)
# print(odd_num)

# =============================================
#  using lambda function 
#  to filter the data we are going to use filter function 


# numbers =[1,2,3,4,5,6,7,8,9,10]

# print(list(filter(lambda number: number%2!=0,numbers)) )   
# print(numbers)

# ==============================================

# from   functools  import reduce

# nums = [1, 2, 3, 4]
# total = reduce(lambda x, y: x + y, nums)
# print(total)  # 10
