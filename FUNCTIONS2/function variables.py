'''
📌 Types of Variables in Python Functions:

Local Variables

Global Variables

Function Parameters (Arguments)'''

# 1. ✅ Local Variables
# Defined inside a function and can be used only within that function.


# def greet():
#     name = "Hareesh"  # local variable
#     print("Hello", name)

# greet()
# # print(name)  # ❌ Error: name is not defined outside the function


# 2. ✅ Function Parameters
# Parameters act like local variables that receive values when the function is called.


def greet(name):  # 'name' is a parameter
    print("Hello", name)

greet("Hareesh")  # Output: Hello Hareesh




# 3. ✅ Global Variables
# Defined outside all functions and can be accessed inside functions using the global keyword if modification is needed.


x = 10  # global variable

def show():
    print("x is", x)

def modify():
    global x
    x = 20

show()     # Output: x is 10
modify()
show()     # Output: x is 20


'''
🧠 Key Points

Variables inside a function don’t affect variables outside unless declared as global.

Local variables are destroyed after the function completes.

You can use nonlocal to modify a variable in the enclosing function scope (in nested functions).

'''