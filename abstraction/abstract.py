# class aontain one or more abstract method known as abstraction ''''


'''
i we dont know about implementation  am going to abstract method 

'''


# class bank:
#     def m1(self):
#         print("hello")

# t1=bank()
# print(t1)
# print(id(t1))

    


# name error 
# class bank(ABC):
#     def m1(self):
#         print("hello")

# t1=bank()
# print(t1)
# print(id(t1))   
# 
# 



# from abc import ABC
# class bank(ABC):
#     def m1(self):
#         print("hello")

# t1=bank()
# # print(t1)
# print(id(t1))  


from abc import abstractmethod,ABC
class Bank(ABC):

    @abstractmethod # decorator 
    def cal_bal(self):
        pass

b1 =Bank()
print(id(b1))  
'''
TypeError: Can't instantiate abstract class Bank 
without an implementation for abstract method 'cal_bal'
'''

