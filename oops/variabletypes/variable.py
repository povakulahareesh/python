# there are three types : instance ,static .class
#  if variable is varied from object to object   go with the instance variable
#  if variable is not varied from object to object   go with the static variable


class Employee:
    '''hloo good morning'''
    org_name="TCS"
    def  __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
        print("constructor")
a1=Employee(11,"haribb",20000)  
# a2=Employee(1,"harib",2000)  
# a3=Employee(111,"hab",200)  
print(a1.__dict__)      
# print(a2.__dict__)      
# print(a3.__dict__)      
print(Employee.__dict__)      



# ---------------------------------------------------



#  instance variable 

'''
create
 inside constructor using self
 inside  instance  method  self  
 inside  static  method  self  
   out side classs using object 

'''



# class Text :
#     def __init__(self):
#         self.a=20
#     def m1 (self):
#         self.b=20 
#     @classmethod
#     def m2 (cls):
#         pass
#     @staticmethod
#     def m3():
#         pass    
# t1=Text()
# print(t1.__dict__)



#  static & class variable 

''' inside  a class -- directly 
 inside a constructor  -- using class name 
 inside a instance method -- class name 
 inside  a class  method -- class and class name 
 inside  a static metyhod -- class name 
 outside a class - using class name 
 '''




  







