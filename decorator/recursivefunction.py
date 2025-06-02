
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)  # function calls itself
        # result = n * 5  # function calls itself
        # result = 6*5*4*3*2*1  # function calls itself
    return result

result = factorial(6)
print(result)

'''
6* factorial(5)
6*5* factorial(4)
6*5*4* factorial(3)
6*5*4*3 factorial(2)
6*5*4*3*2* factorial(1)
6*5*4*3*2*1

n!=n×(n−1)!

# '''

# ✅ What This Code Does:
# This is a recursive function that calculates the factorial of a number.

# 📌 What is a Factorial?
# Factorial of a number n (written as n!) means:

# Copy
# Edit
# n! = n × (n-1) × (n-2) × ... × 1
# Example:

# Copy
# Edit
# 5! = 5 × 4 × 3 × 2 × 1 = 120


'''✅ Python Example:
python
Copy
Edit
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive call

print(factorial(5))
🔍 How it Works:
matlab
Copy
Edit
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0)
= 5 * 4 * 3 * 2 * 1 * 1
= 120



🧠 Key Points:
Term	Meaning
Recursive Call	Function calling itself
Base Case	Condition that stops recursion
Stack Overflow	If no base case, it runs forever

❗ Warning:
If a recursive function does not have a base case, it will run forever and cause a RecursionError.

🔄 Real Examples of Recursion:
Calculating factorial

Fibonacci series

Tree/graph traversal (like DFS)

Solving problems like Tower of Hanoi

📌 Summary:
Concept	Description
Recursive Function	A function that calls itself
Must Have	A base case to stop calling itself
Use Case	When a problem can be broken into subproblems

'''

