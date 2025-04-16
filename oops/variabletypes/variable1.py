class test:
    a=10
    # constuctor method
    def __init__(self):
        self.b=20
    # isinstance method
    def f1(self):
        self.c=30
#    class method
    @classmethod
    def f2(cls):    
        cls.d=40
    # static method
    @staticmethod
    def f3():
        pass

obj=test()
obj1=test()
obj.f1()
test.f2()
obj.e=30
print(test.__dict__)
print(obj.__dict__)





























