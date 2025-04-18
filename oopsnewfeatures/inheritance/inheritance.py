#  parent class properties access  into child class 
#  parent class members are  access  into child class 
# self is there  known as instance method
#   cyclic inheritance is not possible
#   inheritance :  passing the parent class as an argument to the child class.
'''  
inheritance : reusing the existing class functionality  and  adding and  extending new features 

types of inheritance 
simple 
multiple
multilevel
hirarchical
cyclic inheritance ---> not supporting any programming language 
tommorow--> encapsulstion abstraction polymorphyshim
'''

#   simple inheritance 

# class parent:
#     def m1(self):
#         print("this is  m1 parent method  ")
#     def m2(self): 
#          print("this is  m2 parent method  ")  
# class child(parent):
#     def m3(self):
#         print("child class m3 method")     
# c1=child()
# c1.m1()             
# c1.m2()             
# c1.m3()             

# ========================================
#  java is not supporting multiple inheritance 

#   multiple inheritance  


# class parent1:
#     def m1(self):
#         print("this is  m1 parent1 method  ")
# class parent2:        
#     def m2(self): 
#          print("this is  m2 parent2 method  ")  
# class child(parent1,parent2):
#     def m3(self):
#         print("child class m3 method")     
# c1=child()
# c1.m1()             
# c1.m2()             
# c1.m3()      
# =================================================
#  method resolution order  (mro)
# it can execute based on order
# it can execute based on  inheritance order


# class parent1:
#     def m1(self):
#         print("this is  m1 parent1 method  ")
# class parent2:        
#     def m1(self): 
#          print("this is  m2 parent2 method  ")  
# # class child(parent1,parent2):
# class child(parent2,parent1):
#     def m2(self):
#         print("child class m3 method")     
# c1=child()
# c1.m1()                         
# c1.m2()  

# ============================================================

#  multilevel inheritance 



# class parent1():
#     def m1(self):
#         print("this is  m1 parent1 method  ")
# class parent2(parent1):        
#     def m2(self): 
#          print("this is  m2 parent2 method  ")  
# class child(parent2):
#     def m3(self):
#         print("child class m3 method")     
# c1=child()
# c1.m1()                         
# c1.m2()  
# c1.m3()  


# ==================================================================
# class grandfather ():
#     def ouputgf(self): #function or method
#         print (' am the grandf')
#         # parent inheritant from grand father
#         #  with the help of grandfather parent will be inherited
# class parent(grandfather):
#     def ouputp(self): #function or method
#         print (' am the parent')
#         # how to inheritace parent class to child class
#                 # child inheritant from parent
#                         #  with the help of parent, child will be inherited
# class child( parent):
#     def ouputc(self):
#         print (' am the child')

# # now object is created for child
# a=child()
# a.ouputc() #child method 
# a.ouputp()    # parent method
# a.ouputgf()  

# =========================================================

# heirarchical inheritance



# class grandfather:
#     def m1(self):
#         print("this is m1 gf class")
# class parent1(grandfather):
#      def m2(self):
#         print("this is m2 p1 class")
# class parent2(grandfather):
#     def m3(self):
#         print("this is m3 p2 class")
# class child(parent1,parent2):
#     def m4(self):
#         print("this is m3 child class")
# c1=child()
# c1.m1()      
# c1.m2()      
# c1.m3()      
# c1.m4()      























