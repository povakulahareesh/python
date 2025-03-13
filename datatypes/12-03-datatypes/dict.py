# colection keys and values as one entity
# key should be immutable vales are mutable
# key will act as index
# no slicing
# 


# if we want to represent key  values as one entity
# duplicate keys are not allowed
# 


# a={"a":122,"b":"ddddd"}
# print (a)
# print (a["a"])
# print (a["dd"])    # key is not available it will give key error


#  membership operator

# sequence means group of elements
# how to verify element present in    sequence or not in operator

unames=["rrr","rrre","rew","rew"]
enames=("ds","rew","rew","rewfd")
eids={101,102,2223,455,55,55}
emp={"eid":1122,"ename":"reddy"}  #dict not use in membership
ename="rahul"
values=range(5,55,3)  #start stop skip

# how to verify element present in    sequence or not in operator

print("rr" in unames)
print("rrr" in unames)
print("ds" in enames)
print(101 in eids)
print("r" in ename)
print("r" in ename)
print(5 in values)
