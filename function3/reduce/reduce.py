#  i want print my total marks 

# reduce() - reduce sequence of elements into a single elements 


# map, filter , reduce ---> excepting one function and  iterator  or sequence 

from functools  import reduce

marks=[1,2,3,4,5,6,7,8,9]
result=reduce(lambda a,b:a+b,marks)
print(result)





