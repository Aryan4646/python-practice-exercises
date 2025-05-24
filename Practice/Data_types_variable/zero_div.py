# a program that takes user input for division and handles division by zero gracefully.

def div(a,b):
    try:
        c = a // b
    except ZeroDivisionError:
        print("Invalid denominator can not be zero")
        return None
    else:
        return c

try:
    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))
except ValueError:
    print("Invalid input. Input must be integer.")
else:
    print(f"Number 1 is: {num1}")
    print(f"Number 2 is: {num2}")
    result = div(num1, num2)
    if result is not None:
        print(f"Division of number 1 by number 2 is: {result}")

