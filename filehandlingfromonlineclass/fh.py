#   when we get filenotfound error we need open on present folder 

''' file handling:-->we need to open some  file in read mode and write mode or append mode 
---  file handling --> means-->we are exchanging the data  between multiple systems  throw the json or csv files 
--- to work with csv  or json or exl files we have to handle  files 
--- basically we have two types of  files   text files and binary files 

text files: 
 any file it contains the character data known as text file 
 in case of text files what is the mode read ,read+ w w+,a,a+,x
 
binary files: audio files , vedio , images 
 in case of binary  files what is the mode rb ,rb+ wb ,wb+,ab,ab+,xb
it converting zero  and  ones 


we exchange data throw the  xml formate and json formate 
we need to read the data , we need to convert the data
 there are some inbuilt functions  or  methods 

 open()--function 
open(provide our file name,mode )
fp.close(   )

read operation some methods are there 
 read()method---> raed whole file  content 
  read(n)---> read n no of characters 
  readline()---> read first line
  readlines() --> read lines in the form of list 

  write()are also some methods are there 
  write()
  writeline()
  write(strvalue)
  writelines(list of lines )

  ==========================

  file modes:
r:
r+:
w:
write means override is going to happen 
write means override is not going to happen 
w+:
a:
a+:

# '''
# #  we will get the file pointer 
# #  read
# fp=open("hii.txt","r")
# data=fp.read()
# print(data)
# fp.close()
# #  write 
# fp1=open("hii1.txt","w")
# fp1.write(data)
# fp1.close()

# #  read only 2 characters 
# fp=open("hii.txt","r")
# data=fp.read(2)
# print(data)
# fp.close()


# #  read onlyfirst line 
# fp=open("hii.txt","r")
# data=fp.readlines()
# print(data)
# fp.close()


