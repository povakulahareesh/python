
'''interview questions and answers '''


# to avoid program  errors using error handling?  
#  taking data and methods in a single unit  is called encapsulation  
#  inhetritance : creating a new class from already existing class  is known as inheritance 
#  wht are the advantage of inhertance : the main advantage of inheritance is code reusability 
#  how many types nof inheritances are there : 4 types they are : single , multiple, multilevel , hierarchical innhertance 
#  what is method overloading means : writing one or more methods with same name with a different arguments  
# what is method overe riding : writing one or more  methods with the  same name and with the same parameters 
#  where we can implement  method overloading and method  overraiding : in polymorphism we can implement 
#  what is polymorphism:the ability to take many form is called polymorphism
#  what is polymorphism: poly means many and morphism means forms  polymorphism means  ability to existing many forms  
#  why we are calling python is a dynamically  typed language : in python we are not declaring the data types explicitly at the time of variable declaration 
# python is dynamically typed languge  because the  python inbuilt  method determines a  type of variable   at the time of run time 
#   what is the defination of name space's in python : name spaces in python are containers   that holds the class names and variables names , method names  ,
#  what is copresullution in python :  means  that determines the value place in a  manual of function  with in a program  based on location within the code  they are two gtype so  scope in python  local scope and global scope
#  what is python path : python path is a  environmental variable it contains  a list of directories 
# how do you use split function in python :  split function is used to get  multiple values from the user  it breaks the input by using a  separator  by default the separator is there   
#   what is the difference between end  and separator parameterrs in python:end is used to print the next line and separator is used to separate  the values 
#   what is the difference between end  and separator parameterrs in python:end and separator both are parameters  used along with print function  in parameter is used   that specifies what should be   printed  at the end of the output   separate parameter  by default the end parameter is next line  charater  separate parameter  that specifies what sholud be printed between two elements by default the  separate parameter is white space  if we given white space  there  should be a space between two elements 

#  what is the list:  list is similar to array  it  holds heteroginous type of data   
#  heteroginous type of data means different type of data  like string ,float , int 
#  can you name some methods in list : 
#  what is tuple: tuple is similar to list but it is  immutable  it means we cant change  the  value of tuple  .,, it also stores heteroginous data   
#  write a program to remove  duplicate charaters in a given string : 


''' 
second interview :
what is python :
it is a computer based programming language 
it is to build  websites and software 
 it is a object oriented programming language 
   
 
 it is statically typed are dynamically typed?
  there are some inbiuilt functions are there so tell me about map and filter?:
   the  difference between map and filter ?
   what are the loops available in python?
   what are the loop control statements in the python ? ---> break, continue and pass
   do you know functions in python ?  --> they are user defined function and built in functions 
    what are parameters ? 
do you know about pip in python? (package installer for python )
pip can be used to install and uninstall . install specific version  packages in python 
 what is pep ?( python enhancement proposal)
* it's super important for understanding how Python works behind the scenes
 what is data abstraction ? how we  achive data abstraction in python?
  what is inheritance ? 
 what is iterators ?
 *An iterator is an object in Python that allows you to loop over (or iterate through) a collection, one item at a time.
  do you know closures in python?
  how we can use nested function outside of the main function ? 
   what are the libraries do you know ? 
   compile ,pandas and numpy 
   do you know files in python ? -->text files and binary files 
'''

s="harish"
l=[]
for ch in s:
    if ch not in l:
        l.append(ch)
        output="".join(l)
        print(output)

'''explanation:


        ✅ Why use "".join(l)?
"".join(l) converts the list of characters like ['h', 'a'] into a string like "ha".

This gives a clean, readable output instead of printing the list itself.

✅ What happens with "harish"?
Let’s go step by step:


Character (ch)	Is it in l?	l after appending	Printed output
'h'	No	['h']	h
'a'	No	['h', 'a']	ha
'r'	No	['h', 'a', 'r']	har
'i'	No	['h', 'a', 'r', 'i']	hari
's'	No	['h', 'a', 'r', 'i', 's']	haris
'h'	Yes! (already in list)	No change	Nothing printed

        
        
        '''


#   not in  example

# l = ['a', 'b', 'c']
# print('a' not in l)   # False (because 'a' *is* in the list)
# print('x' not in l)   # True  (because 'x' is *not* in the list)



# import mysql.connector
# dbcon=None
# try:
#     dbcon=mysql.connector.connect(host='localhost',
#                                   user='root',
#                                   password='root',
#                                   database='harish')
#     cursor = dbcon.cursor()
#     sql_st='''
#             create table employee(
#             eid int,
#             ename varchar(32),
#             esal float
#             );
#            '''
#     cursor.execute(sql_st)
#     dbcon.commit()
#     print("Table Created Successfully")

# except mysql.connector.DatabaseError as err:
#     print(err.msg)

# finally:
#     pass




