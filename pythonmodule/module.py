# every python file acting as a Module
# module contains --> variables ,functions ,classes
# inbuilt modules--> math , random,csv ,json,request
# pi is part of math module
# pi
# squre root
# ceil -->means top -->high value
# floor--> low value



# print (pi)
# pi is part of math module

# import math 
# print(math.pi)
# print(math.sqrt(100))
# print(math.ceil(9.8))
# print(math.floor(9.8))




#  module containes number --> number contains--> variable function and variable 
'''
import module 
 imoprt module and , module 2 
 if we want all members imort*
 from module import  number 1, number 2, number 3
 from module import number 1 as alia and number 2 as hareesh 

'''
# ====================================

# from math import  pi,sqrt,ceil,floor


# print(pi)
# print(sqrt(100))
# print( ceil(9.3))
# print(floor(9.6))

# ==============================
# from  math import*
# print(pi)
# print(sqrt(100))
# print(ceil(9.3))
# print(floor(9.8))

# ================================

# generate 10  4 digit otp numbers
#  random module random(),randint(),
#  


# import random

# otp_list = [random.randint(1000, 9999) for _ in range(101)]
# print(otp_list)


# ============================================
# import  random
# # help (random)
# print (random.randint(1000,9999))
# =========================================
# write python script
# to generate  100 -4 digit numbers


# from random import randint
# for i in range (100):
#     print(randint(1000,9999))
# 
# ===========================================

# # lottory lucky dip 

from random import randint,choice
lottory_numbers=[]
for x in range(10):
    lottory_numbers.append(randint(100,999))
    print(lottory_numbers)
    print(choice (lottory_numbers))

# ==============================================

#  import random 

# from random import choices,choice
# enames=["sdfgh","tyuio","rtyuiop","fghjk"]

# # printy (random.choices(enames))
# print(choices(enames))


# ===================================


