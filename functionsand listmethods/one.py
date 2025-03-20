'''

froup of statements for specific purpose and execute  some business logic & return the value
 function is denoted with def key word
--- advantage is code reusability
-- using def key word we can create a  function
pass is used to maintain dummy block
add (2,2)-->arguments
def add (a,b)--->parameters
there rae some arguments 
positional arguments 
default arguments 
var length arguments 
named argument
in pythonn functions return multiple values

# '''
# pass is used to maintain dummy block
# 
# def add (a,b):
#     pass
# add(1,2)


# def add (a,b):
#     # print(a+b)

#       return a+b
#     #   print(a+b)
# print(add(1,2))

#   without parameters

# def add ():
#      print("addition")

#     #  Exception has occurred: TypeError
# # add() takes 0 positional arguments but 3 were given
# add (1,2,2)  # actual arguments



# def add (a,b,c):
#         print(a+b+c)
# add (2,3,4)


# def add (a,b):
#         c=1
#         print(a+b)
# r2=add (2,3)
# print(r2)



# def wish():
#     return 1,2,3
# r1=wish()
# print(r1)


# def wish(a,b):
#     return a+b+3
# r1=wish(1,2)
# print(r1)



# def add (a,b):
#     # print(a+b)

#     return a+b
#     #   print(a+b)
# # r1=add(1,2)
# # print(r1)

# print (add(1,2))



# r2=wish(1,23)
# print(r2)
 
 
'''
python -->innerv function --> namless ananymousfunction -->lamda function-->map()-->filter()-->decaration --->
'''

# list tuple set dict crud  methods


# l=["ds","ee","pp","pp","yuio","ertyui","sdfghjk"]
# # print(l.index("ee") )# return index value of specifiedc element
# # l.append("hareesh") # add element into list
# # l.remove("ee") # remove specified elements
# # l.pop() #pop remove end of the list element
# # l.clear()  #clear all list elements
# print(l.count("pp"))  # return no of accurencencess # manam echina elements anni sarlu repeat ayyayo chudachu
# # print(l.index("ee"))
# # print(l)


# list allowed duplicates

# l=    [1,2,3,3,4,4,5,656,78,"ghii","byee","hii","oyyyy"]
# #index 0 1 2 3 4--------------------------------------- 
# print(l)
# # l.append("ll") # insert element at the nd of the list element
# # l.pop() # remove last element from our list
# # l.remove("byee") # remove particular element
# # l.insert(0,"hii") # replace element at particular index value 
# # l.reverse()

# print(l)



# sort and reverse


# sort method 

# l1=[1,25,689,2357,23412,66,3]
# l1.sort ()   # print in proper way # print in assending order or decending order 
# print (l1)


# python modules and python functions




# l=[1,2,33,3,4,4,5,5,6,6,7,8,222,33]
# # l.append("hii")
# # l.sort()
# # l.remove(1)
# # l.pop()
# # l.clear()
# # print(l.index(4))
# # l.reverse()
# # l.insert(0,"kk")
# # print(l.count(1))
# # l.extend()

# print(l)

# ============================================================


# dict 
# group of key values as one entity is known as dict
# duplicatekeys are not allowed 
# duplicate values are allowed
# 



emp={"a":111,
     "b":"hareesh",
     "c":229003}
# print(emp.keys())
# print(emp)

# print(emp.keys())
# print(emp.values())
# print(emp.items())
# print(emp["a"])
# print(emp["b"])
# print(emp["c"])
# print(emp["d"])  #key error
# # specefied key is not there in our dict we get key error



# # print keys
# for key  in emp.keys():
#     print(key)


#     # print values
# for value  in emp.values():
#     print(value)
    
#     #  if we want both keys and valuees usin item
#     # item means combination of key , value


# for item  in emp.items():
#     print(item)



# pop and pop item
# p0p-->remove key  value  of specified key
# popitem -->remove key  value  of specified keyr 
# or remove orbitary item
# tuple is immutable because we can't doo any insert or delete  operations


emp={"a":111,
     "b":"hareesh",
     "c":229003}
# remove key  value  of specified key
emp.pop("b")
print(emp)
# pop item used to remove object end of the key and value
emp.popitem() # pop item used to remove object end of the key and value
print(emp)
# remove key  value  of specified key


