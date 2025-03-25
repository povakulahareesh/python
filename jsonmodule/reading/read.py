# f=open('abc.txt','r')
# f1=f.read()
# print(f1)
# f.close()


# f=open('abc.txt','r')
# f1=open('xyz.txt','w')
# # f5=open('xyh.txt','w')

# f3=f.read()
# print(f3)
# f1.write(f3)
# # f5.write(f3)
# print("creating new file")
# f.close()
# f1.close()
# # f5.close()



f=open('ch.txt','r')
f2=open('abc.txt','w')
f1=f.read()
print(f1)
f2.write(f1)
print("creting file ")
f.close()
f2.close()
