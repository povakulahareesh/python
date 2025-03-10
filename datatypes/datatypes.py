# a=102
# b=22.3
# c="hhh"
# d=True
# e=1+22j
# f=[2,3,4,5,6,3]
# g=(2,3,4,5,6,3)
# h={2,3,4,5,6,3}

# i={
#     "a":102,
#     "b":"gh"
# }
# j=bytes(f)
# k = bytearray(f)
# l=frozenset(f)
# def wish():
#     pass
# print (wish())
# print (type(wish()))

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)
# print(j)
# print(k)
# print(f)

# print( type(a))
# print( type(b))
# print( type(c))
# print( type(d))
# print( type(e))
# print( type(f))
# print( type(g))
# print( type(h))
# print( type(i))
# print( type(j))
# print( type(k))
# print( type(f))


#how to represent int data type in python

# a=3487 # how to represent int format using #decimal format -base -10---meands 0-10
# b=0b1111 #binary format--base-2--zero&ones
# c=0o15 #octal format---base-8
# d=0xabd # hexa decimal format---base-16
# print(a) #3487
# print(b) #15
# print(c) #35
# print(d) #2748

# ChatGPT

# You said:

# a=3487 
# b=0b1111 
# c=0o34 
# d=0xabc  
# print(a) #3487
# print(b) #15
# print(c) #35
# explainthis
 
# print(d) #2748
# ChatGPT said:
# This Python code demonstrates different ways to represent integer literals using various number systems:

# Code Breakdown:
# a = 3487        # Decimal (Base 10)
# b = 0b1111      # Binary (Base 2)
# c = 0o34        # Octal (Base 8)
# d = 0xabc       # Hexadecimal (Base 16)

# print(a)  # Output: 3487
# print(b)  # Output: 15 (0b1111 in binary is 15 in decimal)
# print(c)  # Output: 28 (0o34 in octal is 3×8 + 4 = 28)
# print(d)  # Output: 2748 (0xABC in hexadecimal is A×16² + B×16¹ + C×16⁰ = 10×256 + 11×16 + 12 = 2748)


# Explanation:
# Decimal (Base 10):

# a = 3487 is a standard integer in decimal format.
# Binary (Base 2, Prefix 0b):

# b = 0b1111 means 1×2³ + 1×2² + 1×2¹ + 1×2⁰ = 8 + 4 + 2 + 1 = 15.
# Octal (Base 8, Prefix 0o):

# c = 0o34 means 3×8 + 4 = 24 + 4 = 28.
# Hexadecimal (Base 16, Prefix 0x):

# d = 0xABC where:
# A = 10, B = 11, C = 12
# Value = (10 × 16²) + (11 × 16¹) + (12 × 16⁰)
# = (10 × 256) + (11 × 16) + (12 × 1)
# = 2560 + 176 + 12 = 2748

#decimal format - base-10
#default number system in python .allowed digits are 0 to 9
#binary format -base-2
#allowed digits are only 0&1
#literal value prefix with 0b or 0B
#octal format -base-8(0to7)
#literal value prefix with 0o or 0O

#hexa decimal format :base:-16
# 0 to 9 and a-f &A-F
#literal value prefix with 0x or 0X

# float 
# using floating point values(decimal values)
# esal=45.6
# print (type(esal))


# string

# esal="prostack"
# print (type(esal))

# esa="k"
# print (type(esa))

# from keyword import kwlist
# print(kwlist)


# # boolean
# a=True
# print (type(a))

# pyhthon datatype functions
# ===================================
# int(),float(),str(), bool(),complex(),range(),list(),tuple(),set(),dict(),byte(),bytearray(),frozenset()
# None


# complex
# real part and imaginary part

# # range
# r=range(500)
# l1=[100,200,300,400]  
# t1=(100,200,300,400)
# s1={10,20}
# dict={
#     "eid":101,
# "ename":"hareesh"
    
# }
# print(s1)
# print (r)
# all datatypes are holding multiple values
# list:if you want represent group of elements as one entity  nothing but list
# # tuple:list type only but read only version list and it is a read only manner
# set:group of unique elements/duplicates are not allowed
# dictionary:group of key& values

# bytes
# byte array
# frozenset

# l1=[22,22,33,4,56,77,11,673,72,6]
# b=bytes(11)
# ba=bytearray(l1)
# print(type(l1))
# print(type(b))
# print(type(ba))

# byte :means representing group of elements, range  from 0 t0 255 & 0 to 256
# byte is immutable -->means not changeable
#  byte array : means representing group of elements, range  from 0 t0 255 & 0 to 256
# byte array is mmutable-->mmutable


# l1=[22,22,33,22,33,4,4,255]
# b=bytes(11)
# ba=bytearray(l1)
# print(type(l1))
# print(type(b))
# print(type(ba))

# =========================================================

# IDE

# integrated learning environments
# google - search for best ide for python


# how to represent bool type
# print(bool(True))
# print(bool(False))
# # for every datatype there is one function is there with the help of that function we are creating boolean value

# print(bool(0))
# print(bool(1))

# print (bool(100))  #true-non -zero
# print (bool(0))   #false-zero
# print (bool("true")) #true
# print (bool(1.33)) #true
# print (bool(00.00)) #false

# bool(x)
# if x- int type
#     0 means false 
#     non-zero means True

# if x- str type
#x value -empty string -false  otherwise true
# when empty string is there it is false

# print (bool(""))
# print (bool("hjk"))

# if -x -float - 
# -total-number is zero-False 
# otherwise result true


# mutable:mutability-->list,set,dict,bytearray
# immutable:int ,str ,boolean,complex,float,range,bytes,frozenset,tuple ,none
#  immutability: once we create,we can't perform any changes in that object

# immutable
# a=100
# a=200
# a=7
# print(a)

# mutable

# list =[10,20,30]
# print(list)
# list[0]=100
# print(list)

# byte arry-->group of values in  between 0 to 255
# it is a mutable object

# l1=[11,22,33,44,55,7,88,]
# b=bytearray(l1)
# c=bytes(l1)
# for value in b:
#     print(value)

# print(l1)
# print(b)
# print(type(b))
# print(c)
# print(type(c))



# l1=[11,22,33,44,55,7,88,]
# b=bytearray(l1)

# b[0]=77

# for value in b:
#     print (value)
#     # print(b)



    
# l1=[11,22,33,44,55,7,88,]
# b=bytearray(l1)
# for value in b:
#     print (value)




# l1=[11,22,33,44,55,7,88,]
# b=bytes(l1)

# # b[0]=77  # itb is a immutable

# for value in b:
#     print (value)
#     # print(b)


# bytes vs byte array
# bytes object does not support item assignment-->bites are immutable
# byte array is mutable object


# what is bytes datatype
#byte vs byte array
# represent -group of values in between 0-255
# bytes array has mutable &bytes means immutable

# b=bytes([121,22,33,44,56,255])
# ba=bytearray([121,22,33,44,5,255])
# # ba[0]=110
# print (b)
# print(ba)
# ba[0]=11
# print(ba)
# for value in ba:
#     print(value)
# print(b)
# print (type(b))

# print(type(ba))

# ==========================================================

# important datatypes
# list ,tuple,set,dict,string

# all types
v1=100
v2=100.00
v3="jaganmama"
v4=10+4j
v5=True
v6=[]
v7=()
v8={77,33,99}
v9={}
v10=bytes([10,20,30,30])
v11=bytearray([10,20,30,30])
v12=frozenset({10,2,3,4,5,6,7,88,})
v13=range(10)
# am writing one function
def get_deatails():
    pass
v14=get_deatails()
print(v14)




