# fp=open("hello.txt","r")
# fp1=open("hello.txt","w")
# data=fp.read()
# fp1.write(data)
# print ("hlo good morning")
# fp.close()
# fp1.close()



#read abc.txt file and write data into new file.
fp1=open("ab.txt",'r')
fp2=open('abc.txt','w')

data=fp1.read()
fp2.write(data)
print("New file Created successfully")
fp1.close()
fp2.close()