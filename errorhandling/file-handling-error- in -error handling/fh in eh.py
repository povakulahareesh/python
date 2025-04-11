# a=open("ab.txt","r")
# c=open("abc.txt","w")
# # print(a.read())
# b=a.read()
# c.write(b)
# print("new file created")
# print(b)
# a.close()
# c.close()
# =======================================================


try:
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    print(a/b)
    fp=open("ab.txt","r")
    print(fp.read())
except ZeroDivisionError as err:
    print(a/1)
except ValueError as err:

    print("enter only digits:")
except FileNotFoundError as err:
    fp=open("abc.txt","r")
    print(fp.read())
except:
    print("new error! check the error")
    
finally:
    print("it will execute automatically")
