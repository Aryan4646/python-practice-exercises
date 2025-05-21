# A Program to calculate the factorial of a number using a
# loop and also using recursion.

num = int(input("Enter the number: "))

# Using loops
# fac = 1
# for i in range(2,num+1):
#     fac *= i
# print(f"Factorial of number {num} is {fac}")

# Using recursion
def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        facto = n * fac(n-1)
    return facto


print(f"Factorial of number {num} is {fac(num)}")