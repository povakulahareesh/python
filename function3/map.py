# marks=[2,3,4,5]
# nmarks=[]
# for mark in  marks:
#     nmarks.append(mark+1)
# print(marks)
# print(nmarks)
# #  without function


# ==============================================

#   i want add one mark to every element


#   with function

marks=[2,3,4,5]
nmarks=[]
#  def parameter we give  any  name as  parameter
def add(m):
    return m+1
for mark in  marks:
#     nmarks.append(mark+1)
 nmarks.append(add(marks))
print(marks)
print(nmarks)    





