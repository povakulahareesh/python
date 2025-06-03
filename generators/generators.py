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


# =================================
def add():
    for i in range(11):
        yield i
result= add()
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())




# =====================================================

# ✅ 1. Just Print Numbers (Simple Way)

# def add():
#     for i in range(11):
#         print(i)

# add()


# ✅ 2. Return Numbers as a List

# def add():
#     for i in range(11):
#        return list(range(11))
# # a=add()
# print(add())



# ✅ 3. Use a Generator (Best for Big Data / Efficiency)


# def add():
#     for i in range(11):
#         yield i

# for num in add():
#     print(num)




