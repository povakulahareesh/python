
# bytes vs byte array
# bytes object does not support item assignment-->bites are immutable
# byte array is mutable object


# l1=[11,22,33,44,55,7,88,]
# b=bytes(l1)

# # b[0]=77  # it is a immutable

# for value in b:
#     print (value)
#     # print(b)
#

# bytearray

    
# l1=[11,22,33,44,55,7,88,]
# b=bytearray(l1)
# l1[0]=88 # it is mutable and arange is (256)
# for value in b:
#     print (value)


a= bytes([2,23,44,55,55,77,88])
print (a)
print (type(a))
for value in a:
    
    print (value)


