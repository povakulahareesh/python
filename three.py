# a,b,c=2,9,8
# print(a)
# print(b)
# print(c)



# x=True
# print (type(x))




# x=2
# print (float(x))

# x=2.5
# print (int(x))


# x=int (input("enter first number:"))
# y=int (input("enter the second number:"))
# z=x+y
# print( z ,"finalanswer")


# x=True
# print(int(x))




# #division
# a=9
# b=3
# print(a/b)

# #modulas
# a=9
# b=3
# print(a%b)

#conversions

# x=[5]
# y=[5]++
# z=x
# print(x  is y)
# print(x is z) 

#conditional statements

# a=10
# c=30
# if a<30:
#     print("right") 
# else:
#  print ("wrong")


# a=55
# b=55
# if a>b:
#    print("wrong")
# # elif a==b:
# else :
#     print ("right")


#print even or odd

# num = int (input())
# if num  %2== 0:
#     print ("even")
# else:
#   print("odd")


  #positive or negative given number


# num = int (input())
# if num>0:
#     print ("positive")
# elif num<0:
#   print("negative")
# else:
#     print("zero")

#loops ("for loop")

# for i in range (0,55,2):
#     print(i)

# for i in range (0,55):
#     print(i)

#even or odd
# #even
# for i in range (0,55):
#      if i%2==0:
#           print(i)

#           #odd
        
# for i in range (0,55):
#      if i%2==1:
#           print(i)



#tables

# num= int(input())
# for i in range (1,22):
#     print(num,"*",i,'=' ,num*i)




# num = int (input())
# for i in range (1,11):
#     #  print(num,"*",i,"=" ,num*i)
#     print(num,"*",i,"=",num*i)

# # while loop
# i=1
# while i<=10:
#   print(i)

#   i+=


  # until we give condition
  # we  skip one iteration we use continue
  # break statement it will stop iteration
  # pass is nothing but in  any block 
  # if we want to skip the some function we have to use pass statement or any function 
  # pass used to stop error in empty statement
# break


# for i in range(5):
#     if i == 3:
#         break  # Exits the loop when i == 3
#     print(i)

# # continue
# for i in range(5):
#     if i == 3:
#         continue  # Skips the print statement when i == 3
#     print(i)

# # pass 
# for i in range(5):
#     if i == 3:
#         pass  # Does nothing
#     print(i)


# functions
# functions is a block of code
# A function in Python is a reusable block of code that performs a specific task.
# def key word can use in functions
# types of functions
# built in functions&user defined functions
# what is indentation
# functions used for code re-usability

# built in functins
# print()
# input()
# int()	
# float()
# str()

#  when we have to given values in declaration part known as arguments


 # positional arguments

# The most common type of argument.
# Values are passed in the same order as the parameters are defined


# def  prostack(a,b,c):
#   return  a,b,c
# print (prostack(9,7,4))



#  Keyword Arguments (Named Arguments)
# Arguments are passed using parameter names (keywords).
# Order does not matter.
# when we want to add particular value for particular variable



# def  prostack(a,b,c)://parameters
#   return  a,b,c
# print (prostack(a=9,b=7,c=4))//arguments
 

#  default arguments

# def  prostack(a=9,b=7,c=4):
#   return  a,b,c
# print (prostack(1,2,3))
# print (prostack(b=66))


# orbitary arguments& *args **args


# arbitary arguments *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# *args

# def function(*args):
#     return sum (args)
# print (function(1,2,2,3,21))

# **kwargs
# we use  **kwargs to store keys & values


# def function(**kwargs):
#     print (kwargs)
# function(name="john",age=22,marks=33)


# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# local scope
# used tyo declare inside  the function known as local scope
# def pro():
#     a=11
# pro()

# a=10

# lists
# lists are used  to store multiple values in single variables
# list can store multiple data types
# array can store only one  data type
# list is hetrogenious data type
# ---means--->we can store multiple data types
# it is a compound data type
# it is a sequencde data type

# list is a mutable--->means ae can change the data
# list = [1,"oop",True]
# # print (list)
# # we want type
# print (type(list))
#  we want type
# mutable means we can change the values in list
# list allow duplicates
# list is denoted in[]

# methods in list
# append


# list=[2,23,45,6,]
# list.append(89)

# print (list)



# list=[2,23,45,6,]

# # sum means add all list values
# print (sum(list))
# 


# insert

# list=[2,23,45,6,]
# # index 0,1,2,3
# list.insert(2,44)
# print (list)



# extend


# extend used to add bulk values in last of list


# list=[2,23,45,6,]

# list.extend([34567,5678,678,4567])
# print (list)
# #  pop

# pop(index) → Removes and returns the item at the given index (default is the last item
# list=[2,23,45,6,]

# list.pop(0)

# # without index it will delete end of list
# print (list)




# remove  --->remove(item) → Removes the first occurrence of the specified item.

# list=[2,23,45,6,]

# list.pop(23)
# # it can remove without index value

# print (list)


# clear


# clear() → Removes all elements from the list.


# list=[2,23,45,6,]

# list.clear()
# # used to remove all value in list

# print (list)


# sort method

# list=[2,23,45,6,]

# list.sort()
# # used for print assending order

# print (list)


# list=[2,23,45,6,]

# list.sort()
# # used for print assending order

# print (list)
  
# for decending order


# numbers = [5, 2, 9, 1, 5, 6]
# numbers.sort(reverse=True)
# print(numbers)  # Output: [9, 6, 5, 5, 2, 1]






# numbers = [5, 2, 9, 1, 5, 6]
# numbers.sort(reverse=True)
# print(numbers)  # Output: [9, 6, 5, 5, 2, 1]


# we can't use stings in sort method


# numbers = ["dd","gf","rd"]
# # for decending order
# # numbers.sort(reverse=True)
# # for assending order
# numbers.sort()

# print(numbers)  # Output: [9, 6, 5, 5, 2, 1]

# count

# count used to count repeated values in list

# numbers = [1, 2, 3, 4, 2, 2, 5, 2]
# count_of_twos = numbers.count(2)
# print(count_of_twos)  # Output: 4

# copy

# copy method used to copy current list


# numbers = [1, 2, 3, 4, 2, 2, 5, 2]
# c = numbers.copy()
# print(c)  


# numbers = ["rfd","ipl","ipl","ipl","ipl"]
# count_of_twos = numbers.count("ipl")
# print(count_of_twos)  









































  
  
  




