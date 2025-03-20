

# ============================================================


# dict 
# group of key values as one entity is known as dict
# duplicatekeys are not allowed 
# duplicate values are allowed
# 



emp={"a":111,
     "b":"hareesh",
     "c":229003}
# print(emp.keys())
# print(emp)

# print(emp.keys())
# print(emp.values())
# print(emp.items())
# print(emp["a"])
# print(emp["b"])
# print(emp["c"])
# print(emp["d"])  #key error
# # specefied key is not there in our dict we get key error



# # print keys
# for key  in emp.keys():
#     print(key)


#     # print values
# for value  in emp.values():
#     print(value)
    
#     #  if we want both keys and valuees usin item
#     # item means combination of key , value


# for item  in emp.items():
#     print(item)

# ======================================================

# pop and pop item
# p0p-->remove key  value  of specified key
# popitem -->remove key  value  of specified keyr 
# or remove orbitary item
# tuple is immutable because we can't doo any insert or delete  operations


emp={"a":111,
     "b":"hareesh",
     "c":229003}
# remove key  value  of specified key
emp.pop("b")
print(emp)
# pop item used to remove object end of the key and value
emp.popitem() # pop item used to remove object end of the key and value
print(emp)
# remove key  value  of specified key


