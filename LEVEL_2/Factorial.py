num = int(input("Enter the number whose factorial you want to calculate: "))
fac = 1
for i in range(1,num+1):
    fac *= i
print(f"Factorial of {num} is {fac}.")