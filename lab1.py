#1

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
         raise ZeroDivisionError("You cannot divide by zero")
    return a/b

#2
def fibonacci_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n < 0:
        raise ValueError("The number must be positive.")

    a = 0
    b = 1

    for i in range(2,n+1):

        next_value = a + b
        a = b
        b = next_value

    return b

def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        raise ValueError("The number must be positive.")
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
#3
def factorial_recursive(n):
    if n < 0:
        raise ValueError("The number must be positive.")
    if n == 0:
        return 1

    return n*factorial_recursive(n-1)

def factorial_iterative(n):
    if n < 0:
        raise ValueError("The number must be positive.")
    if n == 0:
        return 1

    result = 1

    for i in range(1,n+1):
        result *= i

    return result
#4
def nwd_iterative(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("the number must be an integer")

    if a < 0 or b < 0:
        raise ValueError("The number must be positive.")

    while b != 0:
        a, b = b, a%b
    return a

def nwd_recursive(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("the number must be an integer")
    if a < 0 or b < 0:
        raise ValueError("The number must be positive")

    if b == 0:
        return a

    return nwd_recursive(b,a%b)

#5
def group_files(text):
    if not isinstance(text, str):
        raise TypeError("The argument must be a string")

    files = text.split(", ")

    grouped = {}

    for file in files:
        extension = file.split(".")[-1]
        if extension not in grouped:
            grouped[extension] = []
        grouped[extension].append(file)

    return grouped



