class test:
    a=10 # static or class variable  
    # constuctor method
    def __init__(self):
        #  if variable variables are varied from object to object  known as instance variable
        self.b=20
    # instance method
    # instance variable--> if the variable values are varied or changed  from  one object to another object 
    def f1(self):
        self.c=30
#    class method
    @classmethod
    def f2(cls):    
        cls.d=40
    # static method
    # static variable---> if the variable values are not changed from  one object to another object
    @staticmethod
    def f3():
        pass

obj=test()
obj.f1()
test.f2()
obj.f2()
obj.e=30
# print(test.__dict__)
print(obj.__dict__)

