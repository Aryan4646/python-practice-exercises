# Factorial of a number

def fac(n):
    if n == 0:
        return 1
    else:
        # either this
        # return n*fac(n-1)

        # to understand what is happening
        x = fac(n-1)
        facto = n*x
        return facto

num = int(input("Enter the number whose factorial you want to calculate: "))
# Using Loop
# fac = 1
# if num > 0:
#     for i in range(num,0,-1):
#         fac *= i
#     print(f"Factorial of number {num} is equal to {fac}")


# using recursion
if num>0:
    print(f"Factorial of number {num} is equal to {fac(num)}")
elif num ==0:
    print(f"Factorial of number {num} is equal to {fac}.")
else:
    print("Factorial of only +ve number or 0 can be calculated")

