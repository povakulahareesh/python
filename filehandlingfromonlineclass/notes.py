#  if swe want to handle that file  we assign one variable
# a=open("hii.txt","r")
# # r=a.readable()
# # r=a.readline(),end="#"     # it will print only first line 
# # r=a.readline()    # it will print only first line 
# # r=a.readline()# it will print only second line 
# # r=a.readline(2)# it will print two characters 
# # r=a.readlines() # read lines in the form of list 
# r=a.read()
# #  using methods we can read the data from the text file 
# print(r)


# #  write data 
# f1=open("harish.txt","w")
# f1.write("hlo girish")
# # f1.write("hlo machiiiii")
# print("file created")
# f1.close()
''' w-- is write ()
r--means read()
a---> append ()
'''

# # append
# f2=open("harish.txt","a")
# f2.write("kkkkkkk")



#  i want copy from a data to b.txt file 

# f=open("a.txt","r")
# f1=open("abc","w")
#  loop for a file
# for data in f:
#     print(data)


#  copy a.txt in the b.txt 

# f=open("a.txt","r")
# f1=open("b.txt","w")
# for data in f:
#     f1.write(data)


#  read iomage file in the binary formate 
# rd=read binary 
#  image can read in the binary formate 
f=open("harishpic.jpg","rb")
f1=open("mypic.jpg","wb")
for i in f:
    f1.write(i)

