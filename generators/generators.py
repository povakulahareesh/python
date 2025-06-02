# generators are functions which  contain  yield keyword
#  there is no return statements 


# def add():
#     yield 1
#     yield 2
#     yield 3
# result=add()
# for value in result:
#     print(value)


# ===========================================

# def add():
#     for i in range(11):
#         yield i
# result= add()
# for value in result:
#     print(value)



def add():
    for i in range(11):
       return i
# a=add()
print(add())

