num1 = float(input("Enter the number 1 : "))
num2 = float(input("Enter the number 2: "))

print(f"\nNumber 1 before swap: {num1}")
print(f"Number 2 before swap: {num2}\n")

num1, num2 = num2, num1
print(f"Number 1 after swap: {num1}")
print(f"Number 2 after swap: {num2}")