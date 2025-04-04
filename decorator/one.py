#  decorator function

def modify(func):
    def inner(a, b):
        return func(a, b)
    return inner

@modify
def add(a, b):
    print(a + b)

add(1, 2)  # Output: 3
