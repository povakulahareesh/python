# str = input ('enter a string')
# #  print number vowel in given string

# vowels =['a','e','i','o','u']

# for s in str:
#     print(s)


# ====================================================


# str = input ('enter a string--->')
# #  print number vowel in given string

# vowels =['a','e','i','o','u']
# count=0
# for s in str:
#     if s in vowels:
#         # print(s)
#         count=count+1
# print(count)


# =========================================
# read only verrsion of list only
# list is mutable
#  in list we can append the values and remove the values
#  in tiple we can't perform update operation  and delete operation
# ===============================================
#  tuple is read only object only 
#   tuple is immutable 
#  once tuple object is created we can't perform any operation s
# indexing is possible 
# tuple 
#  group of elements as one entity is known as tuple
#  it is heterogeneous elements 
#  duplicates are allowed    and insertion order also possible but only the problem is once tuple object is created we can't perform update operation 
#  
# 
# 
#   
# t1=(10,20,39,40,45,66,77,88,11) 
# t2=()  
# t3=11,22,33,44,55,55
# print(t1)
# print(type(t2))
# print(type(t3))
# ====================================
# enames=("dfghjk","t6iop[]","tyuiop[]","sdfgh")
# #  we can access elements using index 
# print(enames)
# print (enames[0])
# print (enames[1])
# print (enames[2])
# print (enames[3])
# print (enames[4]) #  index is not there we get one error -->
# # IndexError: tuple index out of range
# # reading tiple elements  - using - index and slicing

# ==========================================

#  we are accessing tuple slice operator 

#tuple  is immutable 
#  we can't  chandge update or delete 
# ids=(11,22,33,44,55,66,77,88,99,8,74,66,33,4)

# print(ids[:])
# print(ids[1:2])
# print(ids[4:20])

# ===================================

# enames=("dfghjk","tiop","tyuiop","sdfgh")
# #  we give index in curly braces
# print(enames[2]) # slicing 
# print(enames[2:3]) # using slice operator 
# =================================
# in list update is possible 

# enames=["dfghjk","t6iop[]","tyuiop[]","sdfgh"]
# enames[0]="hareesh "
# print(enames)

# =======================================

# /tuple is immutable
'''
we can create tuple
 we can read tuple
 we can't update tuple
  we can't delete tuple 

'''
# =================================    # 
# tuple methods
#   index(),--> return index value of specified element --> element is not there we get value error 
# count() --> it return number of occurences of given elements --> repeated elements ni count chesudhi 
#  in tuple there is no sort 
#  using sorted function we can sort the tuple 
# ================================================

# enames=("dfghjk","tiop","tyuiop","sdfgh")
# print(tuple(sorted(enames)))
# print( enames.count("tiop"))
# print( enames.index("tiop"))
# # print( enames.index("tp"))#value error 
# =================================
# a=(22,22,33,44,55,66,77,88,99,11,23)
# r=sorted(a)
# print( tuple(r))


#  inbuilt functions 

# list(),str(),bool(),float(),complex(),list(),tuple(),set,dict, bytes,bytearray,frozenset,range,bin,oct,hex,eval,map, filter ,reduce, sorted, min ,max 

# min()--> return min value  from sequence either list or tuple ,dict,set
# max()--> return max value  from sequence either list or tuple ,dict,set


# a=(22,22,33,44,55,66,77,88,99,11,23)
# print(min(a))
# print(max(a))


# ===================================
#   list are tuple both are grouping the elements only 
#  list[], tuple()
#  group of elements are as a one entity
#    list is a mutable 
#  tuple  is a immutable 
# in tuple there is no update operation and delete operation 
#   where we can use tuple ?--> basically  and object level
# Lists are useful for keeping related items together. 
# Tuples are great for storing data that should not be modified.

# tuple can itererate using while loop for loop


#  for loop 

a=(22,22,33,44,55,66,77,88,99,11,23)
# for i in a:
#     print(i)

# while loop 
i=0
while i<=len(a)-1:
    print(a[i])
    i=i+1
#   read only version of list only 




