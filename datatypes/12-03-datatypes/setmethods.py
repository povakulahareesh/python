

# set method

# in python we call as dct object

#  group of elements as one entity
# does not allowed duplicates
# order not maintained because indexing not possible
# set object we can iterate using  for loop
# hoe to create  empty set 
# s2=set{} 
# s1.copy()



# update ()  method

# s1.add()
# s1.update(seq)
# s1.union(s2)
# s1.intersection of s2
# s2.add(10)

# delete
#s1. pop()
#s1. remove()
#s1. discord()
#s1. clear()
# 


# s={}
# s1={2,3,4,5,6,66,77,899111,344,55}

# iterate using for loop
# for  eid in s1:
#     print(eid)

# print(s)
# print(len(s))
# print(s1)
# print(len(s1))

# print(type(s))
# print(type(s1))



# crud methods

# s1={2,3,4,5,6,66,77,899111,344,55}
# print(s1)
# s2=s1.copy()
# print(s2)

# copy()-->create new set object

# update    ->add(),update()
# set operation  -->union(),intersection(),symmetric_difference(),difference





# s1={1,2,3,4,5,6,7}

# # add()---->add individual element in our set object
# # update ()--->add multiple methods
# # s1.add(333333)
# s1.update({11,22,33,44,55})
# # oredr not guarenteyy
# s1.update('hii')
# print(s1)




# a={'q','e','r','t','y','u','o'}
# b={'k','v'}
# c="jagan mamayya"

# # a.update(b)
# # print(a)
# a.update(c,{'z','d','f'})
# print(a)



# crud delete methods

# clear ()-->remove all elements from set object

# a={1,2,3,45,6,7,89,22}
# # pop()--->remove ranbdomlly element
# # we can't predicty which element will be removed
# a.pop()
# print(a) 


# remove (x)  vs discard(x)


'''
remove()
if element is present  present   it remove specified element from set
if element  is not present  it  display error 
discard()

if element  is present present  it remove specified element from set
if element  is not present  it doesn't display error 



'''

# s1={101,102,103}
# # s1.remove(101)
# # s1.discard(101)
# # s1.remove(1) #key  error
# s1.discard(1) #no  error
# print (s1)  #{101, 102, 103}


#  tommorow modules packages and functions

# s1={10,20,30,40}
# s2={30,40,50,60}
# print(s1.union(s2)) #duplicates are not allowed
# print(s1.intersection(s2)) # only duplicates can out put
# print(s1.difference(s2))  #  duplicate value remove in s1
# print(s2.difference(s1)) # duplicate value remove in s2
# print(s1.symmetric_difference(s2)) # duplicates remove in those s1&s2     
# # print(s2.difference(s1))



# s1={10,20,30,40}
# s2={30,40,50,60}
# print(s1|s2) #or operator
# print(s1 and s2)
# print(s1-s2)
# print(s2-s1)
# print(s1^s2)



# s1 = {10, 20, 30, 40}
# s2 = {30, 40, 50, 60}

# print(s1 | s2)  # Union (OR operator)
# print(s1 and s2)  # Logical AND (not a set operation, evaluates to one of the sets)
# print(s1 - s2)  # Difference (items in s1 but not in s2)
# print(s2 - s1)  # Difference (items in s2 but not in s1)
# print(s1 ^ s2)  # Symmetric Difference (items in s1 or s2, but not in both)





