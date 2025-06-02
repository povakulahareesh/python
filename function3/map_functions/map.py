
# #  without   function
# marks=[2,3,4,5]
# nmarks=[]
# for mark in  marks:
#     nmarks.append(mark+1)
# print(marks)
# print(nmarks)



# ==============================================

#   i want add one mark to every element


#   with function

# marks=[2,3,4,5]
# nmarks=[]
# #  def parameter we give  any  name as  parameter
# def add(m):
#     return m+1
# for mark in  marks:
# #     nmarks.append(mark+1)
#     nmarks.append(add(mark))
# print(marks)
# print(nmarks) 


# marks=[2,3,4,5,6]
# nmarks=[]
# def add(m):
#     return m+1
# for mark in marks:
#     nmarks.append(add(mark))
# print(marks)    
# print(nmarks)    



# # marks = [2, 3, 4, 5]
# # nmarks = []

# # def add(m):
# #     return m + 1

# # for mark in marks:
# #     nmarks.append(add(mark))  # ✅ Corrected this line

# # print(marks)
# # print(nmarks)



#  without for loop 


marks = [2, 3, 4, 5]

def add(m):
    return m + 1

nmarks = list(map(add, marks))  # map applies 'add' to each item in 'marks'

print(marks)
print(nmarks)


