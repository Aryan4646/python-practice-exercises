num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))
print("\nSelect Operation:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
z = int(input("Enter the operation: "))
if z == 1:
    print(f"The addition of {num1} and {num2} is : {num1+num2}")
elif z == 2:
    print(f"The subtraction of {num1} and {num2} is : {num1-num2}")
elif z == 3:
    print(f"The Multiplication of {num1} and {num2} is : {num1*num2}")
elif z == 4:
    if num2 == 0:
        print("Invalid operation 0 can not be in denominator")
    else:
        print(f"The divison of {num1} and {num2} is : {num1/num2}")
else:
    print("Invalid operation Try again")