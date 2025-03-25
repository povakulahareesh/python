# lottery lucky dip system 


from random import randint,choices
l_num=[]
for x in range(10):
    l_num.append(randint(100,999))
print(l_num)
print(choices (l_num))
#  choices means it take lottory lucky single number 
#  choices random number take some list & choice random number doesn't take list
# choice() :  i won't generate any random number  but take some list only  
# =======================================================
# from random import randint,choices

# lotery_NO=[]

# for x in range(10):
#     lotery_NO.append(randint(100,999))
# print(lotery_NO)
# print(choices(lotery_NO))
# ============================================================

# import random

from random  import  choices,choice
ename=["fghjk","ghjkl","uiop","tyuiop","hjkl"]

# print (random.choices(ename))
print (choice(ename)) #--> without array print avudhi


